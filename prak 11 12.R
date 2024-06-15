#prak 11
df_calista = read.delim("clipboard")
head(df_calista)
model <- aov(korosi ~ metode, data = df_calista)
summary(model)
tukey.test <- TukeyHSD(model)
tukey.test
#elkom 2
df_calistaaz = PlantGrowth
View(df_calistaaz)
model <- aov(weight ~ group, data = df_calistaaz)
summary(model)
tukey.test <- TukeyHSD(model)
tukey.test

#prak 12
df_calistaa = read.delim("clipboard")
head(df_calistaa)
model_reg = lm(df_calistaa$Y~df_calistaa$X)
summary(model_reg)

#elkom 2
calista <- read.csv("C:/probstat/houseprice.csv")
calista$Brick_dummy <- ifelse(calista$Brick == "Yes", 1,0)
calista$N_dummy1 <- ifelse(calista$Neighborhood == "West", 1,0)
calista$N_dummy2 <- ifelse(calista$Neighborhood == "North", 1,0)
model = lm(calista$Price~calista$SqFt+calista$Bedrooms+calista$Bathrooms+calista$Brick_dummy+calista$N_dummy1+calista$N_dummy2)
summary(model)
