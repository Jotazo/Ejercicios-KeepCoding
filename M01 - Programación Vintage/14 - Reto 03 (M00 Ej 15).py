import bcrypt
"""
--- Encriptando contraseñas ---

Hacer el mismo programa que el ejercicio 15 del módulo 0 utilizando un diccionario y encriptando la contraseña con bcrypt
"""

usuarios = {
        "pigmonchu":"lolailo1970",
        "genaro23":"1234abc$",
        "arrumako":"killo.2018"
        }

sal = bcrypt.gensalt() # sal?

strUser = input("User....: ")
strPwd = input("Password: ")

bytePwd = strPwd.encode() # Contraseña en bytes, encriptada
pwd_hashed = bcrypt.hashpw(bytePwd, sal) # Contraseña con sal(encriptada)

encontrado = False

for usuario in usuarios:
    if strUser == usuario:

        bytePwd1 = usuarios[strUser].encode()
        pwd1_hashed = bcrypt.hashpw(bytePwd1, sal)

        if bcrypt.checkpw(bytePwd, pwd1_hashed):

            print("Ok, las contraseñas coinciden")
            encontrado = True
            
if not encontrado:
    print("Usuario y/o contraseña incorrecto")

