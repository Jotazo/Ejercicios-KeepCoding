from time import sleep
from os import system

def inicial():
    """
    ---Aplicando impuestos---
    
    Haz un programa que aplique un impuesto de 5,5% sobre tres precios introducidos por el usuario.
    Deben introducirse también el número de ejemplares de producto de cada precio que se compran. 
    Se debe imprimir el subtotal sin tasas, la tasa y la suma de ambos

    Restricciones:

    1.Manten separadas las partes de entrada, salida y proceso de tu programa
    """
    productos_y_precios = {}
    # --- Introduccion de datos --- #

    for i in range(3):
        precio_producto = float(input("Introduzca el precio del producto a comprar: "))
        num_ejemplares = int(input("Introduzca la cantidad de ejemplares a comprar: "))
        productos_y_precios[precio_producto] = num_ejemplares

    # --- Procesos del programa --- #

    precio_total = 0
    unidades_totales = 0

    for precios, unidades in productos_y_precios.items():
        precio_total += (precios*unidades)
        unidades_totales += unidades
    
    IMPUESTO = 0.055
    precio_con_impuesto = precio_total + (precio_total*IMPUESTO)

    # --- Salida de datos --- #

    contador = 1
    for precio, unidades in productos_y_precios.items():
        unidad = ''
        if unidades == 1:
            unidad = 'unidad'
        else:
            unidad = 'unidades'
        print(f"Producto {contador} - {precio:6.2f} € / unidad - {precio*unidades:6.2f} € x {unidades} {unidad}")
        contador += 1

    print(f"\t\t\t\t----------------------")
    print(f"\t Subtotal sin tasas    : {precio_total:6.2f} € x {unidades_totales} unidades")

    print(f"\t\t\t\t----------------------")
    print(f"\t Total con impuesto(5%): {precio_con_impuesto:6.2f} € x {unidades_totales} unidades") 
        
def reto1():
    # 1.Comprobar que la entrada sea numérica e impedir continuar si no es así
    productos_y_precios = {}

    # --- Introduccion de datos --- #

    for i in range(3):
        while True:
            system('cls')
            try:
                precio_producto = float(input("Introduzca el precio del producto a comprar: "))
                if precio_producto <= 0:
                    raise ValueError
                num_ejemplares = int(input("Introduzca la cantidad de ejemplares a comprar: "))
                if num_ejemplares <= 0:
                    raise ValueError
                break
            except:
                print("No ha introducido un valor correcto")
                print("Debe ser un numero entero positivo y no puede ser 0")
                sleep(1.0)

        productos_y_precios[precio_producto] = num_ejemplares

    # --- Procesos del programa --- #

    precio_total = 0
    unidades_totales = 0

    for precios, unidades in productos_y_precios.items():
        precio_total += (precios*unidades)
        unidades_totales += unidades

    IMPUESTO = 0.055
    precio_con_impuesto = precio_total + (precio_total*IMPUESTO)

    # --- Salida de datos --- #

    contador = 1
    for precio, unidades in productos_y_precios.items():
        unidad = ''
        if unidades == 1:
            unidad = 'unidad'
        else:
            unidad = 'unidades'
        print(f"Producto {contador} - {precio:6.2f} € / unidad - {precio*unidades:6.2f} € x {unidades:2.0f} {unidad}")
        contador += 1

    print(f"\t\t\t\t----------------------")
    print(f"\t Subtotal sin tasas    : {precio_total:6.2f} € x {unidades_totales} unidades")
    
    print(f"\t\t\t\t----------------------")
    print(f"\t Total con impuesto(5%): {precio_con_impuesto:6.2f} € x {unidades_totales} unidades")

def reto2():
    # 2.Permitir que el programa tenga un número indeterminado de productos y cantidades de entrada
    productos_y_precios = {}
    
    salir = False

    # ---Introducción de datos--- #

    while not salir:
        
        while True:

            system('cls')
            try:
                precio_producto = float(input("Introduzca el precio del producto a comprar: "))
                if precio_producto <= 0:
                    raise ValueError
                num_ejemplares = int(input("Introduzca la cantidad de ejemplares a comprar: "))
                if num_ejemplares <= 0:
                    raise ValueError
                break
            except:
                print("No ha introducido un valor correcto")
                print("Debe ser un numero entero positivo y no puede ser 0")
                sleep(1.0)

        productos_y_precios[precio_producto] = num_ejemplares

        opcion = ""

        # Preguntamos si quiere introducir mas productos

        while True:
            opcion = input("Desea introducir otro producto?(S/N) ")
            if opcion.upper() == 'N':
                salir = True
                break
            elif opcion.upper() == 'S':
                break
            else:
                print("No ha introducido una opción correcta.")
                print("Por favor, introduzca S/N en función de si quiere o no introducir otro producto")

    precio_total = 0
    unidades_totales = 0

    # Calculamos el total de todos los precios y el total de unidades

    for precios, unidades in productos_y_precios.items():
        precio_total += (precios*unidades)
        unidades_totales += unidades

    IMPUESTO = 0.055
    precio_con_impuesto = precio_total + (precio_total*IMPUESTO)
    

    # --- Salida de datos --- #

    system('cls') # Limpiamos la pantalla y la preparamos para la salida de datos

    # Imprimimos el Producto, el precio por unidad y el precio total según unidades

    contador = 1

    for precio, unidades in productos_y_precios.items():
        unidad = ''
        if unidades == 1:
            unidad = 'unidad'
        else:
            unidad = 'unidades'
        print(f"Producto {contador} - {precio:6.2f} € / unidad - {precio*unidades:6.2f} € x {unidades:2.0f} {unidad}")
        contador += 1

    # Imprimimos el subtotal sin tasas

    print(f"\t\t\t\t----------------------")
    print(f"\t Subtotal sin impuesto : {precio_total:6.2f} € x {unidades_totales:2.0f} unidades")

    # Imprimimos el total con tasas

    print(f"\t\t\t\t----------------------")
    print(f"\t Total con impuesto(5%): {precio_con_impuesto:6.2f} € x {unidades_totales:2.0f} unidades")

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