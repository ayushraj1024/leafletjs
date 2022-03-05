library(spatstat)
library(maptools)
library(geojsonR)

args <- commandArgs(TRUE)
N <- args[1]
char_js = FROM_GeoJson(url_file_string = N)
sp <- as(char_js, "Spatial")
sp <- as(sp, "ppp")

e <- envelope(sp, Kest, nsim = 100)
png(filename="temp.png", width=500, height=500)
plot(e, main = 'K Function')