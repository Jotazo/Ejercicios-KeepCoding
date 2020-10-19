"""
--- Función es bisiesto ---

Crear una función que como parámetro de entrada tenga un año y devuelva true si es bisiesto y false si no lo es.

Condiciones de bisiesto:
- Cualquier año divisible entre 400 es bisiesto
- De los restantes, cualquier año divisible entre 100 no es bisiesto
- De los restantes cualquier año divisible entre 4 es bisiesto
- Los demás no son bisiesto
"""

def esBisiesto(agno):
    if agno % 400 == 0:
        return True
    elif agno % 400 != 0 and agno % 100 == 0:
        return False
    elif agno % 400 != 0 and agno % 100 != 0 and agno % 4 == 0:
        return True
    else:
        return False

agno = 2016

if esBisiesto(agno):
    print(f"El año {agno} es bisiesto")
else:
    print(f"El año {agno} no es bisiesto")
