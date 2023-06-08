import time
import os

def encrypt_text(plaintext, key):
    # Calcula el número de columnas necesarias según la longitud de la clave
    num_columns = len(key)
    # Calcula el número de filas necesarias para contener todo el texto
    num_rows = (len(plaintext) + num_columns - 1) // num_columns

    # Rellena el texto plano con caracteres de relleno si es necesario
    padded_plaintext = plaintext.ljust(num_rows * num_columns)

    # Crea una lista de columnas vacías
    columns = [''] * num_columns

    # Distribuye los caracteres del texto plano en las columnas
    for i, char in enumerate(padded_plaintext):
        column_index = i % num_columns
        columns[column_index] += char

    # Ordena las columnas según la clave
    sorted_columns = [col for _, col in sorted(zip(key, columns))]

    # Concatena las columnas en el texto cifrado
    ciphertext = ''.join(sorted_columns)
    return ciphertext


def decrypt_text(ciphertext, key):
    # Calcula el número de columnas necesarias según la longitud de la clave
    num_columns = len(key)
    # Calcula el número de filas necesarias para contener todo el texto
    num_rows = (len(ciphertext) + num_columns - 1) // num_columns

    # Crea una lista de columnas vacías
    columns = [''] * num_columns

    # Distribuye los caracteres del texto cifrado en las columnas en el orden original
    index = 0
    for i in range(num_columns):
        num_chars = num_rows if i < len(ciphertext) % num_columns else num_rows - 1
        columns[i] = ciphertext[index:index+num_chars]
        index += num_chars

    # Crea una lista para almacenar las columnas en el orden correcto
    ordered_columns = [''] * num_columns

    # Reordena las columnas según la clave original
    for i, col in enumerate(columns):
        col_index = key.index(str(i+1))
        ordered_columns[col_index] = col

    # Concatena las columnas en el texto claro
    plaintext = ''.join(''.join(row) for row in zip(*ordered_columns))
    return plaintext


def generate_key(num_columns):
    # Genera una clave de cifrado basada en el número de columnas
    return ''.join(str(i+1) for i in range(num_columns))


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print('El archivo no existe en la ruta especificada.')


def main():
    while True:
        print("\nMENU:")
        print("1) Leer un archivo .txt a cifrar")
        print("2) Generar e imprimir la(s) claves de cifrado")
        print("3) Cifrar e imprimir el texto cifrado")
        print("4) Descifrar e imprimir el texto claro")
        print("5) Realizar todos los procesos anteriores y mostrar en pantalla")
        print("6) Salir")

        option = input("Ingrese el número de la opción deseada: ")

        if option == '1':
          
            print("Ingrese el documento que desea encriptar:")
            archivo = input()
            ruta = os.path.join("C:\\UCE\\Seguridad\\Seguridad\\Algoritmos\\Grupo3\\Transposicion", archivo)
            start_time = time.time_ns()
            plaintext= read_file(ruta)
            end_time = time.time_ns()
            elapsed_time = end_time - start_time
                            
            if plaintext:
                print("Texto plano leído del archivo:")
                print(plaintext)
                print(f"Tiempo transcurrido: {elapsed_time} nanosegundos")

        elif option == '2':
            num_columns = int(input("Ingrese el número de columnas para la clave de cifrado: "))
            start_time = time.time_ns()
            key = generate_key(num_columns)
            end_time = time.time_ns()
            elapsed_time = end_time - start_time

            print("Clave de cifrado generada:")
            print(key)
            print(f"Tiempo transcurrido: {elapsed_time} nanosegundos")

        elif option == '3':
            if 'plaintext' not in locals():
                print("Primero debe leer un archivo .txt a cifrar.")
                continue

            start_time = time.time_ns()
            ciphertext = encrypt_text(plaintext, key)
            end_time = time.time_ns()
            elapsed_time = end_time - start_time

            print("Texto cifrado:")
            print(ciphertext)
            print(f"Tiempo transcurrido: {elapsed_time} nanosegundos")

        elif option == '4':
            if 'ciphertext' not in locals():
                print("Primero debe cifrar un texto.")
                continue

            start_time = time.time_ns()
            decrypted_text = decrypt_text(ciphertext, key)
            end_time = time.time_ns()
            elapsed_time = end_time - start_time

            print("Texto descifrado:")
            print(decrypted_text)
            print(f"Tiempo transcurrido: {elapsed_time} nanosegundos")


        elif option == '5':
            print("Ingrese el documento que desea encriptar:")
            archivo = input()
            ruta = os.path.join("C:\\UCE\\Seguridad\\Seguridad\\Algoritmos\\Grupo3\\Transposicion", archivo)
            start_time = time.time_ns()
            plaintext= read_file(ruta)
            end_time = time.time_ns()
            elapsed_time = end_time - start_time

            num_columns = int(input("Ingrese el número de columnas para la clave de cifrado: "))

            start_time = time.time_ns()
            key = generate_key(num_columns)
            end_time = time.time_ns()
            key_time = end_time - start_time

            start_time = time.time_ns()
            ciphertext = encrypt_text(plaintext, key)
            end_time = time.time_ns()
            encrypt_time = end_time - start_time

            start_time = time.time_ns()
            decrypted_text = decrypt_text(ciphertext, key)
            end_time = time.time_ns()
            decrypt_time = end_time - start_time

            print("\nRESULTADOS:")
            
            print("Texto plano leído del archivo:")
            print(plaintext)
            print(f"Tiempo transcurrido: {elapsed_time} nanosegundos")
            print("Clave de cifrado generada:")
            print(key)
            print("Texto cifrado:")
            print(ciphertext)
            print(f"Tiempo transcurrido en generación de clave: {key_time} nanosegundos")
            print(f"Tiempo transcurrido en cifrado: {encrypt_time} nanosegundos")
            print("Texto descifrado:")
            print(decrypted_text)
            print(f"Tiempo transcurrido en descifrado: {decrypt_time} nanosegundos")

        elif option == '6':
            print("GRACIAS Y ADIÓS")
            break

        else:
            print("Opción inválida. Por favor, ingrese un número válido.")


if __name__ == '__main__':
    main()
