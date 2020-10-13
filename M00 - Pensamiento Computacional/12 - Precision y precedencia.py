from time import sleep
from os import system

def inicial():
    """
    --- Cálculo de interés simple ---

    Crear un programa que calcule el interés simple, teniendo en cuenta que se calcula con la siguiente fórmula:

    A = P * (1 + r * t) 

    donde A es la cantidad ganada, P la cantidad invertida, r el interes y t los años transcurridos desde el inicio de la inversión

    Tras X años de inversión al Y %, su cantidad debe ser T

    Restricciones:
    1.La tasa de interés debe introducirse como porcentaje y no decimal, es decir 15 y no 0,15
    2.La inversión debe redondearse al céntimo
    3.La salida debe formatearse como divisa (€)

    Cantidad invertida: 1234.567
    Años transcurridos: 3.2
    Interés anual: 8
    Tras 3 años de inversión al 8.00%, su cantidad debe ser 1550.62€
    """
    strCapital = input("Cantidad invertida: ")
    strAnnos = input("Años Transcurridos: ")
    strInteres = input("Interés anual: ")

    P = round(float(strCapital),2)
    r = float(strInteres)/100
    t = float(strAnnos)

    A = P * (1 + r * t)

    print(f"Tras {int(t)} de inversión al {r*100:.2f}%, su cantidad debe ser {A:.2f}")

def reto1():
    # 1.Valida que las entradas sean numéricas y que el usuario no pueda continuar si no introduce un número
    while True:
        try:
            strCapital = input("Cantidad invertida: ")
            if strCapital[0] == '-' or strCapital[0] == '.':
                raise ValueError
            P = round(float(strCapital),2)

            strAnnos = input("Años Transcurridos: ")
            if strAnnos[0] == '-' or strAnnos[0] == '.':
                raise ValueError
            t = float(strAnnos)

            strInteres = input("Interés anual: ")
            if strInteres[0] == '-' or strInteres == '.':
                raise ValueError
            r = float(strInteres)/100
                
            break
        except:
            print("No ha introducido un valor correcto")    

    A = P * (1 + r * t)

    print(f"Tras {int(t)} de inversión al {r*100:.2f}%, su cantidad debe ser {A:.2f}")

def reto2():
    # 2.Modifica el programa para que imprima el valor de la inversión cada año de la misma hasta llegar al valor pedido
    while True:
        try:
            strCapital = input("Cantidad invertida: ")
            if strCapital[0] == '-' or strCapital[0] == '.':
                raise ValueError
            P = round(float(strCapital),2)

            strAnnos = input("Años Transcurridos: ")
            if strAnnos[0] == '-' or strAnnos[0] == '.':
                raise ValueError
            t = float(strAnnos)

            strInteres = input("Interés anual: ")
            if strInteres[0] == '-' or strInteres == '.':
                raise ValueError
            r = float(strInteres)/100
                
            break
        except:
            print("No ha introducido un valor correcto")    

    ix = 1

    while ix <= int(t):
        A = P * (1 + r * ix)
        if ix == 1:
            palabra_annos = 'año'
        else:
            palabra_annos = 'años'
        print(f"Tras {ix} {palabra_annos} de inversión al {r*100:.2f}%, su cantidad debe ser {A:.2f}")
        ix += 1
     
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