import numpy as np
import matplotlib.pyplot as pl
from scipy.interpolate import RectBivariateSpline
from obslen import jd, base
from aper import aper, aperrad
from intfer import rotate, grids, signal

pl.figure(figsize=(13,5))

# observation Julian day 
jd = jd

# three dimensional baseline 
east = np.real(base[4])
north = np.imag(base[4])
up = 1e-6

xt,yt = rotate(east,north,up,jd)
gX,gY,wX,wY = grids(xt,yt,aperrad)

psi = 1.82

text_kwargs = dict(ha='center', va='center', fontsize=14)
for b in np.linspace(.02,.025,51):  #best value: wavelength/angular_separation
    w = aper(wX,wY,b,psi)
    g = signal(gX,gY,w)
    
    pl.subplot(1,3,2)
    pl.contourf(wX,wY,w)
    pl.colorbar(shrink=0.60)
    pl.gca().set_aspect('equal')
    pl.title('Mask width %5.1f mm' % (1e3*b), **text_kwargs)

    pl.subplot(1,3,3)
    pl.contourf(gX,gY,abs(g))
    pl.colorbar(shrink=0.60)
    pl.plot(xt,yt,'.',color='cyan')
    pl.gca().set_aspect('equal')
    pl.title('Track of (E,N) = (1,-3)',**text_kwargs)  

    pl.subplot(1,3,1)
    xgr = gX[0,:]
    ygr = gY[:,0]
    z = np.transpose(abs(g))
    spline = RectBivariateSpline(xgr,ygr,z)
    gt = spline.ev(xt,yt)
    pl.plot(jd,gt)
    pl.xlabel('Julian Day', ha='center', fontsize=12)
    pl.ylabel('correlated Signal', fontsize=12)
    pl.title('According to mask width',**text_kwargs)
    pl.ylim(0.48,0.70)
    pl.pause(.04)
    pl.clf()
    
