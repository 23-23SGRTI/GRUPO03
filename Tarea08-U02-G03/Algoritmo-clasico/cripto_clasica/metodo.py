import string
alfabeto= list(string.ascii_lowercase)  
#el string.ascii_lowercase nos ayuda a no crear un array con todo el abecedario 
#es decir de esta forma llamamos al abecedario en minuscula de la a-z 
from timeit import default_timer


def cifrado_cesar(alfabeto,n,texto):
    iniciocifrado = default_timer()
    
    texto_cifrado = ""
    
    for letra in texto:
                if letra in alfabeto: 
                    indice_actual = alfabeto.index(letra)  # permite acceder al indice de un elemento especifico 
                    indice_cesar = indice_actual + n
                    if indice_cesar > 25:
                        indice_cesar -= 25 
                    texto_cifrado += alfabeto [indice_cesar]
                else:
                    texto_cifrado += letra
    print ("Texto encriptad0:", texto_cifrado )

    fin = default_timer()
    print("tiempo de texto encriptado: ",fin-iniciocifrado)
    return texto_cifrado


def decodificar(alfabeto,n,texto):
    iniciodecifrado = default_timer()
    texto_decodificado = ""
    for letra in texto:
                if letra in alfabeto: 
                    indice_cesar = alfabeto.index(letra)  # permite acceder al indice de un elemento especifico 
                    indice_original = indice_cesar - n
                    if indice_original < 0:
                        indice_original += 25 
                    texto_decodificado += alfabeto [indice_original]
                else:
                    texto_decodificado += letra
    print ("frase decodificada:", texto_decodificado)
    fin2 = default_timer()
    print("tiempo de decifrado",fin2-iniciodecifrado)
    return texto_decodificado