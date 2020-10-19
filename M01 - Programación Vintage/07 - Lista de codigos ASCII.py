"""
--- Listando códigos ascii ---

Crear un programa que devuelva los códigos ASCII de los carácteres desde el 32 al 127.

Restricciones:

1. Formatear la salida en cuantro columnas perfectamente alineadas. Puedes ayudarte con format y print

Retos:

1.Crear un modulo con una función que imprima la tabla de asciis tal cual se muestra arriba y 
que lo haga directamente si no se ejecuta desde otro programa (lo hace como main texto del enlace)
"""

def codigo_ascii():
    contador = 1
    for i in range(32, 128):
        if contador % 4 == 0:
            print(f"{chr(i):>10}\n")
        else:
            print(f"{chr(i):>10}", end = " ")
        contador += 1
        
if __name__ == "__main__":
    codigo_ascii()