from os import system
from time import sleep

def inicial():
    """
    ---Contando caracteres---

    El programa pedirá una cadena de caracteres y devolverá el número de caracteres.

    Restricciones:

    1.Asegurate de que devuelve la cadena original
    2.Utiliza la función específica de python para resolverlo
    
    """
    system('cls')

    cadena = input("Introduzca una cadena, por favor.\n>")

    print("Procesando cadena...")
    sleep(2.0)
    numCaracteres = len(cadena)
    system('cls')

    print(f"La cadena:\n'{cadena}'\nTiene: {numCaracteres} caracteres.")

def reto1():
    # 1. Si el usuario no introduce nada, el programa le conminará a que escriba algo.

    system('cls')
    cadena = ""

    while len(cadena) < 1:
        cadena = input("Introduzca una cadena, por favor.\n>")

    print("Procesando cadena...")
    sleep(2.0)
    numCaracteres = len(cadena)
    system('cls')

    print(f"La cadena:\n'{cadena}'\nTiene: {numCaracteres} caracteres.")

def reto2():
    #2. Hazlo sin utilizar la función específica de python

    system('cls')

    cadena = input("Introduzca una cadena, por favor.\n>")
    
    print("Procesando cadena...")
    sleep(2.0)

    numCaracteres = 0
    for i in cadena:
        numCaracteres += 1
    

    system('cls')

    print(f"La cadena:\n'{cadena}'\nTiene: {numCaracteres} caracteres.")

def main():
    while True:

        system('cls')
        opcion = input("Elige una opción:\n1 - Programa normal\n2 - Reto 1\n3 - Reto 2\n>")

        if opcion == "1":
            print("Ha elegido Programa normal")
            sleep(1.0)
            system('cls')
            inicial()
            break
        elif opcion == "2":
            print("Ha elegido Reto 1")
            sleep(1.0)
            system('cls')
            reto1()
            break
        elif opcion == "3":
            print("Ha elegido Reto 2")
            sleep(1.0)
            system('cls')
            reto2()
            break
        else:
            print("No ha escogido opción correcta")
            sleep(1.0)
            system('cls')

main()