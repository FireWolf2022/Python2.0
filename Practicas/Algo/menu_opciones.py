from crear_matrices import create
from operaciones import suma_resta, mult_esc, mostrar_matrices, mult_mat, determinante, traspuesta, inversa
from utils import lista_opciones, name_error, separador, enter, clear_console, matrices_disponibles, resultados, cant_min, mismo_nombre_operacion, len_error
from crear_matrices import matrices

def start():
    create()
    print('Ahora le mostramos opciones a elegir: ')
    while True:
        while True:
            try:
                clear_console()
                separador()
                op = int(input(lista_opciones))
                break
            except:
                print("Hubo un error")
                input(enter)
                separador()


        if op not in [i for i in range(1,10)]:
            print('Elija una opcion valida...')
            input(enter)
            continue
        match op:
            case 1:
                clear_console()
                create()
            case 2:
                clear_console()
                print('Matrices creadas hasta el momento')
                mostrar_matrices('all')
                input(enter)
                
            case 3:
                if cant_min(matrices,2):continue
                clear_console()
                print(matrices_disponibles)
                mostrar_matrices('all')
                m1 = input("Indique el nombre de la primera matriz que desea sumar: ")
                m2 = input("Bien, ahora ingrese el segundo: ")
                if m1 == m2 : 
                    print(mismo_nombre_operacion)
                    input(enter)
                    continue
                if m1 not in matrices.keys() or m2 not in matrices.keys():
                    print(name_error)
                    input(enter)
                else:
                    suma_resta(m1,m2,'s')
                
            case 4:
                if cant_min(matrices,2):continue
                clear_console()
                print(matrices_disponibles)
                mostrar_matrices('all')
                m1 = input("Indique el nombre de la matriz a restar: ")
                m2 = input("Bien, ahora ingrese el segundo: ")
                if m1 == m2 : 
                    print(mismo_nombre_operacion)
                    input(enter)
                    continue
                if m1 not in matrices.keys() or m2 not in matrices.keys():
                    print(name_error)
                    input(enter)
                else:
                    suma_resta(m1,m2,'r')

            case 5:
                if cant_min(matrices,1):continue
                clear_console()
                print(matrices_disponibles)
                mostrar_matrices('all')
                m = input('Ingrese el nombre de la matriz: ')
                if m not in matrices.keys():
                    print(name_error)
                    separador()
                    continue
                k = int(input('Indique el escalar por el que va a multiplicar la matriz: '))
                mult_esc(m,k)
                clear_console()
                resultados()
                mostrar_matrices(m)
                input(enter)

            case 6:
                if cant_min(matrices,2): continue
                clear_console()
                print(matrices_disponibles)
                mostrar_matrices('all')
                m1 = input("Ingrese el nombre de la primera matriz que desea multiplicar: ")
                m2 = input("Ahora el de la segunda matriz: ")
                if m1 not in matrices.keys() or m2 not in matrices.keys():
                    print(name_error)
                    input(enter)
                else:
                    mult_mat(m1,m2)

            case 7:
                clear_console()
                if cant_min(matrices,1): continue
                print(matrices_disponibles)
                mostrar_matrices('all')
                m = input('Ingrese el nombre de la matriz: ')
                if m not in matrices.keys():
                    print(name_error)
                    separador()
                    continue
                clear_console()
                resultados()
                print(determinante(m))
                input(enter)
                
            case 8:
                clear_console()
                if cant_min(matrices,1): continue
                print(matrices_disponibles)
                mostrar_matrices('all')
                name = input("Ingrese el nombre de la matriz que va a seleccionar ")
                if name not in matrices.keys():
                    print(name_error)
                    continue
                if len(matrices[name]) != len(matrices[name][0]):
                    print(len_error, " debe ser cuadrada")
                    continue
                if determinante(name) == 0:
                    print("La matriz no tiene inversa :(")
                    input(enter)
                    continue
                inversa(name)
                input(enter)

            case 9:
                pass
            case 10:
                break

            case _:
                print("Candela algo salio mal, error mio...")
                input(enter)
 