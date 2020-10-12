import getpass
from time import sleep
from os import system

def inicial():
    """
    Validando contraseñas
    Se trata de crear un programa que pida usuario y contraseña y que valide si coinciden.
    En el caso de que lo hagan devolver un mensaje Entró en el sistema y en el contrario No te conozco, no pasas

    Lo interesante de este programa no es sólo la estructura de if necesarias, sino también la estructura de datos
    necesaria para almacenar usuarios y sus contraseñas.

    Restricciones
    Utilizar if/else
    Hacer el programa sensible a mayúsculas - minúsculas
    """

    usuarios = (
        ("pigmonchu", "lolailo1970"),
        ("genaro23", "1234abc$"),
        ("arrumako", "killo.2018"),
    )

    strUser = input("User....: ")
    strPwd =  input("Password: ")
    ix = 0

    while ix < len(usuarios):
        if strUser == usuarios[ix][0] and strPwd == usuarios[ix][1]:
            mensaje = "Entró en el sistema"
            break
        else:
            mensaje = "No te conozco, no pasas"
        ix += 1

    print(mensaje)
        
def reto1():
    # 1.Impide que la contraseña se vea. Investiga para ello
    usuarios = (
        ("pigmonchu", "lolailo1970"),
        ("genaro23", "1234abc$"),
        ("arrumako", "killo.2018"),
    )

    strUser = input("User....: ")
    strPwd =  getpass.getpass("Password: ")
    ix = 0

    while ix < len(usuarios):
        if strUser == usuarios[ix][0] and strPwd == usuarios[ix][1]:
            mensaje = "Entró en el sistema"
            break
        else:
            mensaje = "No te conozco, no pasas"
        ix += 1

    print(mensaje)

def reto2():
    # 2.Utiliza un diccionario en lugar de una tupla de tuplas
    usuarios = {
        "pigmonchu":"lolailo1970",
        "genaro23":"1234abc$",
        "arrumako":"killo.2018"
        }

    strUser = input("User....: ")
    strPwd = input("Password: ")

    if strUser in usuarios and usuarios[strUser] == strPwd:
        print("Entró en el sistema")
    else:
        print("No te conozco, no pasas")

def main():
    while True:

        system('cls')
        opcion = input("Elige una opción:\n1 - Programa normal\n2 - Reto 1\n3 - Reto 2\n>")

        if opcion == "1":
            print("Ha elegido Programa normal")
            sleep(1.0)
            system('cls')
            inicial()
            break
        elif opcion == "2":
            print("Ha elegido Reto 1")
            sleep(1.0)
            system('cls')
            reto1()
            break
        elif opcion == "3":
            print("Ha elegido Reto 2")
            sleep(1.0)
            system('cls')
            reto2()
            break
        else:
            print("No ha escogido opción correcta")
            sleep(1.0)
            system('cls')

main()
