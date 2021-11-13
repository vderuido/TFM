library(sensR)
library(numDeriv)
library(multcomp)

# Calculo para distancia respecto a distancia entre butacas en unidades unitarias
aciertos<- c(6,17,23,31,55,40,61,59,73,52,47,54,47,15,21,14,18)
total<-c(15,45,52,60,81,64,81,69,87,59,55,57,50,15,22,14,18)
Protocolos<- c("twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC")
a<-dprime_table(aciertos,total,Protocolos)

# Calculo para distancia respecto de la fuente en metros
aciertos2<- c(10,25,24,41,41,53,79,81,66,53,74,43,25,18)
total2<-c(15,35,32,54,56,67,102,100,84,63,95,62,44,41)
Protocolos2<- c("twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC")
a2<-dprime_table(aciertos2,total2,Protocolos2)

# Calculo para distancia respecto de distancia entre butacas en metros
aciertos3<- c(21,36,55,81,71,67,61,48,59,46,32,32,24)
total3<- c(61,76,102,111,95,78,70,52,62,47,33,33,24)
Protocolos3<- c("twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC")
a3<- dprime_table(aciertos3,total3,Protocolos3)

# Calculo para distancia respecto de la fuente en metros solo SIN DUDA
aciertos4<- c(8,22,17,34,36,44,69,69,56,42,59,34,15,14)
total4<-c(11,30,23,40,47,52,82,84,68,49,77,42,25,31)
Protocolos4<- c("twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC")
a4<-dprime_table(aciertos4,total4,Protocolos4)

# Calculo para distancia respecto de distancia entre butacas en metros solo SIN DUDA
aciertos5<- c(14,20,41,62,50,57,57,39,51,43,30,32,23)
total5<- c(41,49,74,79,65,62,64,40,53,44,31,32,23)
Protocolos5<- c("twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC")
a5<- dprime_table(aciertos5,total5,Protocolos5)
