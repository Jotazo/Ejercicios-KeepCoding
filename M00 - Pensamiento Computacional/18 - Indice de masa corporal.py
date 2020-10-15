from time import sleep
from os import system

def inicial():
    """

    --- Indice de masa corporal ---

    Craer un programa que calcule el indice de masa corporal de una persona según la fórmula

    IMC= (peso/altura**2)

    Si el índice de masa corporal está entre 18,5 y 15 el peso se considera normal. Por encima se considera sobrepeso, por debajo delgadez.

    Haz un programa que pida ambos datos, devuelva tu índice de masa corporal e indique si estás por encima o por debajo de la normalidad

    Restricciones:

    1.Impedir que el programa continúe si se introducen datos no numéricos
    """

    while True:
        try:

            strPeso = input("Introduce tu peso(en kg): ")
            if strPeso[0] == '-' or strPeso[0] == '.':
                raise ValueError
            peso = float(strPeso)

            strAltura = input("Introduce tu altura(en m): ")
            if strAltura[0] == '-' or strAltura[0] == '.':
                raise ValueError
            altura = float(strAltura)

            break

        except:
            print("No ha introducido un valor numérico")
            

    imc = (peso/altura**2)
    
    if imc > 18.5:
        print(f"Su IMC es de: {imc}\nEsta por encima de su peso")
    elif imc <= 18.5 and imc >= 15:
        print(f"Su IMC es de: {imc}\nEsta en su peso")
    else:
        print(f"Su IMC es de: {imc}\nEsta por debajo de su peso")

def reto1():
    
    # 1.Crear una versión que acepte unidades de altura y peso anglosajonas (deberás buscar y cambiar la fórmulas)

    tipoDatos = input("Escoge una opcion:\n1 - Para IMC, con medidas europeas\n2 - Para IMC, con medidas anglosajonas:\n>")

    if tipoDatos == '1':

        while True:
            try:

                strPeso = input("Introduce tu peso(en kg): ")
                if strPeso[0] == '-' or strPeso[0] == '.':
                    raise ValueError
                peso = float(strPeso)

                strAltura = input("Introduce tu altura(en m): ")
                if strAltura[0] == '-' or strAltura[0] == '.':
                    raise ValueError
                altura = float(strAltura)

                break

            except:
                print("No ha introducido un valor numérico")          

        imc = (peso/altura**2)

        if imc > 18.5:
            print(f"Su IMC es de: {imc:.2f}\nEsta por encima de su peso")
                
        elif imc <= 18.5 and imc >= 15:
            print(f"Su IMC es de: {imc:.2f}\nEsta en su peso")
                
        else:
            print(f"Su IMC es de: {imc:.2f}\nEsta por debajo de su peso")

    if tipoDatos == '2':

        while True:
            try:

                strPeso = input("Introduce tu peso(en lb): ")
                if strPeso[0] == '-' or strPeso[0] == '.':
                    raise ValueError
                peso = float(strPeso)

                strAltura = input("Introduce tu altura(en in): ")
                if strAltura[0] == '-' or strAltura[0] == '.':
                    raise ValueError
                altura = float(strAltura)

                break

            except:
                print("No ha introducido un valor numérico")          

        imc = (peso / (altura**2)) * 703

        if imc > 18.5:
            print(f"Su IMC es de: {imc:.2f}\nEsta por encima de su peso")
                
        elif imc <= 18.5 and imc >= 15:
            print(f"Su IMC es de: {imc:.2f}\nEsta en su peso")
                
        else:
            print(f"Su IMC es de: {imc:.2f}\nEsta por debajo de su peso")
                
def diagnostico(IMC):
    mensaje = ""

    if IMC < 16:
        mensaje = "Delgadez Severa"
    elif IMC >= 16 and IMC <= 16.99:
        mensaje = "Delgadez Moderada"
    elif IMC >= 17 and IMC <= 18.49:
        mensaje = "Delgadez Leve"
    elif IMC >= 18.50 and IMC <= 25:
        mensaje = "Normal"
    elif IMC >= 25.01 and IMC <= 29.99:
        mensaje = "Preobeso"
    elif IMC >= 30 and IMC <= 34.99:
        mensaje = "Obesidad Leve"
    elif IMC >= 35 and IMC <= 39.99:
        mensaje = "Obesidad Media"
    else:
        mensaje = "Obesidad Mórbida"

    return mensaje

def reto2():

    """
    Partiendo de la siguiente tabla:

    Clasificación	IMC
    Delgadez Severa	< 16,00
    Delgadez Moderada	16,00 - 16,99
    Delgadez leve	17,00 - 18,49
    Normal	18,50 - 25,00
    Preobeso	25,01 - 29,99
    Obesidad leve	30,00 - 34,99
    Obesidad media	35 - 39,99
    Obesidad mórbida	>= 40

    Devolver el diagnóstico según el imc.
    """
    tipoDatos = input("Escoge una opcion:\n1 - Para IMC, con medidas europeas\n2 - Para IMC, con medidas anglosajonas:\n>")

    if tipoDatos == '1':

        while True:
            try:

                strPeso = input("Introduce tu peso(en kg): ")
                if strPeso[0] == '-' or strPeso[0] == '.':
                    raise ValueError
                peso = float(strPeso)

                strAltura = input("Introduce tu altura(en m): ")
                if strAltura[0] == '-' or strAltura[0] == '.':
                    raise ValueError
                altura = float(strAltura)

                break

            except:
                print("No ha introducido un valor numérico")          

        imc = (peso/altura**2)

        if imc > 18.5:
            print(f"Su IMC es de: {imc:.2f}\nEsta por encima de su peso")
                
        elif imc <= 18.5 and imc >= 15:
            print(f"Su IMC es de: {imc:.2f}\nEsta en su peso")
                
        else:
            print(f"Su IMC es de: {imc:.2f}\nEsta por debajo de su peso")

        mensaje_diagnostico = diagnostico(imc)

        print(f"Diagnostico: {mensaje_diagnostico}")

    if tipoDatos == '2':

        while True:
            try:

                strPeso = input("Introduce tu peso(en lb): ")
                if strPeso[0] == '-' or strPeso[0] == '.':
                    raise ValueError
                peso = float(strPeso)

                strAltura = input("Introduce tu altura(en in): ")
                if strAltura[0] == '-' or strAltura[0] == '.':
                    raise ValueError
                altura = float(strAltura)

                break

            except:
                print("No ha introducido un valor numérico")          

        imc = (peso / (altura**2)) * 703

        if imc > 18.5:
            print(f"Su IMC es de: {imc:.2f}\nEsta por encima de su peso")
                
        elif imc <= 18.5 and imc >= 15:
            print(f"Su IMC es de: {imc:.2f}\nEsta en su peso")
                
        else:
            print(f"Su IMC es de: {imc:.2f}\nEsta por debajo de su peso")

        
        mensaje_diagnostico = diagnostico(imc)

        print(f"Diagnostico: {mensaje_diagnostico}")

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
