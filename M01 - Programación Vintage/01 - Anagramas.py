"""
--- Anagramas ---
Crear un programa que indique si una cadena es un anagrama de otra (mismos carácteres en orden diferente). Ejemplo

Primera cadena: otra
Segunda cadena: rota
    
"otra" y "rota" son anagramas

Restricciones:

1.Hacerlo con la función esAnagrama
2.Ambas palabras deben tener la misma longitud

Retos:

# 1.Hacerlo sin las facilidades de manejo de cadenas de python
"""

def esAnagrama(p1, p2):
    mensaje = ""

    longitud = len(p1)
    contador = 0
    
    for letra in p1:
        if letra in p2:
            contador += 1

    if contador == longitud:
        mensaje = f"{p1} y {p2} son anagramas"
    else:
        mensaje = f"{p1} y {p2} no son anagramas"

    return mensaje

print(esAnagrama('vatrocinio', 'travocinio'))
