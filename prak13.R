#lat 1
Dataku_calista = read.delim("clipboard")
wilcox.test(Dataku_calista$X, Dataku_calista$X.1, paired = TRUE)
#2
calista = read.delim("clipboard")
wilcox.test(calista$Sebelum, calista$Sesudah, paired = TRUE)
#lat 2
df_calista = read.delim("clipboard")
wilcox.test(df_calista$obat~df_calista$grup)
#lat 3
calista3 = read.delim("clipboard")
ganjil <- c(64, 62, 45, 66, 70, 62, 80, 54, 65)
genap <- c(54, 77, 50, 54, 89, 56, 72, 65, 76)
wilcox.test(ganjil, genap, paired = TRUE)
#2
calista4 = read.delim("clipboard")
caffein_e <- c(95, 99, 94, 89, 96, 93, 88, 105, 88)
placeb_o <- c(105, 119, 100, 97, 96, 101, 94, 95, 98)
wilcox.test(caffein_e, placeb_o, paired = FALSE)