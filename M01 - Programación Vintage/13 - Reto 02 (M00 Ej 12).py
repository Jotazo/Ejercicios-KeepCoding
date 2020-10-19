"""
--- Cálculo de interés simple con funciones ---

Crear una función CalculateSimpleInterest(Amount, tax, years) que devuelva el valor de la inversión transcurrido el tiempo indicado.

Crearla como módulo y modicar el ejercicio 12 del módulo 00 para usar la función primero y el módulo después
"""

def CalculateSimpleInteres(amount, tax, years):

    A = amount * (1 + tax * years)

    return A