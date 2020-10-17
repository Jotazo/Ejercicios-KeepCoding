from misModulos.metodos_cadenas import *

"""

--- Crear funcion que convierta un texto a minúsculas ---

Crear funcion que convierta un texto a minúsculas según la definición myLower(cadena)

Restricciones:

1.Crearla de tal manera que sólo incluya los caracteres alfabéticos
2.Crearla en forma de módulo

Retos:

1.Validar que el parámetro sea del tipa adecuado y si no lo es gestionar el error 
sin que se produzca una excepción. Para comprobar si una variable es del tipo esperado utilizar isinstance

"""

def myLower(cadena):
    nueva_cadena = ""
    for caracter in cadena:
        if mayus(caracter):
            caracter_minuscula = ord(caracter) + 32
            nueva_cadena += chr(caracter_minuscula)
        else:
            nueva_cadena += caracter
    return nueva_cadena
    
cadena_inicial = 'HÓlÖ *`1wsa" ASSASd CÈracÜla'
cadena_minusculas2 = myLower(cadena_inicial)
print(f"Cadena inicial:\n{cadena_inicial}\nCadena en minúsculas:\n{cadena_minusculas2}")