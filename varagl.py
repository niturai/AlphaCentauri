import numpy as np
import matplotlib.pyplot as pl
from scipy.interpolate import RectBivariateSpline
from obslen import jd, base
from aper import aper, aperrad, b
from intfer import rotate, grids, signal


#observation Julian day
jd = jd

# three dimensional baseline
east = np.real(base[4])
north = np.imag(base[4])
up = 1e-6

xt,yt = rotate(east,north,up,jd)
gX,gY,wX,wY = grids(xt,yt,aperrad)

psi = [1.75, 1.77, 1.78, 1.82, 1.85, 1.87, 1.89] 
sig = []
for i in psi:
    w = aper(wX,wY,b,i)
    g = signal(gX,gY,w)
    xgr = gX[0,:]
    ygr = gY[:,0]
    z = np.transpose(abs(g))
    spline = RectBivariateSpline(xgr,ygr,z)
    sig.append(spline.ev(xt,yt))

gt = sig

pl.rcParams.update({'font.size': 15})
text_kwargs = dict(ha='center', va='center', fontsize=20)
pl.plot(jd,gt[0], linestyle='solid', color='black', label='100.3$^\circ$',markersize=20)
pl.plot(jd,gt[1], linestyle='dashed', color='green', label='101.4$^\circ$',markersize=20)
pl.plot(jd,gt[2], linestyle='dashdot', color='cyan', label='102.0$^\circ$',markersize=20)
pl.plot(jd,gt[3], linestyle='solid', color='blue', label='104.3$^\circ$',markersize=20)
pl.plot(jd,gt[4], linestyle='dotted', color='red', label='106.0$^\circ$',markersize=20)
pl.plot(jd,gt[5], linestyle='dashed', color='deeppink', label='107.1$^\circ$',markersize=20)
pl.plot(jd,gt[6], linestyle='dotted', color='lime', label='108.3$^\circ$',markersize=20)
pl.xlabel('Julian Day', ha='center', fontsize=20)
pl.ylabel('correlated Signal $g_w(u)$', fontsize=20)
pl.title('According to mask orientation',**text_kwargs)
pl.ylim(0.48,0.70)
pl.legend(bbox_to_anchor=(0.89, 0.4))
pl.gcf().set_size_inches(10, 10)
pl.show()

