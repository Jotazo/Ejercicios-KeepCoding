"""
--- Determinar el precio de un conjunto de entradas al Zoo ---
Hacer un programa que muestre el precio total de las entradas de un grupo de personas al zoo. 
Teniendo en cuenta los siguientes precios:

niños de 2 o menos años: no pagan
Hasta los 12 años: 14 €
Jubilados de 65 o más año: 18€
Resto: 23€.

El programa pedirá la edad de los componentes del grupo, primero pedirá una edad, y sucesivamente las demás. 
En el momento en que se introduzca un 0 se considerará el final y el programa devolverá lo siguiente:

1 entradas de baby (0€):      0.00€
3 entradas de menores (14€): 42.00€
2 entradas normales (23€):   46.00€
1 entradas jubilado (18€):   18.00€
                             ------
                            106.00 €
"""

precios = {
    'niño': 0,
    'joven': 14,
    'adulto': 23,
    'jubilado': 18
}

cantidad_ent = {
    'niño': 0,
    'joven': 0,
    'adulto': 0,
    'jubilado': 0
}

def tipoUsuario(edad):
    if edad <= 2:
        return 'niño'
    elif edad >= 3 and edad <= 12:
        return 'joven'
    elif edad >= 13 and edad <= 64:
        return 'adulto'
    else:
        return 'jubilado'

edad = int(input("Introduzca la edad: "))

while edad != 0:

    usuario = tipoUsuario(edad)
    cantidad_ent[usuario] += 1
    edad = int(input("Introduzca la edad: "))


total_precio_niño = cantidad_ent['niño'] * precios['niño']
total_precio_joven = cantidad_ent['joven'] * precios['joven']
total_precio_adulto = cantidad_ent['adulto'] * precios['adulto']
total_precio_jubilado = cantidad_ent['jubilado'] * precios['jubilado']

precio_total = total_precio_niño + total_precio_joven + total_precio_adulto + total_precio_jubilado

print(f"{cantidad_ent['niño']:>2} entrada de niño      ({precios['niño']}€): {total_precio_niño:6.2f} €\
    \n{cantidad_ent['joven']:>2} entrada de joven    ({precios['joven']}€): {total_precio_joven:6.2f} €\
    \n{cantidad_ent['adulto']:>2} entrada de adulto   ({precios['adulto']}€): {total_precio_adulto:6.2f} €\
    \n{cantidad_ent['jubilado']:>2} entrada de jubilado ({precios['jubilado']}€): {total_precio_jubilado:6.2f} €")

print("\t\t\t\t------")
print(f"\t\t\t      {precio_total:6.2f} €")
