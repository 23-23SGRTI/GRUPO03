from io import open
import time
import os
import hashlib

class HASH:
	def generaHash(h):
		digest=h.hexdigest()
		return digest

print("\t\t\t\t//////////////// METODO DE CIFRADO (HASH) ///////////////////////")

print ("hola bienvenido al cifrado de HASH")

ruta="C:/Users/lenin/Desktop/Algoritmos/Algoritmos/Tarea08-U02-G03\hash"
print("Ingrese el documento que desea encryptar") 
archivo=input()
archivo_ruta= os.path.join(ruta,archivo)

if os.path.exists(archivo_ruta):
    # Abrir el archivo en modo lectura
    with open(archivo_ruta) as archivo:
        # Leer el contenido del archivo
        contenido = archivo.read()
        print(contenido)
else:
    print("El archivo no existe en la ruta especificada.")

while True:
    opc= int (input("MENU: \n 1) texto que contiene el archivo \n 2) hash del archivo \n 3) Salir \n"))

    if opc == 1:
        print (contenido)
    elif opc == 2:
            #metodo hash
            inicio = time.time_ns()
            print("\n\t*****Se realizara el cifrado HASH:******** ")
            c = bytes(contenido, "utf-8")
            h = hashlib.new("sha256", c)
            hash1 = HASH.generaHash(h)
            print("El HASH del archivo es: ")
            print(hash1)
            fin = time.time_ns()
            tiempo=fin-inicio
            print("EL TIEMPO QUE SE DEMORO EN CIFRAR EL MENSAJE  FUE: " + str(tiempo) + " nanosegundos")

    elif opc == 3:
        print("GRACIAS Y ADIOS")
        break
    else:
        print ("Opcion invalida")
   
        
