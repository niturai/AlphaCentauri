import numpy as np
import matplotlib.pyplot as pl
from scipy.interpolate import RectBivariateSpline
from obslen import jd, base
from aper import aper, aperrad, psi
from intfer import rotate, grids, signal


#observation Julian day
jd = jd

# three dimensional baseline
east = np.real(base[4])
north = np.imag(base[4])
up = 1e-6

xt,yt = rotate(east,north,up,jd)
gX,gY,wX,wY = grids(xt,yt,aperrad)

b = [0.0211, 0.0215, 0.0220, 0.0225, 0.0230, 0.0235, 0.0240] 

sig = []
for i in b:
    w = aper(wX,wY,i,psi)
    g = signal(gX,gY,w)
    xgr = gX[0,:]
    ygr = gY[:,0]
    z = np.transpose(abs(g))
    spline = RectBivariateSpline(xgr,ygr,z)
    sig.append(spline.ev(xt,yt))

gt = sig
pl.rcParams.update({'font.size': 15})
text_kwargs = dict(ha='center', va='center', fontsize=20)
pl.plot(jd,gt[0], linestyle='dotted', color='black', label='21.1mm',markersize=20)
pl.plot(jd,gt[1], linestyle='dashed', color='green', label='21.5mm',markersize=20)
pl.plot(jd,gt[2], linestyle='dashdot', color='cyan', label='22.0mm',markersize=20)
pl.plot(jd,gt[3], linestyle='solid', color='blue', label='22.5mm',markersize=20)
pl.plot(jd,gt[4], linestyle='dotted', color='red', label='23.0mm',markersize=20)
pl.plot(jd,gt[5], linestyle='dashed', color='deeppink', label='23.5mm',markersize=20)
pl.plot(jd,gt[6], linestyle='dashdot', color='lime', label='24.0mm',markersize=20)
pl.xlabel('Julian Day', ha='center', fontsize=20)
pl.ylabel('Correlated signal $g_w(u)$', fontsize=20)
pl.title('According to mask width',**text_kwargs)
pl.ylim(0.48,0.70)
pl.legend(bbox_to_anchor=(0.89, 0.4))
pl.gcf().set_size_inches(10, 10)
pl.show()

