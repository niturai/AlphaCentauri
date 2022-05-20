import numpy as np
import matplotlib.pyplot as pl

pl.rcParams['font.size'] = '16'

# the general constant values 
c = 299792458.0                  ## in m/s
h = 6.62607015e-34               ## J.s
k = 1.380649e-23                 ## J/K

# constant parameter of binary system 
T_a=5800                         ## Temperature of source A
T_b=5250                         ## Temperature of source B
r_a = 2.10e-8                    ## Radius of source A in radian 
r_b = 1.48e-8                    ## Radius of source B in radian

# Distance from earth in light second 
D = 0.14e9

def pspec(T,arad,nu):
    om = np.pi*arad**2
    z = h*nu/(k*T)
    z = np.clip(z,0,10)
    return om * (nu/c)**2 / (np.exp(z) - 1)

nu = np.linspace(4.2e14,7.8e14,100)

rsol = 2.32
print(r_a*D/rsol,r_b*D/rsol)

fa = pspec(T_a,r_a,nu)
pl.plot(nu/1e12,fa,linestyle='dashed',color='black',label='$\\alpha$ Cen A')
fb = pspec(T_b,r_b,nu)
pl.plot(nu/1e12,fb,linestyle='dotted',color='black',label='$\\alpha$ Cen B')
pl.gcf().set_size_inches(8, 8)
pl.legend()

pl.xlabel('$\\nu$ (THz)', fontsize=18, labelpad=10)
pl.ylabel('$\\Phi$ ($10^{-4}\\rm\\,photons\\;m^{-2}\;s^{-1}\;Hz^{-1}$)', fontsize=18, labelpad=10)
current_values = pl.gca().get_yticks() * 1e4
pl.gca().set_yticklabels(['{:.1f}'.format(x) for x in current_values])


def f2l(nu):
    return c/nu / 1e3

def l2f(lam):
    return c/(lam+1e-30) / 1e3


secax = pl.gca().secondary_xaxis('top', functions=(f2l,l2f))
secax.set_xlabel('$\\lambda$ (nm)',fontsize=18, labelpad=10)

pl.tight_layout()
pl.show()

