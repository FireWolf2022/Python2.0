from random import shuffle
arreglo = ["-", "--", "---", "----"]

def mezclar(lista):
    shuffle(lista)
    usuario(lista)
    return lista

def usuario(lista):
    intento = ""
    while intento not in [n for n in range(1,4)]:
        try:
            intento = int(input("Ingrese un numero del 1 al 4: "))
        except:
            print("Error")

    comprobacion(lista, intento)
    return intento

def comprobacion(lista, intento):
    if lista[intento -1] == "-":
        print("Mano, a lavar")
    else:
        print("Te salvate")
    print(f"Te toco {lista[intento-1]}")

mezclar(arreglo)