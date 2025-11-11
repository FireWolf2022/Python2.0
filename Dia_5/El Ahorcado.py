from random import *

def palabra_random():
    lista_random = ["mesa", "silla", "laptop", "ventana", "arbol", "departamento", "edificio", "docente", "ingenieria", "armario", "taquilla", "zapatilla", "tendedera", "arrocera", "telefono", "audifonos"]
    return choice(lista_random)

def principal():
    vitalidad = 6
    palabra = palabra_random()
    usuario = ["_"] * len(palabra)
    print("".join(usuario))
    letras_introducidas = set()
    while True:
        if vitalidad >=1:
            letra = input("Ingrese la letra... : ").lower()
            if letra not in letras_introducidas:
                letras_introducidas.add(letra)
            else:
                print("Ya intento con esta letra")
                print("".join(usuario))
                continue

            if is_alpha(letra):
                lista,vitalidad = letra_en_palabra(letra, palabra, usuario,vitalidad)
                print(f"{"".join(usuario)} | vidas restantes: {vitalidad}")

                if "".join(usuario).isalpha():
                    print("Has ganadooooo!!!!!")
                    print(f"Respusta: {"".join(usuario)}")
                    break
            else:
                print("Lo que ingreso no fue una letra")
        else:
            print("Te has quedado sin intentos :'(")
            print("GAME OVER!!!!")
            print(f"La palabra correcta era :{"".join(palabra)}")
            break



def letra_en_palabra(l,palabra,usuario,vitalidad):
    if l in "".join(palabra):
        if len(l) == 1:
            for i, e in enumerate(palabra):
                if l == e:
                    usuario[i] = e
            else:
                return usuario, vitalidad
        elif len(l) == len(palabra):
            for letra in l:
                for i,e in enumerate(palabra):
                    if letra == e:
                        usuario[i] = e
            else:
                return usuario, vitalidad
        else:
            print("Solo puede intentar adivinar una letra, o la palabra completa, !No fragmentos¡")

    else:
        if len(l) != 1 & len(l) != len(palabra):
            print("No puede introducir varias letras, a menos que intente adivinar la palabra completa!!")
            return usuario, vitalidad
        else:
            print("Letra o palabra incorrecta!!")
    return usuario, vida(vitalidad)


def is_alpha(l):
    if l.isalpha():
        return True

    return False

def vida(n):
    n -=1
    return n

principal()
