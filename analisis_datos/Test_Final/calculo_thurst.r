library(sensR)
library(numDeriv)
library(multcomp)

aciertos<- c(6,17,23,31,55,40,61,59,73,52,47,54,47,15,21,14,18)
total<-c(15,45,52,60,81,64,81,69,87,59,55,57,50,15,22,14,18)
Protocolos<- c("twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC")
a<-dprime_table(aciertos,total,Protocolos)

aciertos2<- c(10,25,24,41,41,53,79,81,66,53,74,43,25,18)
total2<-c(15,35,32,54,56,67,102,100,84,63,95,62,44,41)
Protocolos2<- c("twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC","twoAFC")
a2<-dprime_table(aciertos2,total2,Protocolos2)
