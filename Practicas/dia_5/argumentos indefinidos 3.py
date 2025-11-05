def numeros_persona(nombre, *args):
    suma = sum(args)
    return f"{nombre} la suma de tus numeros es {suma}"
print(numeros_persona("Leonel",4,5))
