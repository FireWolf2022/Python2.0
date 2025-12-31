from utils import duplicated_name, separador, manejo_errores, random_error
matrices = {}
nombres = set()
def create():
    num = None
    while True:
        try:
            num = int(input('Cuantas matrices vas a crear: '))
            if num <=0:
                print(f"Como tu vas a crear {num} matrices asere, ponte pa esto")
            break
        except:
            print(random_error)
    filas = []
    n = None
    for i in range(int(num)):
        while True:
            try:
                row = int(input(f'Numero de filas de la {i+1}: '))
                column = int(input(f'Numero de columnas de la {i+1}: '))
                break
            except:
                print(random_error)

        lista = []

        for x in range(row):
            print(f'Fila {x+1}')
            for y in range(column):
                filas.append(manejo_errores())
            lista.append(filas)
            filas = []
        
        while True:
            n = input(f'Ingrese el nombre de la matriz {i+1}: ')
            if not n.isalpha():
                print('Los nombres deben ser alfabeticos')
                continue
            if n in nombres:
                print(duplicated_name)
                continue
            nombres.add(n)
            break
            
        matrices[n] = lista
    separador()
