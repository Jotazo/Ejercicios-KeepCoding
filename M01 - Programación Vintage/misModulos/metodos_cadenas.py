def mayus(letra):
    """
    Devuelve TRUE si 'letra' es mayúscula
    """
    if (ord(letra) >= 65 and ord(letra) <= 90) or (ord(letra) >= 192 and ord(letra) <= 221)\
        or (ord(letra) >= 256 and ord(letra) <= 382 and ((ord(letra) % 2) == 0)):
        return True
    else:
        return False

def minus(letra):
    """
    Devuelve TRUE si 'letra' es minúscula
    """
    if (ord(letra) >= 97 and ord(letra) <= 122) or ord(letra) == 231 or ord(letra) == 241 or \
       (ord(letra) >= 224 and ord(letra) <= 255) or (ord(letra) >= 256 and ord(letra) <= 382 and ((ord(letra) % 2) != 0)):
        return True
    else:
        return False

def numeros(letra):
    """
    Devuelve TRUE si 'letra' es un número
    """
    if ord(letra) >= 48 and ord(letra) <= 57:
        return True
    else:
        return False

def caracteres_especiales(letra):
    """
    Devuelve TRUE si 'letra' es un caracter especial
    """
    if not mayus(letra) and not minus(letra) and not numeros(letra):
        return True
    else:
        return False

def tipoLetra(letra):
    """
    Función que en relación a las funciones antes dadas nos retornará:
    - 0 si es mayúscula
    - 1 si es minuscula
    - 2 si es un número
    - 3 si es un caracter especial
    """
    if mayus(letra):
        return 0
    elif minus(letra):
        return 1
    elif numeros(letra):
        return 2
    elif caracteres_especiales(letra):
        return 3

def cuenta_letras(cadena):
    """
    Función que devuelve el numero de letras que tiene 'cadena'
    """
    letras = 0
    resultado = 0

    for letra in cadena:
        if tipoLetra(letra) <= 1:
            letras += 1

    resultado += letras

    return resultado

def myLower(cadena):
    """
    Función 'lower()' propia
    """
    nueva_cadena = ""
    for caracter in cadena:
        if mayus(caracter):
            caracter_minuscula = ord(caracter) + 32
            nueva_cadena += chr(caracter_minuscula)
        else:
            nueva_cadena += caracter
    return nueva_cadena

    
if __name__ == "__main__":
        
    print(cuenta_letras('PeréstoKixao110**'))

    for caracter in 'PeréstoKixao110**':

        if tipoLetra(caracter) == 0:
            print(f"{caracter} es una mayúscula")
        elif tipoLetra(caracter) == 1:
            print(f"{caracter} es una minúscula")
        elif tipoLetra(caracter) == 2:
            print(f"{caracter} es un número")
        else:
            print(f"{caracter} es un carácter especial")