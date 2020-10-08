import time
import os

def inicial():
    """
    ---Hola, mundo---

    Hacer un programa que pida el nombre y te salude por tu nombre

    Restricciones:

    1.Mantener entrada, salida y concatenación separados
    
    """

    nombre = input("¿Como te llamas?\n>")

    mensaje = "Hola, " + nombre

    print(mensaje)

def reto1():
    # 1. Escribir el programa sin usar variables
    print("Hola,", input("¿Como te llamas?\n>"))

def reto2():
    # 2. Escribir un programa que devuelva diferentes tipos de saludos a diferentes tipos de persona.
    nombres = {'Javier':'Hola Javier!', 'Juana':'Saludos Juana!', 'Maria':'¿Que tal María?'}

    nombre = input("¿Como te llamas?\n>")

    if nombre.capitalize() in nombres:
        print(nombres[nombre.capitalize()])
    else:
        print(f"Buenas tardes, {nombre}")

def main():
    while True:

        os.system('cls')
        opcion = input("Elige una opción:\n1 - Programa normal\n2 - Reto 1\n3 - Reto 2\n>")

        if opcion == "1":
            print("Ha elegido Programa normal")
            time.sleep(1.0)
            os.system('cls')
            inicial()
            break
        elif opcion == "2":
            print("Ha elegido Reto 1")
            time.sleep(1.0)
            os.system('cls')
            reto1()
            break
        elif opcion == "3":
            print("Ha elegido Reto 2")
            time.sleep(1.0)
            os.system('cls')
            reto2()
            break
        else:
            print("No ha escogido opción correcta")
            time.sleep(1.0)
            os.system('cls')

main()

