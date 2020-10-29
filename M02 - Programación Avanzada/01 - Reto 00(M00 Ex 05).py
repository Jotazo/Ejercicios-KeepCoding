from tkinter import *

from tkinter import messagebox

# ----- Funciones -----

def suma(n1, n2):
    return n1 + n2
def resta(n1, n2):
    return n1 - n2
def multiplicacion(n1, n2): 
    return n1 * n2
def division(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return 0

def muestraResultados(n1, n2, listaResul):
    
    resultados.config(state=NORMAL)
    resultados.delete("1.0", END)
    mensaje = f"\t {n1:>4} + {n2:>4} = {listaResul[0]:>10.2f}\
              \n\t {n1:>4} - {n2:>4} = {listaResul[1]:>10.2f}\
              \n\t {n1:>4} * {n2:>4} = {listaResul[2]:>10.2f}\
              \n\t {n1:>4} / {n2:>4} = {listaResul[3]:>10.2f}"
    resultados.insert("1.0", mensaje)
    resultados.config(state=DISABLED)

def calcular():
    
    num1Int = inputInt(num1.get(), entryNum1)
    num2Int = inputInt(num2.get(), entryNum2)

    res1 = suma(num1Int, num2Int)
    res2 = resta(num1Int, num2Int)
    res3 = multiplicacion(num1Int, num2Int)
    res4 = division(num1Int, num2Int)

    resultados = [res1, res2, res3, res4]

    muestraResultados(num1Int, num2Int, resultados)

def inputInt(n, enInc):
    try:
        if n == "":
            num = 0
        else:
            num = int(n)
        return num 
    except:
        messagebox.showerror("Error", "No se ha introducido un valor numérico.")
        enInc.delete(0, END)
        return 0

root = Tk()
root.geometry("350x350+500+250")
root.title("Operaciones Matemáticas")
root.resizable(0,0)

num1 = StringVar()
entryNum1 = Entry(root, width=10, textvariable=num1)
entryNum1.pack(side=TOP, pady=10, padx=5)
num2 = StringVar()
entryNum2 = Entry(root, width=10, textvariable=num2)
entryNum2.pack(side=TOP, pady=5, padx=5)

btnCalcular = Button(root, text="Calcular", width=10, command=calcular)
btnCalcular.pack(side=TOP, pady=10, padx=5)

resultados = Text(root, width=40, height=10, state=DISABLED)
resultados.pack(pady=15)

root.mainloop()