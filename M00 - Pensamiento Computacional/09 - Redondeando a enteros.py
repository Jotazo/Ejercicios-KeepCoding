from math import ceil
from math import pi
from time import sleep
from os import system

def inicial():
    """
    ---Pintando el techo---

    5 litros de pintura dan para pintar 100 metros cuadrados de techo. Teniendo esto en cuenta\
    haz un programa que diga cuantos botes de 5 litros de pintura hay que comprar para pintar un techo de anchura y\
    profundidad informada por el usuario (en metros). Devuelve el número de botes suficiente y por supuesto en números enteros.

    Necesitarás 12 litros para pintar 240 metros cuadrados de techo.
    
    Debes comprar 3 botes de pintura.

    Restricciones:

    1.Utiliza una constante para calcular la conversión botes de pintura/metros de techo
    2.Asegurate de comprar un número entero de botes de pintura suficiente (el siguiente número entero) pero no de más
    """

    anchura = int(input("Introduce los metros de anchura del techo a pintar\n>"))
    profundidad = int(input("Introduce los metros de profundidad del techo a pintar\n>"))

    METROXLITRO = 0.05

    metros_cuadrados_techo = anchura * profundidad
    
    total_litros = int(metros_cuadrados_techo * METROXLITRO)
    TOTAL_BOTES = total_litros / 5

    if int(TOTAL_BOTES) < TOTAL_BOTES:
        TOTAL_BOTES = int(TOTAL_BOTES) + 1

    print(f"Para pintar {metros_cuadrados_techo} m2 de techo, son necesarios {TOTAL_BOTES} botes de pintura de 5l.")

def reto1():
    # 1.Revisar que la entrada sean números positivos. Si no es así no dejar que el usuario continue
    while True:
        try:
            system('cls')
            anchura = int(input("Introduce los metros de anchura del techo a pintar\n>"))
            if anchura <= 0:
                raise ValueError
            profundidad = int(input("Introduce los metros de profundidad del techo a pintar\n>"))
            if profundidad <= 0:
                raise ValueError
        except:
            print("No ha introducido un valor correcto. No se admiten ni números negativos ni 0")
            sleep(1.0)

    METROXLITRO = 0.05

    metros_cuadrados_techo = anchura * profundidad
    
    total_litros = int(metros_cuadrados_techo * METROXLITRO)
    TOTAL_BOTES = total_litros / 5

    if int(TOTAL_BOTES) < TOTAL_BOTES:
        TOTAL_BOTES = int(TOTAL_BOTES) + 1

    print(f"Para pintar {metros_cuadrados_techo} m2 de techo, son necesarios {TOTAL_BOTES} botes de pintura de 5l.")
    
def reto2():
    # 2.Hacer el cálculo para habitación redonda
    
    diametro = int(input("Introduce el diametro de la habitación a pintar en metros cuadrados\n>"))

    METROXLITRO = 0.05

    diametro_techo = pi * (diametro**2/4)

    total_litros = diametro_techo * METROXLITRO
    TOTAL_BOTES = total_litros / 5

    if int(TOTAL_BOTES) < TOTAL_BOTES:
        TOTAL_BOTES = int(TOTAL_BOTES) + 1

    print(f"Para pintar {round(diametro_techo,2)} m2 de techo, son necesarios {TOTAL_BOTES} botes de pintura de 5l.")

def reto3():
    # 3.Hacer el cálculo para habitación en forma de L

    pared_larga1 = float(input("Introduce la longitud (en metros) de la pared 1 mas larga: "))
    pared_corta1 = float(input("Introduce la longitud (en metros) de la pared 1 mas corta: "))

    pared_larga2 = float(input("Introduce la longitud (en metros) de la pared 2 mas larga: "))
    pared_corta2 = float(input("Introduce la longitud (en metros) de la pared 2 mas corta: "))

    rectangulo1 = pared_larga1*pared_corta1
    rectangulo2 = pared_larga2*pared_corta2
    
    metros_cuadrados = rectangulo1 + rectangulo2

    METROXLITRO = 0.05

    total_litros = int(metros_cuadrados * METROXLITRO)
    TOTAL_BOTES = total_litros / 5

    if int(TOTAL_BOTES) < TOTAL_BOTES:
        TOTAL_BOTES = int(TOTAL_BOTES) + 1

    print(f"Para pintar {metros_cuadrados} m2 de techo, son necesarios {TOTAL_BOTES} botes de pintura de 5l.")

reto3()