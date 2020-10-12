from time import sleep
from os import system

def inicial():
    """
    --- Tasa autonómica ---

    Construye un programa que aplique una tasa a un precio en función de donde se aplique.
    Así si la provincia en la que se aplica es 'VA' (Valencia) se debe incrementar el precio en un 5,5%. 
    En otro caso no se aplicará esta tasa. La salida debe ser distinta en función de la provincia, así:

    Si el precio es 10 €
    - Provincia = 'VA':
            El subtotal es 10.00€
            La tasa es 0.55€
            El total es 10.55€
    
    - Provincia != 'VA':
            El total es 10.00€

    Restricciones:

    1.Implementar este programa usando sólo un if sin usar else
    2.Las cifras en € deben estar redondeadas al céntimo
    3.Utiliza una sola sentencia print para dar el resultado
    """
    provincia = input("Introduzca su provincia: ")
    strPrecio = input("Introduzca el precio: ")

    precio = float(strPrecio)

    tasa = precio * 0.055
    total = precio + tasa

    mensaje = f"El total es {precio:.2f}€"

    if provincia == 'VA':
        mensaje = f"El subtotal es {precio:.2f}€\nLa tasa es {tasa:.2f}€\nEl total es {total:.2f}€"

    print(mensaje)

def reto1():
    # 1.Permitir al usuario introducir su provincia en mayúsculas, minúsculas o mixto
    provincia = input("Introduzca su provincia: ")
    strPrecio = input("Introduzca el precio: ")

    precio = float(strPrecio)

    tasa = precio * 0.055
    total = precio + tasa

    mensaje = f"El total es {precio:.2f}€"

    if provincia.upper() == 'VA':
        mensaje = f"El subtotal es {precio:.2f}€\nLa tasa es {tasa:.2f}€\nEl total es {total:.2f}€"

    print(mensaje)
    
def reto2():
    # 2.Permitir al usuario introducir el nombre completo de su provincia en mayúsculas, minúsculas o mixto
    provincia = input("Introduzca su provincia: ")
    strPrecio = input("Introduzca el precio: ")

    precio = float(strPrecio)

    tasa = precio * 0.055
    total = precio + tasa

    mensaje = f"El total es {precio:.2f}€"

    if provincia.upper() == 'VALENCIA':
        mensaje = f"El subtotal es {precio:.2f}€\nLa tasa es {tasa:.2f}€\nEl total es {total:.2f}€"

    print(mensaje)

def main():
    while True:

        system('cls')
        opcion = input("Elige una opción:\n1 - Programa normal\n2 - Reto 1\n3 - Reto 2\n>")

        if opcion == "1":
            print("Ha elegido Programa normal")
            sleep(1.0)
            system('cls')
            inicial()
            break
        elif opcion == "2":
            print("Ha elegido Reto 1")
            sleep(1.0)
            system('cls')
            reto1()
            break
        elif opcion == "3":
            print("Ha elegido Reto 2")
            sleep(1.0)
            system('cls')
            reto2()
            break
        else:
            print("No ha escogido opción correcta")
            sleep(1.0)
            system('cls')

main()