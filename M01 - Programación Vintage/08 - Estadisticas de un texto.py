"""
--- Modulo de estadísticas de un texto ---

Crear un módulo con las siguientes funciones

contarCaracteres(texto)
contarPalabras(texto)
contarVocales(texto)
contarConsonantes(texto)

Restricciones:

1.Cada función devolverá el valor numérico de lo que cuenta.
2.Si el módulo se ejecuta directamente (sin ser importado por otro programa deberá listar 
todos los valores de un texto en forma de tabla tabulada)

Retos:

1.Crear otros contadores como:
    contar signos de puntuacion fijando los mismos por ejemplo en los siguientes .,;:¡!¿?()[]-_
    contar un carácter determinado con la función contar(texto, 'r')
"""

vocales = 'aeiouáàéèíìóòúùâêîôûäëïöüÁÀÉÈÍÌÓÒÚÙÄËÏÖÜÂÊÎÔÛ'
consonantes = 'bcçdfghjklmnñpqrstvwxyzBCÇDFGHJKLMNÑPQRSTVWXYZ'
signos = '.,;:¡!¿?()[]-_'

def contarCaracteres(cadena):
    valor = 0

    for i in cadena:
       valor += 1

    return valor

def contarPalabras(cadena):
    lista_palabras = []
    palabra = ""
    contador_final = 1
    ultima_letra = False
    long_cadena = len(cadena)
    
    for letra in cadena:
        
        if contador_final == long_cadena:
            ultima_letra = True

            # Solo se entrará siendo el último caracter una consonante o vocal    

            if ultima_letra:
                if palabra != "" and letra in vocales or letra in consonantes:
                    palabra += letra
                    lista_palabras.append(palabra)
                                    
        if letra not in vocales and letra not in consonantes and palabra != "": #Caracter especial
            if len(palabra) != 1:
                lista_palabras.append(palabra)
                palabra = ""
            else:
                palabra = ""
            
        else:

            if len(palabra) != 0 or (letra in vocales or letra in consonantes): # Añadimos vocal o consonante
                palabra += letra
        contador_final += 1            
    
    return len(lista_palabras)
            


def contarVocales(cadena):
    valor = 0

    for i in cadena:
        if i in vocales:
            valor += 1
    
    return valor

def contarConsonantes(cadena):
    valor = 0

    for i in cadena:
        if i in consonantes:
            valor += 1
    
    return valor

def contarSignos(cadena):
    valor = 0

    for letra in cadena:
        if letra in signos:
            valor += 1

    return valor

def contarCaracterDet(cadena, caracter):
    valor = 0

    for letra in cadena:
        if letra == caracter:
            valor +=1

    return valor

if __name__ == "__main__":
    cadena = "Hola, que tal? Como fue por allá? Por aquí todo sigue igual..."
    caracter = 'o'
    print(f"La cadena: {cadena}\ntiene un total de: {contarCaracteres(cadena)} caracteres.")
    print(f"La cadena: {cadena}\ntiene un total de: {contarPalabras(cadena)} palabras.")
    print(f"La cadena: {cadena}\ntiene un total de: {contarVocales(cadena)} vocales.")
    print(f"La cadena: {cadena}\ntiene un total de: {contarConsonantes(cadena)} consonantes.")
    print(f"La cadena: {cadena}\ntiene un total de: {contarSignos(cadena)} signos de puntuación.")
    print(f"La cadena: {cadena}\ntiene un total de: {contarCaracterDet(cadena, caracter)} '{caracter}'.")

