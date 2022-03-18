import geojson
import sys
import numpy as np
#from pysal import pointpats
import scipy
from pointpats import PointPattern, ellipse, mean_center
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from pylab import figure, show,rand

fileName = sys.argv[1]
with open(fileName) as f:
    gj = geojson.load(f)

nocache = fileName.split("data")[0]

listArray = []
for feature in gj['features']:
    listArray.append([feature["properties"]["longitude"], feature["properties"]["latitude"]])

pp = PointPattern(listArray)
sx,sy,theta = ellipse(pp.points)
theta_degree = np.degrees(theta)

fig = figure()
e = Ellipse(xy=mean_center(pp.points), width=sx*2, height=sy*2, angle=theta_degree) #angle is rotation in degrees (anti-clockwise)
ax = pp.plot(get_ax=True, title='Standard Deviational Ellipse')
ax.add_artist(e)
e.set_facecolor([0.8,0,0])
e.set_edgecolor([1,0,0])
plt.savefig(nocache+"_sd_ellipse.png")
print(nocache+"_sd_ellipse.png")