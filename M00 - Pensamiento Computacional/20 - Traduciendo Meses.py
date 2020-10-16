from time import sleep
from os import system

def inicial():
    """
    --- De número a mes ---

    Hacer un programa que traduzca los números del 1 al 12 a los meses del año. Hacerlo con if - elif.

    Restricciones:

    1.Dejar una única instrucción de salida
    """

    mes = ""
    numMes = input("Introduzca el numero de mes: ")

    if numMes == '1':
        mes = "Enero"
    elif numMes == '2':
        mes = "Febrero"
    elif numMes == '3':
        mes = "Marzo"
    elif numMes == '4':
        mes = "Abril"
    elif numMes == '5':
        mes = "Mayo"
    elif numMes == '6':
        mes = "Junio"
    elif numMes == '7':
        mes = "Julio"
    elif numMes == '8':
        mes = "Agosto"
    elif numMes == '9':
        mes = "Septiembre"
    elif numMes == '10':
        mes = "Octubre"
    elif numMes == '11':
        mes = "Noviembre"
    elif numMes == '12':
        mes = "Diciembre"
    else:
        mes = "ERROR"
        print("No ha escogido una opción correcta")

    print(f"El número {numMes} es el mes de {mes}.")

def reto1():
    # 1.Sustituir la selección con una estructura de datos complejos
    meses = {
        '1':'Enero','2':'Febrero','3':'Marzo','4':'Abril','5':'Mayo','6':'Junio','7':'Julio','8':'Agosto','9':'Septiembre',
        '10':'Octubre','11':'Noviembre','12':'Diciembre',
    }
    mes = ""
    numMes = input("Introduzca el numero de mes: ")
    print(f"El número {numMes} es el mes de {meses[numMes]}.")
def reto2():
    # 2.Hacer el mismo programa en más de un idioma (a elegir por el usuario)
    idiomas = {
        'Español':{
            '1':'Enero','2':'Febrero','3':'Marzo','4':'Abril','5':'Mayo','6':'Junio','7':'Julio','8':'Agosto','9':'Septiembre',
            '10':'Octubre','11':'Noviembre','12':'Diciembre',
        },
        'Ingles':{
            '1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September',
            '10':'October','11':'November','12':'December',
        },
        'Frances':{
            '1':'Janvier','2':'Février','3':'Mars','4':'Avril','5':'Mai','6':'Juin','7':'Juillet','8':'Août','9':'Septembre',
            '10':'Octobre','11':'Novembre','12':'Décembre',
        },
        'Italiano':{
            '1':'Gennaio','2':'Febbraio','3':'Marzo','4':'Aprile','5':'Maggio','6':'Giugno','7':'Luglio','8':'Agosto','9':'Settembre',
            '10':'Ottobre','11':'Novembre','12':'Dicembre',
        }
    }
    mes = ""

    idioma = input("Seleccione un idioma (Español, Ingles, Frances o Italiano): ")
    numMes = input("Introduzca el numero de mes: ")

    print(f"El número {numMes} en {idioma} es el mes de {idiomas[idioma][numMes]}.")
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
