from random import *
print("Bienvenido a Adivina el numero")
numero = 0
win = False
while not win:
    print("Tiene un maximo de 8 intentos para intentar averiguar el numero")
    aleatorio = randint(0,100)
    for i in range(8):
        numero = int(input(f"Ingrese un numero entero positivo de 0-100, # indento: {i+1}: "))
        if numero < 0 or numero > 100:
            print("El numero debe estar entre 0 y 100")
        elif numero < aleatorio:
            print("Estas por debajo :(")
        elif numero > aleatorio:
            print("Estas por arriba :(")
        elif numero == aleatorio:
            print(f"Felicidades! Acertaste! Has ganado, la respuesta correcta era {aleatorio}, te ha tomado {i+1} intento")
            win = True
            break

    if not win:
        print(f"Has fallado todos los intentos, la respuesta correcta era {aleatorio}")