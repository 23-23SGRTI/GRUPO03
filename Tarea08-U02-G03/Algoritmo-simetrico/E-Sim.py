
from cryptography.fernet import Fernet
import time #importacion del tiempo
import os
from io import open
#Cargar una clave 
def cargar_clave():
    return open("clave.key","rb").read()


#Genera y guarda una clave 
def genera_clave():
    clave = Fernet.generate_key()
    with open("clave.key","wb") as archivo_clave:
            archivo_clave.write(clave)

#Generar clave
genera_clave()
#Cargar clave - generada 
clave = cargar_clave()
#imprimir clave
print (" ---------------------------------------------------------------------------------------------------------------------------------------------------")
print("CLAVE :",clave)
print (" ---------------------------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t//////////////// METODO DE CIFRADO (SIMETRICO) ///////////////////////")

print ("hola bienvenido")
ruta="C:/Users/lenin/Desktop/Algoritmos/Algoritmos/Grupo3/Algoritmo-simetrico"
print("Ingrese el documento que desea encryptar") 
archivo=input()
archivo_ruta= os.path.join(ruta,archivo)

if os.path.exists(archivo_ruta):
    # Abrir el archivo en modo lectura
    with open(archivo_ruta) as archivo:
        # Leer el contenido del archivo
        contenido = archivo.read()
        print(contenido)

#Encriptación 
start3=time.time_ns() 
def encript(nom_archivo, clave):
    f = Fernet(clave)
    with open(nom_archivo, "rb") as file:
        archivo_info = file.read()
    encrypted_data = f.encrypt(archivo_info)
    with open(nom_archivo, "wb") as file:
            file.write(encrypted_data)

#E-Archivo

encript(archivo_ruta, clave)


#imprimir documento cifrado
archivo= open (archivo_ruta)
print ("ARCHIVO ENCRIPTADO:\n",archivo.read())
print (" ---------------------------------------------------------------------------------------------------------------------------------------------------")
end3=time.time_ns()


#desencriptar el archivo
start4=time.time_ns()
def desencrypt(nom_archivo,clave):
    f = Fernet(clave)
    with open(nom_archivo, "rb")  as file:
        encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data) 
    with open(nom_archivo, "wb") as file:
        file.write(decrypted_data)

#Archivo a desencriptar 
desencrypt(archivo_ruta,clave)

#Archivo descifrado , I 
archivo= open (archivo_ruta,"rb")
print ("ARCHIVO DESCIFRADO: ",archivo.read())
print (" ---------------------------------------------------------------------------------------------------------------------------------------------------")
end4=time.time_ns()

#Tiempo
print (" ")
print("Tiempo del Cifrado del texto:",str(end3-start3))
print (" ")
print("Tiempo del Descifrado del texto:",str(end4-start4))
#1000000palabras.txt