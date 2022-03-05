import geojson
with open('school_points.geojson') as f:
    gj = geojson.load(f)

i = 0
for feature in gj['features']:
    i = i+1

print(i)

