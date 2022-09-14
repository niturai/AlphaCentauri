import numpy as np
import scipy.special as sp
from numpy.fft import fft2, ifft2, fftshift
from scipy.interpolate import RectBivariateSpline
from multiprocessing import Pool
from dynesty import DynamicNestedSampler
import pickle
from obslen import Night, jd, base, ra, dec, lat, lon, lam, delt, chnl
from aper import aper, b, psi, aperrad

# Fourier transform of any function 
def fourier(f):
    return fftshift(fft2(fftshift(f)))

def ifourier(f):
    return fftshift(ifft2(fftshift(f)))

# the general constant value
c = 299792458.0                  # in m/s
h = 6.62607015e-34               # J.s
k = 1.380649e-23                 # J/K

# the constant parameter of binary system 
T_a=5790                         # Temperature of source A
T_b=5260                         # Temperature of source B
R_a = 2.94                       # Radius of source A in light seconds
R_b = 2.07                       # Radius of source B in light seconds
D = 0.14e9                       # Distance from earth in light second 

# position of orbit in sky
dAB = np.load("dAB.npy")
X = dAB[0,0]
Y = dAB[1,0]
truth = [X,Y]
print("position of orbit (X,Y)=", truth)

# observation Julian day 
jd = jd

# three dimensional baseline 
x = np.real(base)
y = np.imag(base)
z = 1e-6

# the rotation of x and y baseline due to earth rotation 
def rotx(x,y,z,a):
    cs,sn = np.cos(a), np.sin(a)
    return x, cs*y - sn*z, sn*y + cs*z

def roty(x,y,z,a):
    cs,sn = np.cos(a), np.sin(a)
    return cs*x + sn*z, y, -sn*x + cs*z

# photon flux from source A or B
def pho_spec(R, T, l):
    a1 = np.pi * (R/D)**2
    a1 *= 1/(l*l)
    a2 = h*c/(l*k*(T + 2.725))
    a2 = np.clip(a2,0,10)
    I = a1 / (np.exp(a2) - 1) 
    return I

# the model (which is HBT correlation) to estimate the parameter
def hbt(x,y,X,Y,l):
    r = np.sqrt(x**2 + y**2)
    v = 2*np.pi/(l*D)

    I_a = pho_spec(R_a,T_a,l)
    n_a = v*r*R_a

    I_b = pho_spec(R_b,T_b,l)
    n_b = v*r*R_b   

    V_a = I_a * 2 * sp.j1(n_a)/n_a  
    V_b = I_b * 2 * sp.j1(n_b)/n_b
    V_ab = V_a * V_b * np.cos(v * (x*X + y*Y))

    return (I_a + I_b)**(-2) * (V_a**2 + V_b**2 + 2*V_ab)


# getting signal with w aperture which is masked with some function 
def signal(x,y,w):
    g = hbt(x,y,X,Y,lam)
    fg = fourier(g)
    fw = fourier(w)
    dfun = fourier(0*x + 1)
    return ifourier(fg*fw*fw)/ifourier(dfun*fw*fw)

# Rotate the baseline according to each hour angle 
def rotate(dx,dy,dz,jd):
    # Define Hour Angle                                         
    gsid = 18.697374558 + 24.06570982441908*(jd - 2451545)   
    sid = (gsid % 24)*np.pi/12 + lon        # in 1 hour 15 degree of rotation of earth
    ha = sid - ra
    dx,dy,dz = rotx(dx,dy,dz,-lat)
    dx,dy,dz = roty(dx,dy,dz,ha)
    dx,dy,dz = rotx(dx,dy,dz,dec)
    return dx,dy

