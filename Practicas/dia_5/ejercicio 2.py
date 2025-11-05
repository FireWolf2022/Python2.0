palabra = input("Ingrese la palabra: ")

def deletrear(pal):
    new = set()
    for letra in pal:
        new.add(letra)
    new = list(new)
    new.sort()
    print(new)

deletrear(palabra)