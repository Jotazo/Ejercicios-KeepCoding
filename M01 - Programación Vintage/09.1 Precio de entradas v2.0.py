from misModulos.screen import *

import subprocess
subprocess.call('', shell=True)

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

total_entradas_nino = 0
total_entradas_joven = 0
total_entradas_adulto = 0
total_entradas_jubilado = 0

precio_total = 0

def tipoUsuario(edad):
    if edad <= 2:
        return 'niño'
    elif edad >= 3 and edad <= 12:
        return 'joven'
    elif edad >= 13 and edad <= 64:
        return 'adulto'
    else:
        return 'jubilado'

def actualizaPrecios():
    global total_entradas_nino
    global total_entradas_joven
    global total_entradas_adulto
    global total_entradas_jubilado
    global precio_total

    total_entradas_nino = cantidad_ent['niño'] * precios['niño']
    total_entradas_joven = cantidad_ent['joven'] * precios['joven']
    total_entradas_adulto = cantidad_ent['adulto'] * precios['adulto']
    total_entradas_jubilado = cantidad_ent['jubilado'] * precios['jubilado']

    precio_total = total_entradas_nino + total_entradas_joven + total_entradas_adulto + total_entradas_jubilado 

def dibujaPrecios():
    locate(4,1)
    print(f"{cantidad_ent['niño']:>2} entrada de niño      ({precios['niño']}€): {total_entradas_nino:6.2f} €")
    locate(5,1)
    print(f"{cantidad_ent['joven']:>2} entrada de joven    ({precios['joven']}€): {total_entradas_joven:6.2f} €")
    locate(6,1)
    print(f"{cantidad_ent['adulto']:>2} entrada de adulto   ({precios['adulto']}€): {total_entradas_adulto:6.2f} €")
    locate(7,1)
    print(f"{cantidad_ent['jubilado']:>2} entrada de jubilado ({precios['jubilado']}€): {total_entradas_jubilado:6.2f} €")
    locate(9,1)
    print("\t\t\t\t------")
    locate(10,1)
    print(f"\t\t\t      {precio_total:6.2f} €")

clear()
edad = None

while edad != 0:

    actualizaPrecios()
    dibujaPrecios()
    locate(1,1)
    edad = int(input("Introduzca la edad: "))
    usuario = tipoUsuario(edad)
    cantidad_ent[usuario] += 1
    
    locate(1,1)
    clearLine()



