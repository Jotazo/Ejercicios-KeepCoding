"""
--- Función que traduzca números a ordinal ---

Crear una función que tenga como parámetro un número entero y que si este está entre el 1 y el 12 (incluidos)
devuelva como resultado su ordinal, es decir, 'primero', 'segundo',... 'duodécimo', en cualquier otro caso debe
devolver una cadena vacía.

Restricciones:

1.Crear el programa como un módulo. De forma que si se ejecuta como main muestre la tabla de las doce traducciones
2.La tabla de las doce traducciones debe estar perfectamente alineada.

"""

numeros = {
    1:'Primero',
    2:'Segundo',
    3:'Tercero',
    4:'Cuarto',
    5:'Quinto',
    6:'Sexto',
    7:'Séptimo',
    8:'Octavo',
    9:'Noveno',
    10:'Décimo',
    11:'Onceavo',
    12:'Doceavo'
}

def numero_a_ordinal(num):
    if num in numeros:
        print(f"{num:>2} - {numeros[num]:<8}")
    else:
        print(" ")

if __name__ == "__main__":

    for i in range(1,13):
        numero_a_ordinal(i)