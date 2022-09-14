import numpy as np
import matplotlib.pyplot as plt
from obslen import jd, base
from intfer import sigma, smdata

np.random.seed(2)

# julian day observation for 60 sec apart
def int_jd():
    bj =[]
    for i in range(45):
        bj.append(jd[i*20+10])
    return np.array(bj)

jday = int_jd()

# simulated data from each baseline with 1 sec observation
sd = smdata(sigma*np.sqrt(1000))     # only one night, with 10 channels
nsd = smdata(0)

# only for one baseline (1,-3)
sd = sd[4]
nsd = nsd[4]

# Mean of data in 60 sec interval
def bin_data():
    data = []
    ebar = []
    for i in range(45):
        bin = sd[i*20:(i+1)*20]
        data.append(np.mean(bin))
        ebar.append(np.std(bin)/len(bin)**.5)
    return np.array(data), np.array(ebar)

sdata, sebar = bin_data()
xerr = 10/86400

plt.rcParams.update({'font.size': 20})
text_kwargs = dict(ha='center', va='center', fontsize=20)
plt.plot(jd, sd,'.', color='gray')
plt.plot(jd, nsd, color='crimson')
plt.errorbar(jday, sdata, yerr=sebar, xerr=xerr, color='blue', fmt='o')
plt.xlabel('Julian Day', ha='center', fontsize=20)
plt.ylabel('Correlated signal $g_w(u)$ with noise', fontsize=20)
plt.title('Signal for baseline (E,N) = (1,-3)')
plt.gcf().set_size_inches(10, 10)
plt.show()

