from time import sleep
from os import system

def inicial():
    """
    Tabla de multiplicar
    Crear un programa que escriba la tabla de multiplicar del número introducido por el usuario, así

    Introduzca valor: 5
    
    5 x 1 = 5
    5 x 2 = 10
    5 x 3 = 15
    5 x 4 = 20
    5 x 5 = 25
    5 x 6 = 30
    5 x 7 = 35
    5 x 8 = 40
    5 x 9 = 45
    5 x 10 = 50
    Restricciones
    El programa debe impedir la entrada de cualquier número que no sea entero y positivo y volverá a pedirlo
    """
    while True:
        try:
            strNumero = input("Introduzca un numero entero y positivo: ")
            if strNumero[0] == '-' or strNumero[0] == '.':
                raise ValueError
            numero = int(strNumero)
            break
        except ValueError:
            print("No ha introducido un numero entero positivo.")

    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")
def reto1():
    # 1.Formatear la tabla para que los valores salgan en columnas y ajustados a la derecha.

    while True:
        try:
            strNumero = input("Introduzca un numero entero y positivo: ")
            if strNumero[0] == '-' or strNumero[0] == '.':
                raise ValueError
            numero = int(strNumero)
            break
        except ValueError:
            print("No ha introducido un numero entero positivo.")

    for i in range(1,11):
        print(f"{numero: >2} x {i: >2} = {(numero*i): >3}")

def reto2():
    # 2.Seguir pidiendo valores hasta que el usuario introduzca un 0 (cero) entonces parar
    while True:
        try:
            strNumero = input("Introduzca un numero entero y positivo: ")
            if strNumero[0] == '-' or strNumero[0] == '.':
                raise ValueError

            numero = int(strNumero)

            if numero == 0:
                break

            for i in range(1,11):
                print(f"{numero: >2} x {i: >2} = {(numero*i): >3}")

        except ValueError:
            print("No ha introducido un numero entero positivo.")

    
def reto3():
    # 3.Plantear solución con while y con for
    # Solo while, puesto que for ya lo he hecho
    while True:
        try:
            strNumero = input("Introduzca un numero entero y positivo: ")
            if strNumero[0] == '-' or strNumero[0] == '.':
                raise ValueError

            numero = int(strNumero)

            if numero == 0:
                break
            
            i = 1

            while i <= 10:
                print(f"{numero: >2} x {i: >2} = {(numero*i): >3}")
                i += 1

        except ValueError:
            print("No ha introducido un numero entero positivo.")

def main():
    while True:

        system('cls')
        opcion = input("Elige una opción:\n1 - Programa normal\n2 - Reto 1\n3 - Reto 2\n4 - Reto 3\n>")

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
        elif opcion == "4":
            print("Ha elegido Reto 3")
            sleep(1.0)
            system('cls')
            reto3()
            break
        else:
            print("No ha escogido opción correcta")
            sleep(1.0)
            system('cls')
main()