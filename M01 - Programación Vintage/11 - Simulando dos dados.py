import random
from misModulos.screen import locate, clear
from os import system

"""
--- Simular la tirada de dos dados ---

Para simular una tirada de dados o cualquier otro hecho cuyo resultado se debe al azar utilizamos la librería random de python.

En este caso necesitamos un programa que simule la tirada de dos dados mil veces y que nos devuelva la frecuencia de cada resultado
para luego imprimirla.

La mejor manera de hacerlo es un diccionario con los 11 resultados posibles, a saber, 2, 3, 4, 5, ..., 11 y 12.

Restricciones:

1.Mostrar una lista en pantalla con el valor de la combinación, la frecuencia aparecida en nuestra simulación en porcentaje, 
y el porcentaje previsto. Así:

Total    Simulated    Expected
           Percent     Percent
   2          2.90        2.78
   3          6.90        5.56
   4          9.40        8.33
   5         11.90       11.11
   6         14.20       13.89
   7         14.20       16.67
   8         15.00       13.89
   9         10.50       11.11
  10          7.90        8.33
  11          4.50        5.56
  12          2.60        2.78
"""
totales = {
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0,
    10:0,
    11:0,
    12:0
}

esperados = {
    2:2.78,
    3:5.56,
    4:8.33,
    5:11.11,
    6:13.89,
    7:16.67,
    8:13.89,
    9:11.11,
    10:8.33,
    11:5.56,
    12:2.78
}

pos_ast = {
    2:36,
    3:40,
    4:44,
    5:48,
    6:52,
    7:56,
    8:60,
    9:64,
    10:68,
    11:72,
    12:76
}

# -------- Funciones Dibujar---------- #

def imprimeTexto():

    locate(4,0)
    print("Total")
    locate(4,10)
    print("Simulated")
    locate(4,23)
    print("Expected")
    locate(5,12)
    print("Percent")
    locate(5,24)
    print("Percent")

def dibujaRaya():
    raya='------------------------------------------'
    locate(18,35)
    print(raya)

def dibujaNumeros():
    ix = 36

    for i in range(2,13):
        if i == 10 or i == 11 or i == 12:
            locate(19,ix)
            print('1')    
        else:
            locate(19,ix)
            print(i)
        ix += 4

    ix = 68

    for i in range(0,3):
        locate(20,ix)
        print(i)
        ix += 4

def dibujaTabla():
    dibujaRaya()
    dibujaNumeros()

def dibujaAsterisco(numero):
    cant_asteriscos = int(totales[numero]/10)
    linea = 17
    columna = pos_ast[numero] 
    for i in range(cant_asteriscos):
        locate(linea, columna)
        print('*')
        linea -= 1

# -------------------------------------------------------- #


for i in range(1000):

    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    resultado = dado1+dado2
    totales[resultado] += 1

system('cls')

imprimeTexto()

ix = 2

for i in range(6,17):
    locate(i, 2)
    print(f"{ix:>2}")
    locate(i,14)
    print(f"{totales[ix]/10:5.2f}")
    locate(i,26)
    print(f"{esperados[ix]:5.2f}")
    ix += 1

for i in range(2,13):
    dibujaAsterisco(i)

dibujaTabla()


