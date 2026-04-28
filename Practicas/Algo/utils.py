import os
name_error = 'No se encontraron los nombres'
len_error = 'No tienen las mismas dimensiones'
len_mult_error = 'Para poder multiplicar matrices deben coincidir la cantidad de columnas de la 1 y la cantidad de filas de la 2'
random_error = 'Se ha producido un error'
duplicated_name = 'El nombre ya esta en uso, prueba con otro'
mismo_nombre_operacion = "No puede elegir la misma matriz para realizar la operacion"
lista_opciones = '''1-Crear nuevas matrices
2-Mostrar matrices
3-Sumar
4-Restar
5-Multiplicar por un escalar
6-Multiplicar matrices
7-Hallar determinante
8-Matriz inversa
9-Salir
$- '''
enter = 'Presiona "Enter" para continuar...'
despedida = "Fue un placer trabajar contigo soldado, hasta la proxima"
matrices_disponibles = 'Matrices disponibles :)'

def resultados():
    print('-'.center(60,'-'))
    print("Resultado de la operacion".center(60,' '))
    print('-'.center(60,'-'))

def separador():
    print("=".center(60,'='))
    print('Menu de opciones'.center(60,' '))
    print("=".center(60,'='))

def manejo_errores():
    d = None
    while True:
        try:
            d = float(input("# => "))
            break
        except:
            print(random_error)
    return d

def clear_console():os.system('clear')

def cant_min(matriz,n):
    if len(matriz.keys()) < n :
        print("Imposible realizar la operacion con el numero actual de matrices")
        input(enter)
        return True
    return False
