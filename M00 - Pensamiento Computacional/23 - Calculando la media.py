"""
--- Calculando la media ---
Crear un programa que calcule la media de un conjunto de valores introducido por el usuario. 
Si el usuario entra 0 (cero) se considerará el final de la entrada de valores y se procederá a calcular la media.

Restricciones:

1.El cero no se debe incluir en el cálculo de la media
2.Si el primer valor introducido es un cero el programa mostrará un mensaje de error
3.Mantener separadas la entrada, salida y proceso dentro del programa.
4.Si el valor introducido no es numérico volver a pedirlo
"""

valor_total = 0
contador = 0
while True:
        
    try:
        numero = int(input("Introduzca un valor númerico. Si introduce el 0, se dará por finalizado. "))
        if numero == 0 and valor_total == 0:
            raise ValueError
        elif numero == 0:
            break
        valor_total += numero
        contador += 1
    except ValueError:
        print("No ha introducido un valor númerico o ha introducido como primer numero el 0.")

print(f"La media de los números introducidos es: {valor_total/contador}")