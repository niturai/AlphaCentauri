import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 35})

pos = [0+0j, 3+4j, 1+5j, 4+1j]

east = np.real(pos)
north = np.imag(pos)

def conpt(east,north,e,n):
    e1, e2 = east[e], east[n]
    n1, n2 = north[e], north[n]
    plt.plot([e1, e2], [n1, n2], '--', linewidth=6.0)

x = np.linspace(-0.5,4.5,500)
y = np.linspace(-0.5,5.5,500)
 
x,y = np.meshgrid(x,y)

def circ(x,y,rad):
    f = 0*x
    f[x*x + y*y < rad**2] = 1
    return f

def aper(x,y):
    phi = -1.82                                              
    cs, sn = np.cos(phi), np.sin(phi)
    x, y = cs*x - sn*y, sn*x + cs*y
    return circ(x,y,0.20) * np.cos(np.pi*x/0.095)**2          # the masking width 0.095 is a example. 


w = aper(x-0,y-0)
w1 = aper(x-3,y-4)
w2 = aper(x-1,y-5)
w3 = aper(x-4,y-1)

fig, ax = plt.subplots()
cntr = ax.contour(x,y,w, colors='gray')
cntr1 = ax.contour(x,y,w1, colors='gray')
cntr2 = ax.contour(x,y,w2, colors='gray')
cntr3 = ax.contour(x,y,w3, colors='gray')

## connect baseline ##
conpt(east,north,0,1)
conpt(east,north,2,3)
conpt(east,north,0,2)
conpt(east,north,0,3)
conpt(east,north,1,2)
conpt(east,north,1,3)

ld,_ = cntr.legend_elements()
ld1,_ = cntr1.legend_elements()
ld2,_ = cntr2.legend_elements()
ld3,_ = cntr3.legend_elements()

plt.xlabel('East', fontsize=35)
plt.ylabel('North', fontsize=35)
plt.gcf().set_size_inches(18, 18)
plt.show()


