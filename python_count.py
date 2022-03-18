import geojson
import sys


fileName = sys.argv[1]
with open(fileName) as f:
    gj = geojson.load(f)

i = 0
for feature in gj['features']:
    i = i+1

print(i)