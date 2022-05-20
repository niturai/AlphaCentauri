import numpy as np
from itertools import combinations

# convert deg and hour to rad
def raddeg(d,m,s):
    return (d + m/60 + s/3600) * np.pi/180

def radhr(hr,m,s):
    return (hr + m/60 + s/3600) * np.pi/12

# the position of source Alpha Centauri
ra = radhr(14,39,35.06311)
dec = raddeg(-60,50,15.0992)

# the position of baseline (Mt. John NZ)
lat = raddeg(-43,59,12.0)
lon = raddeg(170,27,54.0)

# wavelength of observation 
lam = 6e-7

# resolution time
delt = 4e-10

# observation day
day = 2460000                  # 24 feb 2023

# sqrt(channels x nights)
chnl = 100

# observation duration
Nobs = 1/2                       # each for 12 hour of night

# Number of observation night (observation length)
Night = 1 

# average time of observation
M = int(Nobs * 86400 + 1)                   #  dots 1 sec apart

julday = []
for i in range(0, Night, 1):
    jday = np.linspace(day + i, day + i + Nobs, M)
    julday.append(jday)

jd = np.array(julday).flatten()     # total observation time according to Julian time

# Telescope position
comb = combinations([0+0j, 3+4j, 1+5j, 4+1j],2)

# Number of baselines for observations
base = []
for i in list(comb):
    base.append(i[1] - i[0])

base = base



