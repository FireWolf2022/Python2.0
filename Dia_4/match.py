cliente = {
    'nombre': "Leonel",
    'edad' : 19
}

pelicula = {
    'nombre': "Fast and Furious",
    'origen' : 'EEUU'
}

lista = [cliente, pelicula, "mesa"]

for i in lista:
    match i:
        case {
            'nombre':nombre,
            'edad':edad
        }:
            print("Es un cliente")

        case {
            'nombre':name,
            'origen':origen
        }:
            print("Es una pelicula")
        case _:
            print("Ni idea de q es eso")