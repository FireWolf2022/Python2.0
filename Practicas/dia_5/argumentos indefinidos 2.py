def suma_absolutos(*args):
    suma = 0
    for i in args:
        suma+= abs(i)
    return suma

print(suma_absolutos(3,4,-3))
