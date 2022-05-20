import numpy as np
import scipy.optimize as sciopt

pi = np.pi
cos = np.cos
sin = np.sin


def rotate(x,y,omega,I,Omega):
    cs,sn = cos(omega), sin(omega)
    x,y = x*cs - y*sn, x*sn + y*cs
    cs,sn = cos(I), sin(I)
    x,y,z = x, y*cs, y*sn
    Omega += pi/2
    cs,sn = cos(Omega), sin(Omega)
    x,y,z = x*cs - y*sn, x*sn + y*cs, z
    return np.array((x,y,z))


def posvel(P,a,e,omega,I,Omega,mean_an):
    ec = (1-e*e)**.5
    mean_an = mean_an % (2*pi)
    psi = sciopt.brentq(lambda psi: psi - e*sin(psi) - mean_an, 0, 2*pi)
    cs,sn = cos(psi), sin(psi)
    x,y = cs-e, ec*sn
    vx,vy = -sn/(1-e*cs), ec*cs/(1-e*cs)
    pos = a * rotate(x,y,omega,I,Omega)
    vel = 2*pi * a/P * rotate(vx,vy,omega,I,Omega)
    return pos,vel  


def bary(m,x):
    N = len(m)
    cm = 0*m
    cm[0] = m[0]
    cx = 0*x
    for n in range(1,N):
        cm[n] = cm[n-1] + m[n]
    cx = 0*x
    for n in range(1,N):
        x[n] += cx[n-1]
        cx[n] = (cm[n-1]*cx[n-1] + m[n]*x[n])/cm[n];
    b = cx[N-1]
    x[:] -= b
    return x


def getposvel(fname,now=2020):
    fil = open(fname)
    fil.readline()
    star = []
    N = 4
    for n in range(N):
        pars = fil.readline().split()
        pars = [float(s) for s in pars]
        star.append(pars)

    c = 299792458
    yr = 86400*365.25
    au = 149597870700 / c
    deg = pi/180
    GMsun = 4.9254909e-6  
   
    mass = np.zeros(N)
    pos = np.zeros((N,3))
    vel = np.zeros((N,3))

    for n in range(N):
        mass[n] = float(star[n][0]) * GMsun
    for n in range(1,N):
        P,a,e,I,Omega,ep,omega = star[n][1:]
        mean_an = (now-ep)/P * 2*pi
        P *= yr
        a *= au
        I *= deg
        Omega *= deg
        omega *= deg
        pos[n],vel[n] = posvel(P,a,e,omega,I,Omega,mean_an)
    return mass, bary(mass,pos), bary(mass,vel)

mass, pos,vel = getposvel('alphacen_ini.txt')   

fil = open('inic_out.txt', 'w')  
         
N_body = len(mass)
for l in range(N_body):
    fil.write("%22.15e" %mass[l])        
    fil.write('\t')                       
fil.write("\n")                         

for l in range(N_body):
    for k in range(3):
        fil.write("%22.15e" %pos[l,k])        
        fil.write('\t')
    fil.write("\n")                           

for l in range(N_body):
    for k in range(3):
        fil.write("%22.15e" %vel[l,k])        
        fil.write('\t')
    fil.write("\n")                           

fil.close()                                  

print("mass = ",mass)                         
print("pos = ",pos)                           
print("vel = ",vel)                           
print('center of mass position = ',np.sum(mass*pos[:,0])/np.sum(mass))      

