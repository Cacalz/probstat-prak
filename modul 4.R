#modul 4 
calista=read.delim("clipboard")
view(calista)
t.test(calista$volume, conf.level = 0.95)
t.test(calista$volume, conf.level = 0.50)