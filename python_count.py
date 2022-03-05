import geojson
import sys

fileName = sys.argv[1]
nocache = fileName.split("data")[0]
with open(fileName) as f:
    gj = geojson.load(f)

i = 0
for feature in gj['features']:
    i = i+1

f = open((nocache+"result.txt"), "w")
f.write(str(i))
f.close()

print(i)