from time import sleep
from os import system

def inicial():
    """
    Conversor de temperatura
    Crear un programa que convierta temperatura de Fahrenheita a Celsius y viceversa. 
    El programa pedirá que tipo de conversión queremos y la mostrará.

    Las fórmulas de conversión son:

    C = (F − 32) * 5/9

    F = (C * 9/5) + 32

    Restricciones
    Se puede elegir el tipo de conversión en mayúsculas o minúsculas
    Reducir el número de sentencias al mínimo y no repetir prints
    """

    strTemperatura = input("Introduzca la temperatura a convertir: ")
    strTipo = input("Introduzca 'C' para convertir de Fahrenheit a Celsius y 'F' para convertir de Celsius a Fahrenheit: ")

    temperatura = float(strTemperatura)

    mensaje = ""

    if strTipo.upper() == 'F':
        fahrenheit = (temperatura * 9/5) + 32
        mensaje = f"{temperatura:.2f}ºC = {fahrenheit:.2f}ºF"
    elif strTipo.upper() == 'C':
        celsius = (temperatura - 32) * 5/9
        mensaje = f"{temperatura:.2f}ºF = {celsius:.2f}ºC"
    else:
        print("No ha escogido opción correcta")

    print(mensaje)

def reto1():
    # 1.Asegurar que las entradas son numéricas
    while True:
        strTemperatura = input("Introduzca la temperatura a convertir: ")
        try:
            if strTemperatura[0] == '.':
                raise ValueError
            temperatura = float(strTemperatura)
            break
        except:
            print("No ha escogido opción correcta")    

    strTipo = input("Introduzca 'C' para convertir de Fahrenheit a Celsius y 'F' para convertir de Celsius a Fahrenheit: ")

    mensaje = ""

    if strTipo.upper() == 'F':
        fahrenheit = (temperatura * 9/5) + 32
        mensaje = f"{temperatura:.2f}ºC = {fahrenheit:.2f}ºF"
    elif strTipo.upper() == 'C':
        celsius = (temperatura - 32) * 5/9
        mensaje = f"{temperatura:.2f}ºF = {celsius:.2f}ºC"
    
    print(mensaje)
    
def reto2():
    # 2.Modificar el programa para que acepte grados Kelvin
    while True:
        strTemperatura = input("Introduzca la temperatura a convertir: ")
        try:
            if strTemperatura[0] == '.':
                raise ValueError
            temperatura = float(strTemperatura)
            break
        except:
            print("No ha escogido opción correcta")    

    strTipo = input("Introduzca 'C' para convertir de Fahrenheit a Celsius, 'F' para convertir de Celsius a Fahrenheit y\
     \n'K' para convertir de Celsius a Kelvin: ")

    mensaje = ""

    if strTipo.upper() == 'F':
        fahrenheit = (temperatura * 9/5) + 32
        mensaje = f"{temperatura:.2f}ºC = {fahrenheit:.2f}ºF"
    elif strTipo.upper() == 'C':
        celsius = (temperatura - 32) * 5/9
        mensaje = f"{temperatura:.2f}ºF = {celsius:.2f}ºC"
    elif strTipo.upper() == 'K':
        kelvin = temperatura + 273.15
        mensaje = f"{temperatura:.2f}ºC = {kelvin:.2f}K"
    print(mensaje)

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
