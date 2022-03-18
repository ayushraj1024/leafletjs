import fiona
from shapely.geometry import Point, Polygon, mapping
import matplotlib.pyplot as plt
from descartes import PolygonPatch
from scipy.spatial import Voronoi, voronoi_plot_2d
from shapely.ops import voronoi_diagram
from shapely.geometry import MultiPoint
import sys
import pprint
import geojson
import shapely.wkt
import shapely.geometry
import json
from geojson import FeatureCollection, dump

fileName = sys.argv[1]
nocache = fileName.split("data")[0]

pointGeoJSON = fiona.open(fileName)
pointList = []
pointProperties = []
rawPoints = []
for point in pointGeoJSON:
    rawPoint = [point['geometry']['coordinates'][0],point['geometry']['coordinates'][1]]
    rawPoints.append(rawPoint)
    pointGeom = Point(point['geometry']['coordinates'][0],point['geometry']['coordinates'][1])
    pointList.append(pointGeom)
    pointProperties.append(point['properties'])

regions = voronoi_diagram(MultiPoint(pointList))
features = []
for geometry in shapely.geometry.mapping(regions)["geometries"]:
    featureObject = {"type": "Feature"}
    featureObject["geometry"] = geometry
    features.append(featureObject)

feature_collection = FeatureCollection(features)

with open(nocache+'voronoi.geojson', 'w') as f:
   dump(feature_collection, f)
