from datetime import datetime
from os import system

def inicial():
    """
    ---Cálculo de la jubilación---

    Incorpora el año actual al programa. Crea un programa que cuente cuantos años faltan para tu jubilación
    y que te diga el año en que te jubilarás. Algo así

    ¿Cuantos años tienes? 48
    ¿A qué edad te jubilarás? 67
    Te quedan 19 años para jubilarte
    Estamos en 2018, te jubilarás en 2037.

    Restricciones:
    
    1.Convertir las cadenas de entrada en números
    2.Obten el año actual como lo haga python (no vale ponerlo como constante en el programa)
    """

    system('cls')

    fecha_actual = datetime.now()
    anno_actual = fecha_actual.year

    strEdad = input("¿Cuantos años tienes?\n>")
    strEdad_jubilacion = input("¿A qué edad te jubilarás?\n>")

    edad = int(strEdad)
    edad_jubilacion = int(strEdad_jubilacion)

    cantidad_annos_jubilacion = edad_jubilacion - edad
    anno_jubilacion = anno_actual + cantidad_annos_jubilacion

    print(f"Te quedan {cantidad_annos_jubilacion} años para jubilarte.\
        \nEstamos en {anno_actual}, te jubilarás en {anno_jubilacion}")
    
def reto1():
    # 1.Maneja la situación si el programa devuelve un número negativo de modo que diga que ya puede jubilarse
    system('cls')

    fecha_actual = datetime.now()
    anno_actual = fecha_actual.year

    strEdad = input("¿Cuantos años tienes?\n>")
    strEdad_jubilacion = input("¿A qué edad te jubilarás?\n>")

    edad = int(strEdad)
    edad_jubilacion = int(strEdad_jubilacion)

    cantidad_annos_jubilacion = edad_jubilacion - edad

    if cantidad_annos_jubilacion <= 0:

        print("Ya puedes jubilarte!")

    else:

        anno_jubilacion = anno_actual + cantidad_annos_jubilacion

        print(f"Te quedan {cantidad_annos_jubilacion} años para jubilarte.\
            \nEstamos en {anno_actual}, te jubilarás en {anno_jubilacion}")
        
reto1()
