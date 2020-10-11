from datetime import datetime
from time import sleep
from os import system

def inicial():
    """
    --- Cálculo de interés simple ---

    Crear un programa que calcule el interés simple, teniendo en cuenta que se calcula con la siguiente fórmula:

    A=P⋅(1+rt)

    donde A es la cantidad ganada, P la cantidad invertida, r el interes y t los años transcurridos desde el inicio de la inversión

    Tras X años de inversión al Y %, su cantidad debe ser T

    Restricciones:

    1.La tasa de interés debe introducirse como porcentaje y no decimal, es decir 15 y no 0,15
    2.La inversión debe redondearse al céntimo
    3.La salida debe formatearse como divisa (€)
    """
    fecha_actual = datetime.now()

    cantidad_invertida = float(input("Introduzca la cantidad invertida: ")) 
    interes = int(input("Introduzca el tipo de interés: ")) 
    anno_inicial = int(input("Introduzca el año de inicio de la inversión: "))

    anno_actual = fecha_actual.year
    annos_transcurridos = anno_actual - anno_inicial 

    r = cantidad_invertida*(interes/100)
    A = cantidad_invertida*(1+r*annos_transcurridos)

    print(f"Tras {annos_transcurridos} años de inversión al {interes} %, su cantidad debe ser {round(A,2)}")
def reto1():
    # 1.Valida que las entradas sean numéricas y que el usuario no pueda continuar si no introduce un número
    fecha_actual = datetime.now()
    while True:
        try:
            system('cls')

            cantidad_invertida = float(input("Introduzca la cantidad invertida: ")) 
            if cantidad_invertida <= 0:
                raise ValueError
            interes = int(input("Introduzca el tipo de interés: ")) 
            if interes <= 0:
                raise ValueError
            anno_inicial = int(input("Introduzca el año de inicio de la inversión: "))
            if anno_inicial <= 0:
                raise ValueError
            break
        except:
            print("No ha introducido un valor correcto.")
            print("No puede ser ni un valor negativo ni 0")
            sleep(1.5)

    anno_actual = fecha_actual.year
    annos_transcurridos = anno_actual - anno_inicial 
    
    r = cantidad_invertida*(interes/100)
    A = cantidad_invertida*(1+r*annos_transcurridos)

    print(f"Tras {annos_transcurridos} años de inversión al {interes} %, su cantidad debe ser {round(A,2)}")
def reto2():
    # 2.Modifica el programa para que imprima el valor de la inversión cada año de la misma hasta llegar al valor pedido
    fecha_actual = datetime.now()
    while True:
        try:
            system('cls')

            cantidad_invertida = float(input("Introduzca la cantidad invertida: ")) 
            if cantidad_invertida <= 0:
                raise ValueError
            interes = int(input("Introduzca el tipo de interés: ")) 
            if interes <= 0:
                raise ValueError
            anno_inicial = int(input("Introduzca el año de inicio de la inversión: "))
            if anno_inicial <= 0:
                raise ValueError
            break
        except:
            print("No ha introducido un valor correcto.")
            print("No puede ser ni un valor negativo ni 0")
            sleep(1.5)
            
    anno_actual = fecha_actual.year
    annos_transcurridos = anno_actual - anno_inicial 
    annos_trans_2 = 1

    r = cantidad_invertida*(interes/100)
    

    for i in range(1,annos_transcurridos):
        annos_trans_2 = i
        A = cantidad_invertida*(1+r*annos_trans_2)
        print(f"Tras {annos_trans_2} años de inversión al {interes} %, su cantidad debe ser {round(A,2)}")
        

    A = cantidad_invertida*(1+r*annos_transcurridos)
    print(f"Tras {annos_transcurridos} años de inversión al {interes} %, su cantidad debe ser {round(A,2)}")
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