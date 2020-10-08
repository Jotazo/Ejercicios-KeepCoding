from os import system
from time import sleep

def inicial():
    """
    ---Operaciones aritméticas---

    Escribe un programa que pida dos números y que devuelva su suma, resta, producto y división.

    Restricciones:

    1.Convertir las cadenas de entrada en números
    2.Separar convenientemente la entrada, transformación de cadena en números y salida separados
    3.Crea una única sentencia de salida con los saltos de línea adecuados (sólo un print)

    """
    system('cls')

    strNum1 = input("Introduce un numero:\n>")
    strNum2 = input("Introduce un numero:\n>")

    num1 = int(strNum1)
    num2 = int(strNum2)

    print(f"\n{num1} + {num2} = {num1+num2}\n{num1} - {num2} = {num1-num2}\
        \n{num1} * {num2} = {num1*num2}\n{num1} / {num2} = {num1/num2}")

def reto1():
    # 1.Controla que las entradas sean números de forma que el programa no avance si no se introduce un número
    
    while True:
        try:
            system('cls')

            strNum1 = input("Introduce un numero:\n>")
            if strNum1[1:].isdigit() != True:
                raise ValueError

            strNum2 = input("Introduce un numero:\n>")
            if strNum2[1:].isdigit() != True:
                raise ValueError

            break

        except ValueError:
            print("No ha introducido un número")
            sleep(1.5)


    num1 = int(strNum1)
    num2 = int(strNum2)

    print(f"\n{num1} + {num2} = {num1+num2}\n{num1} - {num2} = {num1-num2}\
        \n{num1} * {num2} = {num1*num2}\n{num1} / {num2} = {num1/num2}")
    
def reto2():
    # 2.No permitas introducir números negativos
    while True:
        try:
            system('cls')

            strNum1 = input("Introduce un numero:\n>")
            if strNum1.isdigit() != True:
                raise ValueError

            strNum2 = input("Introduce un numero:\n>")
            if strNum2.isdigit() != True:
                raise ValueError

            break
        
        except ValueError:
            print("No ha introducido un número o el número introducido es un número negativo")
            sleep(1.5)


    num1 = int(strNum1)
    num2 = int(strNum2)

    print(f"\n{num1} + {num2} = {num1+num2}\n{num1} - {num2} = {num1-num2}\
        \n{num1} * {num2} = {num1*num2}\n{num1} / {num2} = {num1/num2}")

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