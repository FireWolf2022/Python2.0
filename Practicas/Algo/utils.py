name_error = 'No se encontraron los nombres'
len_error = 'No tienen las mismas dimensiones'
random_error = 'Se ha producido un error'
duplicated_name = 'El nombre ya es uso, prueba con otro'
lista_opciones = '1-Crear nuevas matrices\n2-Sumar\n3-Restar\n4-Multiplicar por un escalar\n5-Mostrar matrices\n$- '
enter = "Presiona Enter para continuar..."

def separador():
    print("=".center(60,'='))
    print()
    print("=".center(60,'='))

def manejo_errores():
    d = None
    while True:
        try:
            d = int(input("# => "))
            break
        except:
            print(random_error)
    return d
