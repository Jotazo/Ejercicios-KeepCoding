"""
--- IVA general por paises ---
Según el pais se aplica un tipo general de IVA u otro. Haz un programa que aplique el tipo de iva adecuado según el pais de origen

Seguir la siguiente tabla. El programa debe mostrar la base, el iva aplicado en % y en € y el precio final.

Hungria = 27 %
Croacia, Dinamarca y Suecia = 25%
Finlancia y Rumania = 24 %
Grecia, Irlanda, Polonia y Portugal = 23 %
Eslovenia e Italia = 22
España, Belgica, Letonia, Lituania, Paises Bajos y Republica Checa = 21%
Austria, Bulgaria, Eslovaquia, Estonia, Francia y Reino Unido = 20 %
Alemania y Chipre = 19%
Malta = 18%
Luxemburgo = 15%

Restricciones:

1.Las cantidades en € deben aparecer ajustadas al céntimo
2.Utilizar una sola instrucción de impresión de resultados
"""
paises_IVA = {
    'Hungria': 27,
    'Croacia': 25, 'Dinamarca': 25, 'Suecia': 25,
    'Finlandia': 24, 'Rumania': 24,
    'Grecia': 23, 'Irlanda': 23, 'Polonia': 23, 'Portugal': 23,
    'Eslovenia': 22, 'Italia': 22,
    'España': 21, 'Belgica': 21, 'Letonia': 21, 'Lituania': 21, 'Paises Bajos': 21, 'Republica Checa': 21,
    'Austria': 20, 'Bulgaria': 20, 'Eslovaquia': 20, 'Estonia': 20, 'Francia': 20, 'Reino Unido': 20,
    'Alemania': 19, 'Chipre': 19,
    'Malta': 18,
    'Luxemburgo': 15
}

strPrecio_producto = input("Introduzca el precio del producto: ")
pais = input("Introduzca el país del que proviene el producto: ")

precio_producto = float(strPrecio_producto)

iva_euros = precio_producto*(paises_IVA[pais]/100)

precio_total = precio_producto + iva_euros

print(f"Precio producto:    {precio_producto:6.2f} €\nIVA aplicado({paises_IVA[pais]}%):  {iva_euros:6.2f} €\
    \nPrecio total: \t    {precio_total:6.2f} €")


