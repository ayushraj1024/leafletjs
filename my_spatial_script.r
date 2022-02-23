library(spatstat)
library(maptools)

args <- commandArgs(TRUE)
N <- args[1]

sp <- as(N, "Spatial")
sp <- as(sp, "ppp")

e <- envelope(sp, Kest, nsim = 100)
png(filename="temp.png", width=500, height=500)
plot(e, main = 'K Function')