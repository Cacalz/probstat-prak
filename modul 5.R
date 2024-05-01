#modul 5
calista=read.delim("clipboard")
View(calista)
str(calista)
calista$volume <- as.numeric(gsub(",", ".", calista$volume))
mean(calista$volume, na.rm = TRUE)
t.test(calista$volume, mu=10)

calista=read.delim("clipboard")
View(calista)
str(calista)
volume <- c(15000, 15500, 17500, 14500, 14000,  16000, 14500, 15500, 16500, 14000)
class(volume)
sum(is.na(volume))
mean_volume <- mean(volume)
mean_volume