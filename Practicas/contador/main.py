obj = {
    1:0,
    5:0,
    10:0,
    20:0,
    50:0,
    100:0,
    200:0,
    500:0,
    1000:0
}

def main():
    print("Bienvenido, a continuacion va a tener dos opciones, agregar (en el caso de que no halla se crea uno nuevo) editar (se sumara)")
    while True:
        op = input("1-Agregar\n2-Editar (sumar) \n$- ")
        op = int(op)
        try:
            op = int(op)
        except ValueError:
            print("Debe elegir una opcion valida")


if __name__ == __name__:
    main()
