import geojson
import sys
import numpy as np
#from pysal import pointpats
import scipy
from pointpats import PointPattern, ellipse, mean_center
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from pylab import figure, show,rand
from shapely.geometry import Polygon 
import shapely.wkt
import shapely.geometry
import json
from geojson import FeatureCollection, dump

fileName = sys.argv[1]
with open(fileName) as f:
    gj = geojson.load(f)

nocache = fileName.split("data")[0]

listArray = []
for feature in gj['features']:
    listArray.append([feature["geometry"]["coordinates"][0], feature["geometry"]["coordinates"][1]])

pp = PointPattern(listArray)
sx,sy,theta = ellipse(pp.points)
theta_degree = np.degrees(theta)

fig = figure()
e = Ellipse(xy=mean_center(pp.points), width=sx*2, height=sy*2, angle=theta_degree) #angle is rotation in degrees (anti-clockwise)

#Creating Shapely Ellipse >>>
vertices = e.get_verts()     # get the vertices from the ellipse object
shapelyEllipse = Polygon(vertices)
#print(shapelyEllipse)
features = []
#print(shapely.geometry.mapping(shapelyEllipse))
featureObject = {"type": "Feature"}
feature_collection = {"type": "FeatureCollection", "features": [{"type": "Feature", "geometry": shapely.geometry.mapping(shapelyEllipse)}]}
print(feature_collection)
with open(nocache+'_standard_deviational_ellipse.geojson', 'w') as f:
   dump(feature_collection, f)
#<<< Creating Shapely Ellipse

ax = pp.plot(get_ax=True, title='Standard Deviational Ellipse')
ax.add_artist(e)
e.set_facecolor([0.8,0,0])
e.set_edgecolor([1,0,0])
plt.savefig(nocache+"_sd_ellipse.png")
print(nocache+"_standard_deviational_ellipse.geojson")