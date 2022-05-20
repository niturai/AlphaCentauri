import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import re
import pickle
from dynesty.utils import resample_equal

# position of orbit in sky
dAB = np.load("dAB.npy")
X = dAB[0,0]
Y = dAB[1,0]
truth = [X,Y]

# number of parameter to estimate
pnames = ('$X (ls)$', '$Y (ls)$')
ndim = len(pnames)

# Number of night to observe
Night = np.arange(1,34,1)

# create different interferometric data for different number of night and upload here 
filnames = glob('*dres*')
filnames.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)',x)])

sample = []
for f in filnames:
    infile = open(f,'rb')
    results = pickle.load(infile)
    infile.close()

    weights = np.exp(results['logwt'] - results['logz'][-1])
    sample.append(resample_equal(results.samples, weights))

postsamples = np.array(sample)

# error in x And y using postsamples
err_x = []
err_y = []

for i in range(len(postsamples)):
    samplei = np.copy(postsamples[i])

    p_x = np.percentile(samplei[:,0],[16,50,84])
    p_y = np.percentile(samplei[:,1],[16,50,84])

    err_x.append(p_x[2] - p_x[1])
    err_y.append(p_x[2] - p_x[1])

error_x = err_x
error_y = err_y

# plot interferometric error along with number of night 
plt.rcParams.update({'font.size': 20})
fig, ax = plt.subplots(1,2)
ax[0].plot(Night, error_x, '.', color = 'blue', markersize=15)
ax[1].plot(Night, error_y, '.', color = 'green', markersize=15)
ax[0].set_xlabel('Number Of Night to Observe Source',fontsize=20, fontweight='bold', color='black')
ax[1].set_xlabel('Number Of Night to Observe Source',fontsize=20, fontweight='bold', color='black')
ax[0].set_ylabel('Interferometric 1-sigma error in x_coordinate (light second)',fontsize=20, fontweight='bold', color='black')
ax[1].set_ylabel('Interferometric 1-sigma error in y_coordinate (light second)',fontsize=20, fontweight='bold', color='black')
plt.gcf().set_size_inches(20, 15)
plt.show()

# plot x-interferometric error along with number of night 
plt.rcParams.update({'font.size': 20})
plt.plot(Night, error_x, '.', color = 'blue', markersize=20)
plt.xlabel('Number Of Night to Observe Source',fontsize=25, fontweight='bold', color='black')
plt.ylabel('Interferometric 1-sigma error in X pos (light second)',fontsize=25, fontweight='bold', color='black')
plt.gcf().set_size_inches(20, 15)
plt.show()

# plot y-interferometric error along with number of night 
plt.rcParams.update({'font.size': 20})
plt.plot(Night, error_y, '.', color = 'green', markersize=20)
plt.xlabel('Number Of Night to Observe Source',fontsize=25, fontweight='bold', color='black')
plt.ylabel('Interferometric 1-sigma error in Y pos (light second)',fontsize=25, fontweight='bold', color='black')
plt.gcf().set_size_inches(20, 15)
plt.show()


