import fiona
from shapely.geometry import Point, Polygon, mapping
import matplotlib.pyplot as plt
from descartes import PolygonPatch
from scipy.spatial import Voronoi, voronoi_plot_2d
from shapely.ops import voronoi_diagram
from shapely.geometry import MultiPoint, MultiPolygon, MultiLineString
import sys
import pprint
import geojson
import shapely.wkt
import shapely.geometry
import json
from geojson import FeatureCollection, dump
from shapely.geometry import mapping, shape, GeometryCollection
from fiona import collection
import requests

fileName = sys.argv[1]
nocache = fileName.split("data")[0]
fileName2 = nocache+"_1data.geojson"

geoJSON1 = fiona.open(fileName)
geoJSON2 = fiona.open(fileName2)

shapeList1 = []
properties1 = []
shapeList2 = []
properties2 = []

for shapeUnit in geoJSON1:
    shapeList1.append(shape(shapeUnit["geometry"]))
    properties1.append(shapeUnit["properties"])

for shapeUnit in geoJSON2:
    shapeList2.append(shape(shapeUnit["geometry"]))
    properties2.append(shapeUnit["properties"])

geom1 = GeometryCollection(shapeList1)
geom2 = GeometryCollection(shapeList2)

print(shapely.geometry.mapping(geom1))
print('-------------------------------------------------')
print(shapely.geometry.mapping(geom2))

'''regions = voronoi_diagram(MultiPoint(pointList))
features = []
for geometry in shapely.geometry.mapping(regions)["geometries"]:
    featureObject = {"type": "Feature"}
    featureObject["geometry"] = geometry
    features.append(featureObject)

feature_collection = FeatureCollection(features)

with open(nocache+'voronoi.geojson', 'w') as f:
   dump(feature_collection, f)'''

'''geom3 = geom1.difference(geom2)
features = []
featureObject = {'type':"Feature"}
featureObject["geometry"] = shapely.geometry.mapping(geom3)
features.append(featureObject)
feature_collection = FeatureCollection(features)
print(feature_collection)

with open(fileName) as f:
    gj = geojson.load(f)

xml = """<?xml version="1.0" encoding="UTF-8"?><wps:Execute version="1.0.0" service="WPS" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.opengis.net/wps/1.0.0" xmlns:wfs="http://www.opengis.net/wfs" xmlns:wps="http://www.opengis.net/wps/1.0.0" xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:wcs="http://www.opengis.net/wcs/1.1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xsi:schemaLocation="http://www.opengis.net/wps/1.0.0 http://schemas.opengis.net/wps/1.0.0/wpsAll.xsd"><ows:Identifier>vec:IntersectionFeatureCollection</ows:Identifier><wps:DataInputs><wps:Input><ows:Identifier>first feature collection</ows:Identifier><wps:Data><wps:ComplexData mimeType="application/json"><![CDATA[""" + json.dumps(gj) + """]]></wps:ComplexData></wps:Data></wps:Input><wps:Input><ows:Identifier>second feature collection</ows:Identifier><wps:Data><wps:ComplexData mimeType="application/json"><![CDATA[""" + json.dumps(feature_collection) + """]]></wps:ComplexData></wps:Data></wps:Input><wps:Input><ows:Identifier>intersectionMode</ows:Identifier><wps:Data><wps:LiteralData>FIRST</wps:LiteralData></wps:Data></wps:Input></wps:DataInputs><wps:ResponseForm><wps:RawDataOutput mimeType="application/json"><ows:Identifier>result</ows:Identifier></wps:RawDataOutput></wps:ResponseForm></wps:Execute>"""

headers = {'Content-Type': 'application/xml'} # set what your server accepts
print(requests.post('http://geoserver.cloudgis.in:8080/geoserver/wps', data=xml, headers=headers).text)'''
