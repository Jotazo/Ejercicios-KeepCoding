from os import system
from time import sleep


def main():
    """
    ---Concatenando cadenas---

    Crear un programa que pida nombre, verbo, adverbio y adjetivo y con ellos construya una historia. 
    Utilizar una plantilla con los huecos donde colocar el nombre, el verbo, el adverbio y el adjetivo. 
    Eligiendo bien la plantilla la frase puede resultar absurda y hasta graciosa.

    Restricciones:

    Utilizar un solo print en el programa
    Hacer una versión utilizando substitucion

    """

    nombre = input("Introduzca un nombre:\n>")
    verbo = input("Introduzca un verbo:\n>")
    adverbio = input("Introduzca un adverbio:\n>")
    adjetivo = input("Introduzca un adjetivo:\n>")

    while True:
        opcion = input("¿Complicamos un poco mas la historia?(s/n)\n>")
        if opcion.lower() == "s":
            # 1.Introducir más datos para complicar y aumentar la historia
            hora = input("Introduzca una hora:\n>")
            pais = input("Introduzca un país:\n>")
            ciudad = input("Introduzca una ciudad del país introducido:\n>")
            verbo2= input("Introduzca otro verbo:\n>")

            print(f"Bienvenido/a señor/a {nombre}. Ha sido usted seleccionado/a por ser tan {adjetivo}.\
            \n{adverbio} puede usted actuar de esa manera? {verbo} está un poco fuera de su alcance\
            \nUsted llegará a las {hora} a {pais}, exactamente, a la ciudad de {ciudad}. En {ciudad} usted\
            \npodrá {verbo2} tranquilamente con su familia.")
            break
        elif opcion.lower() == "n":
            print(f"Bienvenido/a señor/a {nombre}. Ha sido usted seleccionado/a por ser tan {adjetivo}.\
            \n{adverbio} puede usted actuar de esa manera? {verbo} está fuera de su alcance")
            break
        else:
            print("No ha introducido una opción correcta.")

def reto2():
    # 2.Construye una historia del estilo de los libros de Construye tu propia 
    # aventura de forma que la historia derive según se elija una u otra opción.
    
    while True:
        system('cls')
        print("Te levantas de la cama. La resaca puede con tu cuerpo. La habitación, iluminada por la claridad del sol\
            \nte muestra una mesilla de noche desordenada por toda la locura nocturna.\nNo recuerdas nada de lo ocurrido.\
        \nUna cabellera oscura y rizada, posada sobre la almohada hace que te des cuenta de que\
        \nhay una mujer dentro de tu cama. Que haces?\n")

    
        opcion = input("1 - Decides no hacer nada. Te vuelves a introducir en la cama y seguir durmiendo, a ver si así\
                    \nse te pasa la resaca.\n2 - Decides levantar las sabanas, a ver que tan buena está...\n>")
        if opcion == '1':
            system('cls')
            print("Sigues durmiendo. Las horas pasan y la resaca continúa... Todo te da vueltas. De repente, empiezas a notar\
                   \ncomo algo, al otro lado de la cama, gotea...")
            sleep(5)
            break
        elif opcion == '2':
            system('cls')
            print("Levantas las sabanas con la intención de ver ese cuerpazo en directo. Sorpresa! El cuerpo está ensangrentado\
                \nlleno de cortes y de las sabanas caen gotas de sangre.")
            sleep(5)
            break
        else:
            print("No has escogido una opción correcta.")
            sleep(1.5)

    while True:
        system('cls')

        print("-SANGRE!- Te dices a ti mismo. No entiendes nada, intentas comprender y recordar lo ocurrido la noche anterior, pero\
        \nte es imposible. Es como si te hubieran borrado la memoria. Demasiado alcohol, ya lo sabías que aquella última copa...\
        \nEs lo último que recuerdas. La última copa que tomabas solo. -EXACTO!- Exclamas para tus adentros. -Estaba solo cuando\
        \ntomaba la última.\nNo recuerdas mas, luces, música, mucha gente...\n-TOC TOC- Suena la puerta...\
        \n-Hola? Hay alguien ahi? Anoche se escucharon gritos y era por saber si estaba usted bien.\nQue haces?")

        opcion = input("1 - Te quedas en silencio, a ver si se marchan. A BUENAS HORAS!\
            \n2 - Contestas: - Gracias, todo bien pasé una noche... ejem... ajetreada. Pero todo correcto(FANTASMA!)\n>")
        if opcion == '1':
            system('cls')
            print("- TOC TOC- Vuelven a picar. -Hola?! Conteste si hay alguien, si no llamaré a la policia!")
            sleep(5)
            break
        elif opcion == '2':
            system('cls')
            print("-Uf! Gracias a dios. Estaba bastante preocupado. Podría abrirme la puerta? Vengo de comprar verdura\
                \ndel mercado y le he traido tambien a usted.")
            sleep(5)
            break
        else:
            print("No has escogido una opción correcta.")

    while True:
        system('cls')
        print("Las cosas se ponen feas... Un cuerpo sin vida en la cama... Si no abro la puerta puede que llamen a la policía...\
            \n-Deberia encontrar una solución lo antes posible...\nDecides abrir la puerta, semi desnudo. Detrás de la puerta, un\
            \nhombre, de, mas o menos, 1'90, con una espalda que caben todas tus cosas en ella. Una cicatriz en la cara. Su sonrisa\
            \nse tuerce conforme pasan los segundos. Te das cuenta que ese hombre te suena... Pero no tienes los suficientes\
            \nreflejos como para cerrar la puerta de nuevo antes de que se te abalance. Cae sobre ti una mole de unos 100 kg?\
            \nNotas el crujir de tu espalda, probablemente las 2 primeras vertebras lumbares se te hayan fracturado.\
            \nTe empieza a faltar la respiración. A tu derecha, una pistola, caida de la chaqueta de éste.\
            \nA tu izquierda, un cuchillo de cocina, -Que cojones pinta este cuchillo aqui?-Te dices para ti...\
            \nQue haces?")
        
        opcion = input("1 - Coges la pistola.\n2 - Coges el cuchillo.\n>")
        if opcion == '1':
            system('cls')
            print("Sus manos estan apretando tu cuello. Notas que te falta la respiración. Decides coger la pistola. Con las pocas\
                \nfuerzas que te quedan, apretas el gatillo... Click- Suena...\n-Una pistola descargada?Que mala suerte... Sus manos\
                \napretando tu cuello sin parar, acaban por rebentarte el esternocleidomastoideo, el aire ya no te llega y lo unico\
                \nque notas es que por tu boca corre sangre a borbotones...\nHAS MUERTO!")
            sleep(5)
            print("FIN")
            break
        elif opcion == '2':
            system('cls')
            print("Sus manos estan apretando tu cuello. Notas que te falta la respiración. Decides coger el cuchillo. Y con todas\
                \ntus fuerzas, decides clavarselo en el estomago. Notas como se va introduciendo poco a poco por su piel.\
                \nEmpieza a perder fuerza. Decides sacarlo e introducirlo de nuevo mas profundamente.\nSu cara cambia de repente...\
                \nYa notas como te llega el aire de nuevo, pero de la rabia decides clavarselo una vez mas. Esta vez lo introduces\
                \ncerca del corazón... -Otro muerto mas- Te dices. Lo apartas a un lado y te levantas. TE HAS SALVADO!")
            sleep(5)
            print("FIN")
            break
        else:
            print("No has escogido una opción correcta.")                     
    

reto2()
