import pyaudio
import wave
import numpy as np
import pandas as pd
import matplotlib.pyplot
import os
import random
from playsound import playsound

## DEFINICIÓN DE FUNCIONES

# Función que devuelve una lista con los archivos dentro de un directorio
def listaArchivos(ruta):
    archivos = os.listdir(ruta)
    return archivos

# Función que reproduce un archivo aleatorio dentro de los existentes dentro de un directorio que se le pasa como parámetro
def seleccionArchivos(ruta, archivos, indice):
    print('Estamos reproduciendo: '+archivos[indice])
    #sonido=wave.open(ruta+'/'+archivos[indice])
    #reproducir(sonido)
    playsound(ruta+'/'+archivos[indice])



#EL CÓDIGO EMPIEZA AQUÍ

#CHUNK=1024
#miruta='/home/vic/Documents/universidad/PFM/IRs/IR_CITSEM/Doorslam/'
#miruta='/home/vic/Documents/universidad/PFM/IRs/IR_test/'
miruta='/home/vic/Documents/universidad/PFM/Audios/tutorial'
#miruta='/home/vic/Documents/universidad/PFM/IRs/Auditorio_Normalizado'
misArchivos=listaArchivos(miruta)
print(misArchivos)
respuestas=[None]*4
opcion=0
rutacsv='/home/vic/Documents/universidad/PFM/Resultados/respuestasTest.csv'
df=pd.DataFrame(
    {
        'archivo1': np.array(respuestas),
        'archivo2': np.array(respuestas),
        'respuesta': np.array(respuestas),
    }

)


for i in range(4):
    miIndice1=random.randint(0,len(misArchivos)-1)
    miIndice2=random.randint(0,len(misArchivos)-1)
    df.iloc[i,0]=misArchivos[miIndice1]
    df.iloc[i,1]=misArchivos[miIndice2]
    while opcion!='3':
        opcion=input("Qué audio quieres escuchar? (1 o 2, escriba 3 para salir)")
        if opcion=='1':
            seleccionArchivos(miruta,misArchivos,miIndice1)
        elif opcion=='2':
            seleccionArchivos(miruta,misArchivos,miIndice2)
    df.iloc[i,2]=input("¿Los audios son iguales?...")
    opcion=0
if os.path.exists(rutacsv):
    print("El archivo ya existe, los resultados se añadirán al final del fichero.")
    df.to_csv(rutacsv, index=False, header=False, mode='a')
else:
    print("El archivo no existe, se creará uno nuevo.")
    df.to_csv(rutacsv, index=False)

print(df)
