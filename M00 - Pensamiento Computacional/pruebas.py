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
    