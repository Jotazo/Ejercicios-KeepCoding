def inicial():

    """
    --- Crear funcion replace ---

    Crear una función que tome una cadena y remplace el caracter de una posición dada por otro según la definición
    myReplace(cadena, posicion, nuevoValor)

    Restricciones:

    1.Teniendo en cuenta que en python una cadena es realmente una tupla de caracteres (inmutable, no se puede modificar
    ni su longitud, ni su contenido) deberás valorar crear una nueva cadena con el resultado y devolverla.
    Crear un módulo reutilizable. Para hacerlo correctamente (incluyendo la distinción entre utilizarlo como módulo o como main 
    - no visto aún en clase - mira aquí)
    
    Posible solución
    Hay varias soluciones, voy a plantear la de fuerza bruta, iterar la cadena hasta encontrar la posición y 
    entonces modificarla. También se podría hacer con subcadenas (ver aquí) utilizando los accesos de python a listas y tuplas. 
    Sería más rápido y elegante. Esa solución os la dejo a vosotros
    """
    def myReplace(cadena, posicion, nuevoValor):
        nueva_cadena = ""
        lista_cadena = list(cadena)
        for indice, letra in enumerate(lista_cadena):
            if indice == posicion - 1:
                nueva_cadena += nuevoValor
            else:
                nueva_cadena += letra
        return nueva_cadena
    
    palabra = myReplace('pena', 4, 'e')

    print(palabra)


def reto1():
    # 1.Crear la función dada como solución con un for
    pass

def reto2():
    # 2.Crear una función que no indique la posición sino con esta firma myReplace(cadena, viejoCaracter, nuevoCaracter) 
    # y que lo haga para todas las ocurrencias de viejoCaracter
    def myReplace(cadena, viejoCaracter, nuevoCaracter):
        nueva_cadena = ""
        for letra in cadena:
            if viejoCaracter == letra:
                nueva_cadena += nuevoCaracter
            else:
                nueva_cadena += letra
        return nueva_cadena
    
    palabra = myReplace('esternocleidomastoideo', 'e', '3')
    
    print(palabra)

reto2()