# the grids for taking the observation 
def grids(x,y,aperrad):
    N = 1024
    xup, xdn = np.max(x), np.min(x)
    xmid, xh = (xup + xdn)/2, (xup - xdn)/2   # mid point and hight (amplitude) of x
    yup, ydn = np.max(y), np.min(y)
    ymid, yh = (yup + ydn)/2, (yup - ydn)/2   # mid point and hight (amplitude) of y
    hr = max(xh,yh)
    r = np.linspace(-hr-2*aperrad, hr+2*aperrad, N)
    wX, wY = np.meshgrid(r,r)
    gX, gY = xmid + wX, ymid + wY
    return gX, gY, wX, wY


# Position of baseline will vary as earth rotate 
dist = []
for i in range(len(base)):
    dist.append(rotate(x[i],y[i],z,jd))

distance =np.asarray(dist)          

xt = distance[:,0]                  # baselines in east direction as earth rotate
yt = distance[:,1]                  # baselines in north direction as earth rotate

grid = []                           # grids position in two dimensions 
for i in range(len(base)):
    grid.append(grids(xt[i,:], yt[i,:], aperrad))
    
tgrid = np.asarray(grid)

gX = tgrid[:,0]

gY = tgrid[:,1]

wX = tgrid[:,2]

wY = tgrid[:,3]

# The aperture function
w = aper(wX,wY,b,psi)

# the total flux spectrum
tspec = pho_spec(R_a,T_a,lam) + pho_spec(R_b,T_b,lam)
print('total flux spectrum =', tspec)

# The value of area without masking aperture
area = np.pi * aperrad**2 
print('area=',area)
print('area with masked aperture =', area/2)

# the noise which is equal for all baseline position
sigma = (area * tspec)**(-1) * np.sqrt(delt)/chnl
print('noise =', sigma)

# the true signal value without noise 
g = signal(gX,gY,w)                   # Signal for all baseline

# Create simulated data for all baseline 
def smdata(sigma):
    simu_data = []
    for i in range(len(base)):
        gi = g[i,:,:]
        xgr = gX[i,0,:]
        ygr = gY[i,:,0]
        zi = np.transpose(abs(gi))
        spline = RectBivariateSpline(xgr,ygr,zi)
        simu_data.append(spline.ev(xt[i,:],yt[i,:]) + sigma * np.random.randn(len(jd)))
    
    return np.array(simu_data)

sdata = smdata(sigma)

# total SNR value 
SNR = (1/sigma)*np.sum(sdata**2)**.5
print('total signal to noise ratio = ', SNR)

# the prior transformation 
ini_x = X
ini_y = Y
def trans_prior(theta):
    Xprime, Yprime = theta
    
    X_min = 0.8 * ini_x
    X_max = 1.2 * ini_x
    
    Y_min = 0.8 * ini_y
    Y_max = 1.2 * ini_y
    
    X = Xprime * (X_max - X_min) + X_min
    Y = Yprime * (Y_max - Y_min) + Y_min
    
    return (X, Y)

# the liklihood function 
def lnlikli(l):
    global X, Y
    X, Y = l
    g = signal(gX,gY,w)               # Signal for all baseline
    model_data = []
    for i in range(len(base)):
        gi = g[i,:,:]
        xgr = gX[i,0,:]
        ygr = gY[i,:,0]
        zi = np.transpose(abs(gi))
        spline = RectBivariateSpline(xgr,ygr,zi)
        model_data.append(spline.ev(xt[i,:],yt[i,:])) 
        
    mdata = np.array(model_data)

    G = np.sum(sigma**(-2) * sdata * mdata)
    W = np.sum(sigma**(-2) * mdata * mdata) 

    return 0.5 * (G*G/W - np.log(W))

if __name__ == "__main__": 
    # the parameters name and number of dimension for parameters
    pnames = ('$X pos (ls) $', '$Y pos (ls) $')
    ndim = len(pnames)

    # the sampling function 
    pool = Pool()
    sampler = DynamicNestedSampler(lnlikli, trans_prior, ndim, pool=pool, queue_size=28)
    sampler.run_nested()

    # Save the sample data in form of pickle 
    dres = sampler.results
    out = open('dres.pkl','wb')
    pickle.dump(dres,out)
    out.close()
    pool.close()


