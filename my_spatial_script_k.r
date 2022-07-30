library(spatstat)
library(maptools)
library(geojsonR)
library(sp)
library(rgdal)
library(geojsonio)
library(sf)
library(spatstat.geom)

args <- commandArgs(TRUE)
N <- args[1]
name <- args[2]
gj <- geojson_read(N,what='sp')
#st_crs(gj)
gj <- spTransform(gj,CRS("+init=epsg:6345"))
gj <- as.ppp.SpatialPoints(gj)
#L <- Lest(gj,correction="Ripley",nsims=100)
png(filename=paste(name,"_ripley_k_function.png"), width=500, height=500)
#OP <- par(mar=c(5,5,4,4))
#plot(L, . -r ~ r, ylab=expression(hat("L")), xlab = "d (m)")
#par(OP)
#plot(L, xlab="d (m)", ylab="L(d)")
p  <- 0.05 # Desired p significance level to display
n <- 1000
EL <- envelope(gj, Kest, nsim=n, rank=(p * (n + 1)))
OP <- par(mar=c(5,5,4,4))
 plot(EL, ylab="K",xlab="Distance (m)", main=paste("p = ",p))
par(OP)