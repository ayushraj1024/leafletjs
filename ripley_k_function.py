import numpy as np
from matplotlib import pyplot as plt
from astropy.stats import RipleysKEstimator
import geojson
import sys

fileName = sys.argv[1]
with open(fileName) as f:
    gj = geojson.load(f)

listArray = []
for feature in gj['features']:
    listArray.append([feature["properties"]["latitude"], feature["properties"]["longitude"]])
z = np.array(listArray)

#z = np.random.uniform(low=5, high=10, size=(100, 2))
Kest = RipleysKEstimator(area=25, x_max=10, y_max=10, x_min=5, y_min=5)

print(z)

r = np.linspace(0, 2.5, 100)
plt.plot(r, Kest.poisson(r), color='green', ls=':', label=r'$K_{pois}$')
plt.plot(r, Kest(data=z, radii=r, mode='none'), color='red', ls='--',
         label=r'$K_{un}$')
plt.plot(r, Kest(data=z, radii=r, mode='translation'), color='black',
         label=r'$K_{trans}$')
plt.plot(r, Kest(data=z, radii=r, mode='ohser'), color='blue', ls='-.',
         label=r'$K_{ohser}$')
plt.plot(r, Kest(data=z, radii=r, mode='var-width'), color='green',
         label=r'$K_{var-width}$')
plt.plot(r, Kest(data=z, radii=r, mode='ripley'), color='yellow',
         label=r'$K_{ripley}$')
plt.legend()
plt.savefig('k_function.png')