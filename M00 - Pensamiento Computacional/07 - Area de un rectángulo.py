from time import sleep
from os import system

def inicial():
    """
    ---Area de un rectángulo---

    Pide la entrada del ancho y profundo de la habitación en metros. Devuelve la superficie en metros\
    cuadrados y en yardas cuadradas (tomando la referencia de aquí).

    Restricciones:

    1.Mantener los cálculos separados de la salida
    2.Usa una constante para las conversiones de unidades (aquí)
    """
    system('cls')

    strAncho = input("Introduce el ancho de la habitación en metros\n>")
    strProfundo = input("Introduce la profundidad de la habitación en metros\n>")

    ancho = int(strAncho)
    profundo = int(strProfundo)

    METRO_CUADRADO = 1.19599

    metros_cuadrados = (ancho*profundo) / 2
    yardas_cuadradas = METRO_CUADRADO * metros_cuadrados

    print(f"Superficie:\n{ancho} m de ancho * {profundo} m de profundo = {metros_cuadrados} m2\
        \n{metros_cuadrados} m2 = {round(yardas_cuadradas,2)} y2")

def reto1():
    # 1.Fuerza a que las entradas sean numéricas. Si no son numericas el usuario no podrá continuar.
    
    while True:

        system('cls')

        try:

            strAncho = input("Introduce el ancho de la habitación en metros\n>")
            if strAncho.isdigit() != True:
                raise ValueError

            strProfundo = input("Introduce la profundidad de la habitación en metros\n>")
            if strProfundo.isdigit() != True:
                raise ValueError
            
            break

        except:
            print("Debe introducir un valor numérico.")
            sleep(1.0)

    ancho = int(strAncho)
    profundo = int(strProfundo)

    METRO_CUADRADO = 1.19599

    metros_cuadrados = (ancho*profundo) / 2
    yardas_cuadradas = METRO_CUADRADO * metros_cuadrados

    print(f"Superficie:\n{ancho} m de ancho * {profundo} m de profundo = {metros_cuadrados} m2\
        \n{metros_cuadrados} m2 = {round(yardas_cuadradas,2)} y2")
    
def reto2():
    # 2.Crea una versión del programa que permita elegir si la entrada va en metros o en yardas
    while True:
        system('cls')
        #Comprobamos que introduzca una opcion de 'Y' o 'M'
        opcion = input("En que medida desea trabajar?\n'Y' para yardas - 'M' para metros.\n>")

        if opcion.upper() != 'Y' and opcion.upper() != 'M':
            print("No ha escogido una opción correcta")
            sleep(1.0)
        else:
            break

    if opcion.upper() == 'Y':

        strAnchoYardas = input("Introduce el ancho de la habitación en yardas\n>")
        strProfundoYardas = input("Introduce la profundidad de la habitación en yardas\n>")

        ancho = int(strAnchoYardas)
        profundo = int(strProfundoYardas)

        YARDA_CUADRADA = 0.83612736

        yardas_cuadradas = (ancho*profundo) / 2
        metros_cuadrados = YARDA_CUADRADA * yardas_cuadradas

        print(f"Superficie:\n{ancho} y de ancho * {profundo} y de profundidad = {yardas_cuadradas} y2\
            \n{yardas_cuadradas} y2 = {round(metros_cuadrados,2)} m2")

    elif opcion.upper() == 'M':

        strAnchoMetros = input("Introduce el ancho de la habitación en metros\n>")
        strProfundoMetros = input("Introduce la profundidad de la habitación en metros\n>")

        ancho = int(strAnchoMetros)
        profundo = int(strProfundoMetros)

        METRO_CUADRADO = 1.19599

        metros_cuadrados = (ancho*profundo) / 2
        yardas_cuadradas = METRO_CUADRADO * metros_cuadrados

        print(f"Superficie:\n{ancho} m de ancho * {profundo} m de profundidad = {metros_cuadrados} m2\
            \n{metros_cuadrados} m2 = {round(yardas_cuadradas,2)} y2")
    
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