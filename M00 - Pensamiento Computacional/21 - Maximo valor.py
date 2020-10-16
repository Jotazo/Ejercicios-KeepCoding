from time import sleep
from os import system

def inicial():
    """
    --- Máximo valor ---
    Introduce 3 números y muestra el mayor

    Restricciones:
    1.Impedir continuar si no son números
    2.Impedir continuar si no son todos distintos
    3.Hacerlo a mano, sin utilizar funciones del lenguaje que te permitan encontrar el mayor.
    """
    while True:
        try:    
            num1 = int(input("Introduzca el primer numero: "))
            num2 = int(input("Introduzca el segundo numero: "))
            num3 = int(input("Introduzca el tercer numero: "))
            if num1 == num2 or num2 == num3:
                raise EOFError
            break
        except EOFError:
            print("Los numeros han de ser diferentes.")
        except:
            print("No ha introducido un valor correcto.")

    mayor = 0
    if num1 > num2 and num1 > num3:
        mayor = num1
    elif num2 > num1 and num2 > num3:
        mayor = num2
    else:
        mayor = num3

    print(f"De los 3 valores introducidos: {num1} - {num2} - {num3} el mayor es: {mayor}")
    
def reto1():
    # 1.Intentar hacerlo de manera más eficiente con funciones y estructuras de datos
    lista_numeros = []

    for i in range(3):
        while True:
            try:
                num = float(input(f"Introduzca el número {i+1}: "))
                break
            except ValueError:
                print("No ha introducido un valor válido.")
        lista_numeros.append(num)

    mayor = max(lista_numeros)

    print(f"Numeros: {lista_numeros[0]} - {lista_numeros[1]} - {lista_numeros[2]}\
        \nValor más alto: {mayor}")

def reto2():
    # 2.Modificar el programa para hacerlo con 10 números
    lista_numeros = []

    for i in range(10):
        while True:
            try:
                num = float(input(f"Introduzca el número {i+1}: "))
                break
            except ValueError:
                print("No ha introducido un valor válido.")
        lista_numeros.append(num)

    mayor = max(lista_numeros)

    print("Numeros: ")

    for i in range(len(lista_numeros)):
        print(f"{lista_numeros[i]}")

    print(f"Valor mas alto: {mayor}")

def reto3():
    # 3.Modificar el programa para hacerlo con tantos números como el usuario quiera

    lista_numeros = []
    cantidad = int(input("Introduzca la cantidad de numeros a introducir: "))
    for i in range(cantidad):
        while True:
            try:
                num = float(input(f"Introduzca el número {i+1}: "))
                break
            except ValueError:
                print("No ha introducido un valor válido.")
        lista_numeros.append(num)

    mayor = max(lista_numeros)

    print("Numeros: ")

    for i in range(len(lista_numeros)):
        print(f"{lista_numeros[i]}")

    print(f"Valor mas alto: {mayor}")

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

