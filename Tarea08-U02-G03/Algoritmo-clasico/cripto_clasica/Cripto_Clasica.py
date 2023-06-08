
#algoritmo de encriptacion clasica cifrado cesar 

import metodo
import string
import os
from timeit import default_timer
alfabeto= list(string.ascii_lowercase) 


# Ruta completa del archivo que deseas leer
ruta = "D:/UNIVERSIDAD CENTRAL/UCE JHON/7 SEPTIMO SEMESTRE/1 SEGURIDAD Y GESTION/2 DEBERES GRUP/criptografias/Tarea09-U02-G05/Algoritmo-clasico/cripto_clasica"

#nombre del archivo que desea encriptar
print ("ingrese el nombre del archivo que desea encriptar")
archivo=input()
# variable que contiene los dos campos
ruta_archivo = os.path.join(ruta, archivo)
# Verificar que el archivo exista en la ruta especificada
if os.path.exists(ruta_archivo):
    # Abrir el archivo en modo lectura
    with open(ruta_archivo) as archivo:
        # Leer el contenido del archivo
        contenido = archivo.read()
        print(contenido)
else:
    print("El archivo no existe en la ruta especificada.")

while True:
    opc= int (input("MENU: \n 1) texto que contiene el archivo \n 2) Encriptacion del archivo \n 3) Desencriptacion del archivo \n 4) Salir \n"))

    if opc == 1:
        print (contenido)
    elif opc == 2:
        #metodo.cifrado_cesar(alfabeto,3,leer)
        frase_cifrada= metodo.cifrado_cesar(alfabeto,3,contenido)
    elif opc == 3:
        metodo.decodificar(alfabeto,3,frase_cifrada)
    elif opc == 4:
        print("GRACIAS Y ADIOS")
    else:
        print ("Opcion invalida")
     








