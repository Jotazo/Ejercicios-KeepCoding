from tkinter import *

# ----- Funciones -----

def cuentaCaracteres(event):
    numCar = ""
    numCar += cadena.get()
    lblChr['text'] = f"Hay {len(numCar)} carácteres en el entry."


# ----- GUI -----
root = Tk()
root.title("Contando caracteres")
root.geometry("300x100+600+300")
root.resizable(0,0)
root.bind('<Key>', cuentaCaracteres)

cadena = StringVar()
entCadena = Entry(root, width=20, textvariable=cadena)
entCadena.pack(pady=10)

lblChr = Label(root, text="")
lblChr.pack(pady=10)


root.mainloop()
