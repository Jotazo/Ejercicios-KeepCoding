def inicial():
    """
    --- Calculando el interés compuesto ---

    Introduciremos aquí los exponentes. En préstamos o inversiones a largo plazo se suele utilizar más el interes compuesto que el simple \
    (diferencias entre ambos).Se trata ahora de escribir un programa que calcule el interés compuesto sobre un capital a lo largo del tiempo.

    El programa ha de pedir el capital inicial, el interes anual, el número de años de la inversión y el número de veces que se calcula\
    en interés en el año. La fórmula a aplicar es:

    A=P(1+rn)nt

    donde

    P es el capital inicial
    r el interes anual
    t los años que dura la inversión (o préstamo)
    n el número de veces que se acumula el interés por año (por ejemplo 12 si es mensual)
    A es la cantidad al final de la inversión,
    Así, para:

    1500 € de capital inicial
    4,3% de interes
    6 años de duración del préstamo
    Se calcula el interés al trimestre (4 periodos por año)
    El programa debería devolver

    1500.00 € invertidos al 4.3% durante 6 años con 4 periodos de imposición por año se transforman en 1938.84 €

    Restricciones:

    1.El interés se introduce como % no como tanto por uno (15 en lugar de 0.15)
    2.Asegurar que las cantidades en euros estén ajustadas al céntimo
    A=P(1+rn)nt
   
    """
    strCapital = input("Introduzca el capital inicial: ")
    strAnnos = input("Introduzca los años de inversión: ")
    strInteres = input("Introduzca el interés anual: ")
    strInteresAcumulado = input("Introduzca la acumulación de interés por año: ")

    P = round(float(strCapital),2)
    t = int(strAnnos)
    r = float(strInteres)/100
    n = int(strInteresAcumulado)

    A = P * (1 + r / n)**(n*t)

    print(f"{P:.2f} € invertidos al {r*100}% durante {t} años con {n} periodos de imposición por año se transforman en {A:.2f} €")

def reto1():
    # 1.Impedir que el usuario siga con el proceso si no introduce valores numéricos correctos
    while True:
        try:
            strCapital = input("Introduzca el capital inicial: ")
            if strCapital[0] == '-' or strCapital[0] == '.':
                raise ValueError
            P = round(float(strCapital),2)
            
            strAnnos = input("Introduzca los años de inversión: ")
            if strAnnos[0] == '-' or strAnnos[0] == '.':
                raise ValueError
            t = int(strAnnos)
            
            strInteres = input("Introduzca el interés anual: ")
            if strInteres[0] == '-' or strInteres[0] == '.':
                raise ValueError
            r = float(strInteres)/100

            strInteresAcumulado = input("Introduzca la acumulación de interés por año: ")
            if strInteresAcumulado[0] == '-' or strInteresAcumulado[0] == '.':
                raise ValueError
            n = int(strInteresAcumulado)

            break
        except:
            print("No ha introducido un valor numérico correcto")
    
    A = P * (1 + r / n)**(n*t)

    print(f"{P:.2f} € invertidos al {r*100}% durante {t} años con {n} periodos de imposición por año se transforman en {A:.2f} €")
def reto2():
    # 2.Hacer una versión del programa que actúe al revés. Conociendo el tipo de interés, los años\
    # y periodos de imposición y sabiendo que suma total se quiere conseguir el programa debe indicar el capital inicial a invertir
    while True:
        try:
            strTotal = input("Introduzca el total a conseguir: ")
            if strTotal[0] == '-' or strTotal[0] == '.':
                raise ValueError
            A = round(float(strTotal),2)
            
            strAnnos = input("Introduzca los años de inversión: ")
            if strAnnos[0] == '-' or strAnnos[0] == '.':
                raise ValueError
            t = int(strAnnos)
            
            strInteres = input("Introduzca el interés anual: ")
            if strInteres[0] == '-' or strInteres[0] == '.':
                raise ValueError
            r = float(strInteres)/100

            strInteresAcumulado = input("Introduzca la acumulación de interés por año: ")
            if strInteresAcumulado[0] == '-' or strInteresAcumulado[0] == '.':
                raise ValueError
            n = int(strInteresAcumulado)
            
            break
        except:
            print("No ha introducido un valor numérico correcto")
    
    P = A / (1 + r / n)**(n*t)

    print(f"Para conseguir {A:.2f} € en {t} años a un interés de {r*100}% con una acumulación de {n} por año se debe invertir {P:.2f} ")

reto2()