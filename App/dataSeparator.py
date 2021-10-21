import numpy as np
import pandas as pd
import matplotlib.pyplot
import os
import math

# Función que devuelve una lista con los archivos dentro de un directorio
def listaArchivos(ruta):
    archivos = os.listdir(ruta)
    return archivos

rutaCSV="/home/vic/Documents/universidad/PFM/analisis_datos/Test_Final/resultadosTest.csv"
rutaResultados="/home/vic/Documents/universidad/PFM/analisis_datos/Test_Final/analisisTest2.csv"

df=pd.read_csv(rutaCSV)

resultados=pd.DataFrame(
    {
        'archivo1': np.array([None]*len(df)),
        'archivo2': np.array([None]*len(df)),
        'respuesta': np.array([None]*len(df)),
        'seguridad': np.array([None]*len(df)),
        'distancia Fila': np.array([None]*len(df)),
        'distancia Butaca':np.array([None]*len(df)),
        'distancia': np.array([None]*len(df)),
    }

)

#Recorrer todo el documento
for i in range(0,len(df)):
    string1=df.iloc[i,0]
    string2=df.iloc[i,1]


    fila1=string1[0]
    fila2=string2[0]
    numerofila1=0
    numerofila2=0
    numerobutaca1=0
    numerobutaca2=0
    distanciaFila=0
    distanciaButaca=0
    distancia=0
    distanciaFilaX=0
    distanciaFilaY=0
    distanciaFila=0

    #Extraer fila y butaca del primer archivo. En primer lugar, analiza si la fila es A o F
    #Después, analiza si la fila es mayor que 10 viendo si la empieza el código de butaca B
    #Tras guardar la fila, analiza la longitud de la butaca para saber cuántos str tiene que tomar
    #Finalmente aplica corrección según sea fila A o F (desplazar 3)

    if fila1=="F":
        if string1[2]!="B":
            numerofila1=int(string1[1]+string1[2])
            if string1[5]=="_" or string1[5]=="." or string1[4]=="B":
                numerobutaca1=int(string1[4])
            else:
                numerobutaca1=int(string1[4]+string1[5])


        else:
            numerofila1=int(string1[1])
            if string1[4]=="_" or string1[4]=="." or string1[4]=="B":
                numerobutaca1=int(string1[3])
            else:
                numerobutaca1=int(string1[3]+string1[4])

        numerofila1=numerofila1+3


    else:
        numerofila1=int(string1[1])
        if string1[4]=="_" or string1[4]=="." or string1[4]=="B":
                numerobutaca1=int(string1[3])
        else:
                numerobutaca1=int(string1[3]+string1[4])


    #Extraer fila y butaca del segundo archivo. En primer lugar, analiza si la fila es A o F
    #Después, analiza si la fila es mayor que 10 viendo si la empieza el código de butaca B
    #Tras guardar la fila, analiza la longitud de la butaca para saber cuántos str tiene que tomar
    #Finalmente aplica corrección según sea fila A o F (desplazar 3)
    if fila2=="F":
        if string2[2]!="B":
            numerofila2=int(string2[1]+string2[2])
            if string2[5]=="_" or string2[5]=="." or string2[4]=="B":
                numerobutaca2=int(string2[4])
            else:
                numerobutaca2=int(string2[4]+string2[5])
        else:
            numerofila2=int(string2[1])
            if string2[4]=="_" or string2[4]=="." or string2[4]=="B":
                numerobutaca2=int(string2[3])
            else:
                numerobutaca2=int(string2[3]+string2[4])

        numerofila2=numerofila2+3

    else:
        numerofila2=int(string2[1])
        if string2[4]=="_" or string2[4]=="." or string2[4]=="B":
                numerobutaca2=int(string2[3])
        else:
                numerobutaca2=int(string2[3]+string2[4])

    #Hacer cálculos de distancia
    if numerobutaca1%2!=0:
        numerobutaca1=numerobutaca1+1
    if numerobutaca2%2!=0:
        numerobutaca2=numerobutaca2+1

    distanciaFila=abs(numerofila1-numerofila2)
    distanciaButaca=(abs(numerobutaca1-numerobutaca2))/2
    distancia=math.sqrt(distanciaFila*distanciaFila + distanciaButaca*distanciaButaca)

    #Calculo de distancia respecto de la fuente
    distanciaFuenteX=min(numerobutaca1,numerobutaca2)+distanciaButaca
    distanciaFuenteY=min(numerofila1,numerofila2)+distanciaFila
    distanciaFuente=math.sqrt(distanciaFuenteX*distanciaFuenteX+distanciaFuenteY*distanciaFuenteY)

    #Almacenar datos en resultados
    resultados.iloc[i,0]=df.iloc[i,0]
    resultados.iloc[i,1]=df.iloc[i,1]
    resultados.iloc[i,2]=df.iloc[i,2]
    resultados.iloc[i,3]=df.iloc[i,3]
    resultados.iloc[i,4]=distanciaFila
    resultados.iloc[i,5]=distanciaButaca
    resultados.iloc[i,6]=distancia
    resultados.iloc[i,7]=distanciaFuente

#Imprimir y guardar en csv
print(resultados)
resultados.to_csv(rutaResultados, index=False)
