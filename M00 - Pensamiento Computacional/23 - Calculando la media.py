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
lista_v = []

x = True

while x:

    try:
        n = int(input("Introduzca un valor numérico: "))
        if len(lista_v) == 0 and n == 0:
            raise TypeError
        else:
            if n < 0:
                raise ValueError
            elif n != 0:
                lista_v.append(n)
            else: # Quiere decir que n == 0
                x = False
    except ValueError:
        print("Ha introducido un valor incorrecto")

    except TypeError:
        print("Ha introducido el 0 como primera opción")
        

media = sum(lista_v) / len(lista_v)
print(media)