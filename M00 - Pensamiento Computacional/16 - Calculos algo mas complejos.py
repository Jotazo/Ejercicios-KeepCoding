
# --- Funciones que nos devuelven, gramos reales, UBE, 
# alcoholemia inmediata y alcoholemia real

def gramos_reales(volumen, graduacion, cantidad):

    A = (volumen * graduacion * 0.8) / 100

    return A*cantidad

def transforma_a_UBE(gramos_reales):

    return gramos_reales / 10

def alcoholemia_inmediata(UBE):

    ai = UBE * 0.3

    return ai

def alcoholemia_real(ai, horas):

    aR = ai - 0.15 * horas

    return aR

# ---

bebidas = []
datos_bebidas = []

while True:

    try:

        strNumBebidas = input("\nNumero de bebidas: ")
        if strNumBebidas[0] == '-' or strNumBebidas[0] == '.':
            raise ValueError
        numBebidas = int(strNumBebidas)

        strVolumen = input("Volumen tomado en cc: ")
        if strVolumen[0] == '-' or strVolumen[0] == '.':
            raise ValueError
        volumen = int (strVolumen)

        strGradoAlcoholico = input("Grado alcoholico: ")
        if strGradoAlcoholico[0] == '-' or strGradoAlcoholico[0] == '.':
            raise ValueError
        gradoAlcoholico = int(strGradoAlcoholico)

        datos_bebidas.append(numBebidas)
        datos_bebidas.append(volumen)
        datos_bebidas.append(gradoAlcoholico)

        bebidas.append(datos_bebidas)

        datos_bebidas = []

        opcion = input("\nOtra bebida(S/N): ")

        if opcion.upper() == 'N':
            break

    except:
        print("No ha introducido un valor numérico")

while True:
    try:
        strTiempoTrans = input("\nHoras Transcurridas: ")
        if strTiempoTrans[0] == '-' or strTiempoTrans[0] == '.':
            raise ValueError
        tiempoTrans = int(strTiempoTrans)
        break
    except:
        print("No ha introducido un valor numérico")

total_gr = 0

for i in range(len(bebidas)): # Calculamos el total de alcohol ingerido
    total_gr += gramos_reales(bebidas[i][1], bebidas[i][2], bebidas[i][0])

UBE = transforma_a_UBE(total_gr) # Transformamos el total a UBE

ai = alcoholemia_inmediata(UBE) # Calculamos la alcoholemia inmediata

alcohol_real = alcoholemia_real(ai, tiempoTrans) # Calculamos el alcohol real

max_alcohol = 0.5

print(f"\nAlcohol en sangre : {alcohol_real:.2f} g/l")

print(f"\nEl máximo permitido es {max_alcohol} g/l.")

if alcohol_real > max_alcohol:
    print("Usted no puede conducir")
else:
    print("Usted puede conducir")
