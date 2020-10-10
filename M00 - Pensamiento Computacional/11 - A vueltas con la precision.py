def inicial():
    """
    --- Conversión de divisas ---

    Crear un programa que pase de dolares a euros. El programa pedirá la tasa de cambio de dolares a euros\
    (cuantos euros se necesitan para tener un dolar). El programa debe devolver lo siguiente

    X dolares a una tasa de cambio de Y

    Total €

    Restricciones:

    1.Asegúrate de que la entrada se redondea al centavo
    2.Utiliza una única sentencia de salida
    """

    tasa_cambio = float(input("Introduce la tasa de cambio de $(dólar) a €(Euro): "))
    cantidad_dolares = float(input("Introduce los dólares a convertir: "))

    dolar_a_euro = tasa_cambio * cantidad_dolares

    print(f"{cantidad_dolares} dólares a una tasa de cambio de {tasa_cambio} €\nTotal: {dolar_a_euro} €")

def reto1():
    # 1.Crea un diccionario de tasas de conversión y pregunta por paises, no por monedas.
    tasas_de_conversion = {
        'Estados Unidos':0.85,
        'Japon':0.008,
        'Canada':0.64,
        'Reino Unido':1.10,
        'Turquia':0.11,
        'Argentina':0.011,
        'Cuba':0.86,
        'Mejico':0.040,
        'India':0.012,
        'China':0.13
    }

    pais = input("Introduzca el país del que quiere convertir la moneda a €(EURO): ")

    if pais.title() not in tasas_de_conversion.keys():
        print("Ese país no se encuentra, introduzca otro por favor...")
    else:
        cantidad = float(input("Introduzca la cantidad de moneda a convertir: "))

        total_convertido = cantidad * tasas_de_conversion[pais.title()]

        print(f"{cantidad} monedas de {pais.title()} a € son: {total_convertido:.2f} €")

reto1()