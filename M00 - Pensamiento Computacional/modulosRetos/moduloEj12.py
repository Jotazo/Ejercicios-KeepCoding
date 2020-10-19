"""
--- Cálculo de interés simple con funciones ---

Crear una función CalculateSimpleInterest(Amount, tax, years) que devuelva el valor de la inversión transcurrido el tiempo indicado.

Crearla como módulo y modicar el ejercicio 12 del módulo 00 para usar la función primero y el módulo después
"""

def CalculateSimpleInteres(amount, tax, years):

    A = amount * (1 + tax * years)

    return A

if __name__ == "__main__":
    
    strCapital = input("Cantidad invertida: ")
    strAnnos = input("Años Transcurridos: ")
    strInteres = input("Interés anual: ")

    P = round(float(strCapital),2)
    r = float(strInteres)/100
    t = float(strAnnos)

    A = CalculateSimpleInteres(P, r, t)

    print(f"Tras {int(t)} de inversión al {r*100:.2f}%, su cantidad debe ser {A:.2f}€")