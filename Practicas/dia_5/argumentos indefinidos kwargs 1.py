def cantidad_atributos(**kwargs):
    cant = 0
    for i in kwargs.items():
        cant +=1
    return cant

print(cantidad_atributos(x = 1, y = 2, z = 3))