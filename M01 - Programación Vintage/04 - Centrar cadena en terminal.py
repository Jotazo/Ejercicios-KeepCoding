import math

"""
--- Centrar cadena en terminal ---

Crear una función que añada espacios por delante a una cadena hasta dejarla centrada en la terminal. 
Para ello se utilizarán como parámetros la cadena y la anchura en caracteres del terminal.

Restricciones:

1.No se deben añadir espacios por detrás de la cadena

Retos:

1.Controlar que los parámetros son del tipo adecuado, es decir, cadena es un string y anchura un entero. 
Utilizando la documentación de python podemos ver que se puede validar el tipo de una variable utilizando 
la funcion predefinida isinstance() ver aquí
"""

def centrar(cadena, anchura = 168):
    palabra_espaciada = ""
    num_espacios = math.floor((anchura-len(cadena))/2)

    for i in range(num_espacios):
        palabra_espaciada += ' '

    palabra_espaciada += cadena

    return palabra_espaciada

print(centrar('cat'))
