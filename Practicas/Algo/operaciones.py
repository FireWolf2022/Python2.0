from crear_matrices import matrices, nombres
from utils import name_error, len_error, duplicated_name, enter, manejo_errores

operation = {}

def suma_resta(a,b,op):    
    if a not in matrices.keys() or b not in matrices.keys():return name_error
    if len(matrices[a]) != len(matrices[b]):return len_error
    if len(matrices[a][0]) != len(matrices[b][0]): return len_error
    
    fila_paso = []
    matris_paso = []
    
    
    for x in range(len(matrices[a])):
        for y in range(len(matrices[a][0])):
            if op == 's':
                fila_paso.append(matrices[a][x][y] + matrices[b][x][y])
            elif op == 'r':
                fila_paso.append(matrices[a][x][y] - matrices[b][x][y])
        matris_paso.append(fila_paso)
        fila_paso = []
    
    while True:
        name = input("Ingrese el nombre de la matriz: ").upper()
        if name in nombres:
            print(duplicated_name)
            continue
        nombres.add(name)
        break
        
    matrices[name] = matris_paso
    
    mostrar_matrices()
    input(enter)

def mult_esc(m,k):
    for x in range(len(matrices[m])):
        for y in range(len(matrices[m][0])):
            matrices[m][x][y] *= k
    
    mostrar_matrices(m)
    input(enter)
    
def mostrar_matrices(select = 'all'):
    if select == 'all':
        for x,y in matrices.items():
            for i in range(len(y)):
                if i == 0:
                    print(f'{x} :', end=' ')
                for e in range(len(y[i])):
                    if e == 0 and i != 0:
                        print('   ', end=' ')
                        
                    if e != len(y[i]) - 1:    
                        print(y[i][e], end=' ')
                        
                    else:
                        print(y[i][e])
                        
                if i == len(y) - 1:
                    print('\n', end='')        
    else:
        if select not in matrices.keys():
            print(name_error)
            return
        
        for i in range(len(matrices[select])):
                if i == 0:
                    print(f'{select} :', end=' ')
                for e in range(len(matrices[select][i])):
                    if e == 0 and i != 0:
                        print('   ', end=' ')
                        
                    if e != len(matrices[select][i]) - 1:    
                        print(matrices[select][i][e], end=' ')
                        
                    else:
                        print(matrices[select][i][e])
                        
                if i == len(matrices[select]) - 1:
                    print('\n', end='') 