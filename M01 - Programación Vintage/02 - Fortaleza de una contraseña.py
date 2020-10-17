from misModulos.metodos_cadenas import *

"""
Crea un programa que dtermine la complejidad de una contraseña en base a las siguientes reglas:

Una contraseña muy débil contiene sólo números y su longitud es menor de 8 carácteres
Una contraseña débil contiene sólo letras y su longitud es menor de 8 carácteres
Una contraseña es fuerte si contiene letras y al menos un número y tiene al menos 8 carácteres de longitud
Una contraseña es muy fuerte si tiene letras, números y caracteres especiales con al menos 8 carácteres de longitud

Restricciones:

1.Crear una función validaPwd que devuelva un valor que evaluado por otro programa determine 
si la contraseña es muy débil, débil, fuerte o muy fuerte. No devuelvas una cadena, debe servir para otros lenguajes.

2.Utilizar una sentencia de salida única
"""

def validaPwd(pwd):
    letras = 0
    numeros = 0
    car_esp = 0

    for letra in pwd:
        if tipoLetra(letra) >= 0 and tipoLetra(letra) <=3:
            letras += 1
        elif tipoLetra(letra) == 4:
            numeros += 1
        elif tipoLetra(letra) == 5:
            car_esp += 1
    if len(pwd) < 4:
        return -1
    else:
        if numeros > 0 and (letras == 0 and car_esp == 0) and len(pwd) < 8:
            return 0
        elif letras > 0 and (numeros == 0 and car_esp == 0) and len(pwd) < 8:
            return 1
        elif letras > 0 and numeros > 0 and car_esp == 0 and len(pwd) >= 8:
            return 2
        elif letras > 0 and numeros > 0 and car_esp > 0 and len(pwd) >= 8:
            return 3

def comprueba_fortaleza(valor):
    if valor == 0:
        return "La contraseña es muy débil"
    elif valor == 1:
        return "La contraseña es débil"   
    elif valor == 2:
        return "La contraseña es fuerte"
    elif valor == 3:
        return "La contraseña es muy fuerte"
    else:
        return "La contraseña tiene menos de 4 carácteres"

print(comprueba_fortaleza(validaPwd('asa')))