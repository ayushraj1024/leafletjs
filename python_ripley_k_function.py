import geojson
import sys
import numpy as np
import scipy
from pointpats import PointPattern, ellipse, mean_center, j, g_test, k_test
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from pylab import figure, show,rand
from scipy import stats
import shapely
import fiona
#import seaborn
#import contextily

fileName = sys.argv[1]
with open(fileName) as f:
    gj = geojson.load(f)

nocache = fileName.split("data")[0]

listArray = []
for feature in gj['features']:
    listArray.append([feature["properties"]["longitude"], feature["properties"]["latitude"]])

pp = PointPattern(listArray)
print(pp.max_nnd)
print(pp.min_nnd)
print(pp.mean_nnd)
print(pp.nnd)
print(pp.nnd.sum()/pp.n)
a = np.array(listArray)
print(stats.zscore(a,axis=1,ddof=1))
kt = k_test(a, support=100, keep_simulations=True)


# plot all the simulations with very fine lines
plt.plot(kt.support, kt.simulations.T, color='k', alpha=.04)
# and show the average of simulations
plt.plot(kt.support, np.median(kt.simulations, axis=0), color='cyan', 
         label='median simulation')

# and the observed pattern's K function
plt.plot(kt.support, kt.statistic, label = 'observed', color='red')

# clean up labels and axes
#plt.set_xlabel('distance')
#plt.set_ylabel('% of nearest neighbor\ndistances shorter')
plt.legend()
#ax[0].set_xlim(0,2000)
#plt.set_title(r"Ripley's $K(d)$ function")

plt.savefig(nocache+"_ripley_k_function.png")