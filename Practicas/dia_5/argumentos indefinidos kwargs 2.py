def lista_atributos(**kwargs):
    lista = []
    for b in kwargs.values():
        lista.append(b)
    return lista

print(lista_atributos(x=1, y=4, z=3))