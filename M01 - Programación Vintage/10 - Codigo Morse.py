from misModulos.screen import locate, clear
from os import system

"""
--- Escribir un programa que traduzca a código Morse ---

Utilizando un diccionario y el control de la pantalla desarrollado en screen. Escribir un programa que traduzca a Morse.

Restricciones:

1.El programa pedira una línea de texto y la traducirá a morse.
2.El programa seguirá pidiendo líneas hasta que se introduzca una cadena vacía. Entonces dejará de pedir lineas
3.El formato de salida debe ser tal que: 
     - Se impriman tantas líneas como se han introducido
     - No se imprima nada entre las líneas (controlar la posición del input)

| Carácter | Código | Carácter | Código | Carácter | Código | |---|---|---|---| |A|· —|N|— ·|0|— — — — —|| |B|— · · ·
|Ñ|— — · — —|1|· — — — —|| |C|— · — ·|O|— — —|2|· · — — —|| |CH|— — — —|P|· — — ·|3|· · · — —|| |D|— · ·|Q|— — · —
|4|· · · · —|| |E|·|R|· — ·|5|· · · · ·|| |F|· · — ·|S|· · ·|6|— · · · ·|| |G|— — ·|T|—|7|— — · · ·|| 
|H|· · · ·|U|· · —|8|— — — · ·|| |I|· ·|V|· · · —|9|— — — — ·|| |J|· — — —|W|· — —|.|· — · — · —|| 
|K|— · —|X|— · · —|,|— · — · — —|| |L|· — · ·|Y|— · — —|?|· · — — · ·|| |M|— —|Z|— — · ·|"|· — · · — · |!|— — · · — —||||||
"""

morse = {
    'A': '._',
    'B': '_...',
    'C': '_._.',
    'D': '_..',
    'E': '_.',
    'F': '.._.',
    'G': '_ _.',
    'H': '....',
    'I': '..',
    'J': '._ _ _',
    'K': '_._',
    'L': '._..',
    'M': '_ _',
    'N': '_.',
    'O': '_ _ _',
    'P': '._ _.',
    'Q': '_ _ ._',
    'R': '._.',
    'S': '...',
    'T': '_',
    'U': '.._',
    'V': '..._',
    'W': '._ _',
    'X': '_.._',
    'Y': '_._ _',
    'Z': '_ _..',
    '0': '_ _ _ _ _',
    '1': '._ _ _ _',
    '2': '.._ _ _',
    '3': '..._ _',
    '4': '...._',
    '5': '.....',
    '6': '_....',
    '7': '_ _...',
    '8': '_ _ _..',
    '9': '_ _ _ _.',
}

system('cls')
locate(8,0)
cadena = input("Introduzca una cadena de texto: ")

cadena_morse = ""
cadenaImprimir = ""

while cadena != "":

    #columna = 0
    
    for letra in cadena:
        if letra not in morse:
            barra = '|'
            letra_a_introducir = letra
            cadena_morse += barra + letra_a_introducir + barra 
        else:
            barra = '|'
            letra_a_introducir = letra
            morse_de_letra = morse[letra]
            cadena_morse += barra + letra_a_introducir + barra + morse_de_letra

    cadenaImprimir += cadena_morse
    clear()
    locate(0,0)
    print(cadenaImprimir)
    cadena_morse = ""
    locate(8,0)
    cadena = input("Introduzca una cadena de texto: ")
    