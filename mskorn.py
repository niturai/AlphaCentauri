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

b = 0.0225

text_kwargs = dict(ha='center', va='center', fontsize=14)

for n in np.linspace(1,2,51):  #best value: wavelength/angular_separation
    w = aper(wX,wY,b,n)
    g = signal(gX,gY,w)
    
    pl.subplot(1,3,2)
    pl.contourf(wX,wY,w)
    pl.colorbar(shrink=0.60)
    pl.gca().set_aspect('equal')
    pl.title('Mask orientation %5.0f' % (np.round(n*180/np.pi)) +'$^\circ$', **text_kwargs)

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
    pl.xlabel('Julian Day', dict(fontsize=12))
    pl.ylabel('correlated Signal', dict(fontsize=12))
    pl.title('According to mask orientation',**text_kwargs)
    pl.ylim(0.45,0.75)
    pl.pause(.04)
    pl.clf()
    
