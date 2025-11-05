def suma_cuadrado(*num):
    resul = 0
    for i in num:
        resul += i**2
    return resul
print(suma_cuadrado(2,2,5))