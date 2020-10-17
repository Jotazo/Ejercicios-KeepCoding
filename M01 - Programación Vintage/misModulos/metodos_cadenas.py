def mayus(letra):
    if (ord(letra) >= 65 and ord(letra) <= 90) or ord(letra) == 199 or ord(letra) == 209:
        return True
    else:
        return False

def minus(letra):
    if (ord(letra) >= 97 and ord(letra) <= 122) or ord(letra) == 231 or ord(letra) == 241:
        return True
    else:
        return False

def mayus_caracteres(letra):
    if (ord(letra) >= 192 and ord(letra) <= 221 and (ord(letra) != 199 and ord(letra) != 209))\
         or (ord(letra) >= 256 and ord(letra) <= 382 and ((ord(letra) % 2) == 0)):
        return True
    else:
        return False

def minus_caracteres(letra):
    if (ord(letra) >= 224 and ord(letra) <= 255 and (ord(letra) != 231 and ord(letra) != 241))\
        or (ord(letra) >= 256 and ord(letra) <= 382 and ((ord(letra) % 2) != 0)):
        return True
    else:
        return False

def numeros(letra):
    if ord(letra) >= 48 and ord(letra) <= 57:
        return True
    else:
        return False

def caracteres_especiales(letra):
    if not mayus(letra) and not minus(letra) and not mayus_caracteres(letra)\
       and not minus_caracteres(letra) and not numeros(letra):
        return True
    else:
        return False

def tipoLetra(letra):
    if mayus(letra):
        return 0
    elif minus(letra):
        return 1
    elif mayus_caracteres(letra):
        return 2
    elif minus_caracteres(letra):
        return 3
    elif numeros(letra):
        return 4
    elif caracteres_especiales(letra):
        return 5

def cuenta_letras(cadena):
    letras = 0
    resultado = 0

    for letra in cadena:
        if tipoLetra(letra) >=0 and tipoLetra(letra) <= 3:
            letras += 1

    resultado += letras

    return resultado

    
if __name__ == "__main__":
        
    print(cuenta_letras('PeréstoKixao110**'))

    for caracter in 'PeréstoKixao110**':

        if tipoLetra(caracter) == 0:
            print(f"{caracter} es una mayúscula")
        elif tipoLetra(caracter) == 1:
            print(f"{caracter} es una minúscula")
        elif tipoLetra(caracter) == 2:
            print(f"{caracter} es una mayúscula con caracter especial")
        elif tipoLetra(caracter) == 3:
            print(f"{caracter} es una minúscula con caracter especial")
        elif tipoLetra(caracter) == 4:
            print(f"{caracter} es un número")
        else:
            print(f"{caracter} es un carácter especial")