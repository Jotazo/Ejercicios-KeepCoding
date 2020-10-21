"""
--- Conversor de temperaturas con funciones ---

Realizar el conversor del ejercicio 17 del módulo 0 con funciones
"""
# --- Funciones ---

def fahrenheit(temperatura):
    f = (temperatura * 9/5) + 32
    return f
def celsius(temperatura):
    c = (temperatura - 32) * 5/9
    return c
def kelvin(temperatura):
    k = temperatura + 273.15
    return k

def pideTemperatura():
    while True:
        strTemperatura = input("Introduzca la temperatura a convertir: ")
        try:
            if strTemperatura[0] == '.':
                raise ValueError
            temperatura = float(strTemperatura)
            break
        except:
            print("No ha escogido opción correcta")

    return temperatura

def devuelveMensaje(tipo, temperatura):
    if tipo.upper() == 'F':
        f = 0.0
        f = fahrenheit(temperatura)
        mensaje = f"{temperatura:.2f}ºC = {f:.2f}ºF"
    elif tipo.upper() == 'C':
        c = 0.0
        c = celsius(temperatura)
        mensaje = f"{temperatura:.2f}ºF = {c:.2f}ºC"
    elif tipo.upper() == 'K':
        k = 0.0
        k = kelvin(temperatura)
        mensaje = f"{temperatura:.2f}ºC = {k:.2f}K"

    return mensaje
# --------------------


temperatura = pideTemperatura()

strTipo = input("Introduzca 'C' para convertir de Fahrenheit a Celsius, 'F' para convertir de Celsius a Fahrenheit y\
    \n'K' para convertir de Celsius a Kelvin: ")

print(devuelveMensaje(strTipo, temperatura))