def inicial():
    """

    --- Solucionando problemas del coche ---

    Hacer un programa que siga el siguiente arbol de decisiones para dar con el diagnóstico del problema de nuestro coche.

    Restricciones:
    1.Realiza las preguntas relevantes según las respuestas del usuario
    
    """

    opcion = input("¿Arranca?: ")
    if opcion == 'S':
        opcion = input("¿Suena un clic-clic?: ")
        if opcion == 'S':
            print("Reemplaza la batería")
        else:
            opcion = input("¿Se enciende del coche pero no arranca?: ")
            if opcion == 'S':
                print("Revisa las bujías")
            else:
                opcion = input("¿Arranca el coche y luego se cala?: ")
                if opcion == 'S':
                    opcion = input("¿Tiene el coche inyección de combustible?: ")
                    if opcion == 'S':
                        print("Lleve el coche al taller")
                    else:
                        print("Abre y cierra el starter")
    else:
        opcion = input("¿Están los bornes de la batería corroídos?: ")
        if opcion == 'S':
            print("Limpia los bornes y arranca de nuevo.")
        else:
            print("Reemplaza los cables y arranca de nuevo.")

def reto1():

    # 1.Investigar sobre árboles de decisión y como codificarlo sin hacerlo a capón como arriba
    pass

inicial()