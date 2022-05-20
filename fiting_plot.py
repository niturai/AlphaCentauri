import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
import pickle
from dynesty.utils import resample_equal

# the value of x and y of orbit
dAB = np.load("dAB.npy")
x = dAB[0,:200]
y = dAB[1,:200]

# the value of time t 
t_coord = np.load("t_coord.npy")
t = t_coord[:200,0]

# polynomial order function
zs = np.zeros(14)
def polynom(zs, t, x, y):
    x_t = y_t = 0
    tp = 1
    for p in range(0,len(zs),2):                                          ## range(start, stop, step)
        x_t += zs[p] * tp
        y_t += zs[p+1] * tp
        tp *= t
    return np.concatenate((x-x_t,y-y_t))                                  ## Join a sequence of arrays along an existing axis.

# Find residuals dx1, dy1
res = leastsq(polynom, zs, (t, x, y))                                        ##
zs = res[0]
z_res = polynom(zs, t, x, y)                                              ## sum of array dx1 and dy1
dx1 = z_res[:len(t)]                                                      ## first len(t) is (x-x_t)
dy1 = z_res[len(t):]                                                      ## after len(t) is (y-y_t)

# x(t) and y(t) function to fit the signal
zs = np.zeros(5)
def sinusoid(zs, t, x, y):
    w = zs[0]
    cs = np.cos(w*t)
    sn = np.sin(w*t)
    x_t = zs[1]*cs + zs[2]*sn
    y_t = zs[3]*cs + zs[4]*sn
    return np.concatenate((x-x_t,y-y_t))

# Guess sinusoid parameters
zs = [2.5e-7,1,1,1,1]                                                       

# Find residuals dx2, dy2
res = leastsq(sinusoid, zs, (t, dx1, dy1))                                 
zs = res[0]
z_res = sinusoid(zs, t, dx1, dy1)                                              
dx2 = z_res[:len(t)]
dy2 = z_res[len(t):]

# the Interferometric Data 
infile = open('dres.pkl','rb')
results = pickle.load(infile)
infile.close()

weights = np.exp(results['logwt'] - results['logz'][-1])    # weighting the each nested 
postsamples = resample_equal(results.samples, weights)   # sample for posterior distribution after weighting the each nested 

# the 1-sigma standard deviation for x and y 
p_x = np.percentile(postsamples[:,0],[16,50,84])
p_y = np.percentile(postsamples[:,1],[16,50,84])

err_x = p_x[2] - p_x[1]
err_y = p_y[2] - p_y[1]

yr = 86400*365.25                                                          
per = 2*np.pi/zs[0]/yr
print('periodic part %6.3f yr' % per)
print(zs[0])

## Plotting the results ##
plt.plot(dx1,dy1)
plt.plot(dx2,dy2)
plt.errorbar(err_x, err_y, xerr=err_x, yerr=err_y, fmt='o', label='interferometric error')
plt.xlabel('X residual (light second)',fontsize=20, fontweight='bold', color='black')
plt.ylabel('Y residual (light second)',fontsize=20, fontweight='bold', color='black')
plt.rcParams.update({'font.size': 20})
plt.gcf().set_size_inches(14, 14)
plt.gca().set_aspect(aspect = 'equal', adjustable = 'datalim')
plt.legend()
plt.show()

