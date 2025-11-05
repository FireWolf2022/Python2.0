secuencia = input("Ingrese los numeros: ")
new = list(secuencia)


def ceros(*args):
    cont = 0
    confirmacion = False
    for i in args:
        i = int(i)
        if i == 0:
            cont +=1
            if cont == 2:
                confirmacion = True
                break
        else:
            if cont > 0:
                cont-=1

    return confirmacion


print(ceros(*new))
