import numpy as np

# the radius of aperture 
aperrad = 0.2

# width of masking strip
b = 0.0225

# orientation of aperture
psi = 1.82

# the circular aperture  
def circ(x,y,rad):
    f = 0*x
    f[x*x + y*y < rad**2] = 1
    return f

# with masked function cos(pi*x/b)**2 
def aper(x,y,b,psi):                          # b is for value of masked strip's width
    cs, sn = np.cos(psi), np.sin(psi)
    x, y = cs*x - sn*y, sn*x + cs*y
    return circ(x,y,aperrad) * np.cos(np.pi*x/b)**2


