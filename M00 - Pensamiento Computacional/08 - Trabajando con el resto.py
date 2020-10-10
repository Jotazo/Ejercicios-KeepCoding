from math import ceil
from time import sleep
from os import system

def inicial():
    """
    ---Repartiendo pizza---

    Escribir un programa que sabiendo cuantas personas hay en una reunión y cuantas pizzas se han comprado,\
    queriendo que cada persona tenga una porción de cada pizza. La pizza sólo puede dividirse en un número par de porciones

    ¿Número de personas? 7
    ¿Número de pizzas? 3
    
    7 personas con 3 pizzas
    Cada persona toma 3 piezas
    Sobran 3 porciones
    """
    personas = int(input("¿Número de personas?\n>"))
    pizzas = int(input("¿Número de pizzas?\n>"))

    trozos_pizza = pizzas * 8
    pizza_por_persona = int(trozos_pizza / personas)
    pizza_sobrante = int(trozos_pizza % personas)

    print(f"{personas} personas con {pizzas} pizzas\nCada persona toma {pizza_por_persona} piezas\
        \nSobran {pizza_sobrante} porciones")

def reto1():
    # 1.Asegurar que la entrada es numerica, positiva y entera. En otro caso impedir que el usuario continue
    while True:
        try:
            personas = int(input("¿Número de personas?\n>"))
            if personas <= 0:
                raise ValueError
            pizzas = int(input("¿Número de pizzas?\n>"))
            if pizzas <= 0:
                raise ValueError
            break
        except:
            print("No ha introducido un valor numérico entero, es negativo o ha introducido 0")

    trozos_pizza = pizzas * 8
    pizza_por_persona = int(trozos_pizza / personas)
    pizza_sobrante = int(trozos_pizza % personas)

    print(f"{personas} personas con {pizzas} pizzas\nCada persona toma {pizza_por_persona} piezas\
        \nSobran {pizza_sobrante} porciones")

def reto2():

    # 2.Escribir los mensajes de salida con formato singular/plural adecuado
    
    while True:
        try:
            personas = int(input("¿Número de personas?\n>"))
            if personas <= 0:
                raise ValueError
            pizzas = int(input("¿Número de pizzas?\n>"))
            if pizzas <= 0:
                raise ValueError
            break
        except:
            print("No ha introducido un valor numérico entero, es negativo o ha introducido 0")

    strPersonas = ""
    strPizzas = ""
    strPiezas = ""
    strPorciones = ""

    trozos_pizza = pizzas * 8
    pizza_por_persona = int(trozos_pizza / personas)
    pizza_sobrante = int(trozos_pizza % personas)

    if personas == 1:
        strPersonas = "persona"
    else:
        strPersonas = "personas"
    
    if pizzas == 1:
        strPizzas = "pizza"
    else:
        strPizzas = "pizzas"

    if pizza_por_persona == 1:
        strPiezas = "pieza"
    else:
        strPiezas = "piezas"

    if pizza_sobrante == 1:
        strPorciones = "porción"
    else:
        strPorciones = "porciones"

    print(f"{personas} {strPersonas} con {pizzas} {strPizzas}\nCada persona toma {pizza_por_persona} {strPiezas}\
        \nSobran {pizza_sobrante} {strPorciones}")

def reto3():
    # 3.Crear un programa que diga cuantas pizzas hay que comprar preguntando personas y porciones de pizza que quieren tomar.
    # Recuerda que las pizzas siempre se dividen en un número par de porciones

    while True:
        try:
            personas = int(input("¿Número de personas?\n>"))
            if personas <= 0:
                raise ValueError
            porciones = int(input("¿Cuantas porciones tomará cada uno?\n>"))
            if porciones <= 0:
                raise ValueError
            break
        except:
            print("No ha introducido un valor numérico entero, es negativo o ha introducido 0")

    total_porciones = personas * porciones
    pizza = 8
    total_pizzas = ceil(total_porciones / pizza)

    print(f"Para {personas} personas, comiendo cada una {porciones} porciones, hay que comprar {total_pizzas} pizzas")

def main():
    while True:

        system('cls')
        opcion = input("Elige una opción:\n1 - Programa normal\n2 - Reto 1\n3 - Reto 2\n4 - Reto 3\n>")

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
        elif opcion == "4":
            print("Ha elegido Reto 3")
            sleep(1.0)
            system('cls')
            reto3()
            break
        else:
            print("No ha escogido opción correcta")
            sleep(1.0)
            system('cls')    

main()