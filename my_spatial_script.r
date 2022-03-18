library(spatstat)
library(maptools)
library(geojsonR)
library(sp)
library(rgdal)

args <- commandArgs(TRUE)
N <- args[1]
print(N)
gj <- readOGR(dsn=N, layer="OGRGeoJSON")
e <- envelope(gj, Kest, nsim = 100)
png(filename="temp.png", width=500, height=500)
plot(e, main = 'K Function')