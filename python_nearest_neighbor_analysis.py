import geojson
import sys
import numpy as np
import scipy
from pointpats import PointPattern, ellipse, mean_center, j, g_test
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from pylab import figure, show,rand
from scipy import stats
#import seaborn
#import contextily

fileName = sys.argv[1]
with open(fileName) as f:
    gj = geojson.load(f)

nocache = fileName.split("data")[0]

listArray = []
for feature in gj['features']:
    listArray.append([feature["geometry"]["coordinates"][0], feature["geometry"]["coordinates"][1]])

pp = PointPattern(listArray)
print(pp.max_nnd)
print(pp.min_nnd)
print(pp.mean_nnd)
print(pp.nnd)
print(pp.nnd.sum()/pp.n)
pp.summary()
a = np.array(listArray)
print(stats.zscore(a,axis=1,ddof=1))
gt = g_test(a, support=100, keep_simulations=True)

f,ax = plt.subplots(1,2,figsize=(9,3), 
                    gridspec_kw=dict(width_ratios=(6,3)))
# plot all the simulations with very fine lines
ax[0].plot(gt.support, gt.simulations.T, color='k', alpha=.01)
# and show the average of simulations
ax[0].plot(gt.support, np.median(gt.simulations, axis=0), color='cyan', 
         label='median simulation')

# and the observed pattern's G function
ax[0].plot(gt.support, gt.statistic, label = 'observed', color='red')

# clean up labels and axes
ax[0].set_xlabel('distance (x100000 meters)')
ax[0].set_ylabel('% of nearest neighbor\ndistances shorter')
ax[0].legend()
#ax[0].set_xlim(0,2000)
ax[0].set_title(r"Ripley's $G(d)$ function")

# plot the pattern itself on the next frame
ax[1].scatter(*a.T)

# and clean up labels and axes there, too
ax[1].set_xticks([])
ax[1].set_yticks([])
ax[1].set_xticklabels([])
ax[1].set_yticklabels([])
ax[1].set_title('Pattern')
f.tight_layout()
plt.savefig(nocache+"_nearest_neighbor_analysis.png")