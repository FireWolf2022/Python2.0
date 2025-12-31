from crear_matrices import create
from operaciones import suma_resta, mult_esc, mostrar_matrices
from utils import lista_opciones, name_error, separador, enter
from crear_matrices import matrices

def start():
    create()
    print('Ahora le mostramos opciones a elegir: ')
    while True:
        while True:
            try:
                op = int(input(lista_opciones))
                break
            except:
                print("Hubo un error")
                input(enter)
                separador()


        if op not in [i for i in range(1,6)]:
            print('Elija una opcion valida...')
            separador()
            continue
        match op:
            case 1:
                create()
            case 2:
                mostrar_matrices()
                m1 = input("Indique el nombre de la primera matriz que desea sumar: ")
                m2 = input("Bien, ahora ingrese el segundo: ")
                if m1 not in matrices.keys() or m2 not in matrices.keys():
                    print(name_error)
                else:
                    suma_resta(m1,m2,'s')
                separador()
                
            case 3:
                mostrar_matrices()
                m1 = input("Indique el nombre de la matriz a restar: ")
                m2 = input("Bien, ahora ingrese el segundo: ")
                if m1 not in matrices.keys() or m2 not in matrices.keys():
                    print(name_error)
                else:
                    suma_resta(m1,m2,'r')
                separador()

            case 4:
                mostrar_matrices()
                m = input('Ingrese el nombre de la matriz: ')
                if m not in matrices.keys():
                    print(name_error)
                    separador()
                    continue
                k = int(input('Indique el escalar por el que va a multiplicar la matriz: '))
                mult_esc(m,k)
                mostrar_matrices()
                separador()
            case 5:
                mostrar_matrices()
                separador()

