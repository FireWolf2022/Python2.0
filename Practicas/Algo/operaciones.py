from crear_matrices import matrices, nombres
from utils import name_error, len_error, duplicated_name, enter, len_mult_error, resultados, clear_console

operation = {}

def suma_resta(a,b,op):    
    if a not in matrices.keys() or b not in matrices.keys():
        print(name_error)
        input(enter)
        return
    if len(matrices[a]) != len(matrices[b]):
        print(len_error)
        input(enter)
        return 
    if len(matrices[a][0]) != len(matrices[b][0]):
        print(len_error)
        input(enter)
        return 
    
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
    clear_console()
    resultados()
    mostrar_matrices(name)
    input(enter)

def mult_esc(matriz, k):
    for x in range(len(matriz)):
        for y in range(len(matriz[0])):
            matriz[x][y] *= k
    return matriz  

def mostrar_matrices(*args):
    if args[0] == 'all':
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
        for name in args:
            if name not in matrices.keys():
                print(name_error)
                return
        
            for i in range(len(matrices[name])):
                    if i == 0:
                        print(f'{name} :', end=' ')
                    for e in range(len(matrices[name][i])):
                        if e == 0 and i != 0:
                            print('   ', end=' ')
                            
                        if e != len(matrices[name][i]) - 1:    
                            print(matrices[name][i][e], end=' ')
                            
                        else:
                            print(matrices[name][i][e])
                            
                    if i == len(matrices[name]) - 1:
                        print('\n', end='') 

def mult_mat(m1,m2):
    mostrar_matrices(m1,m2)

    m1 = matrices[m1]
    m2 = matrices[m2]

    if len(m1[0]) != len(m2):return len_mult_error

    print("Desea continuar con las matrices elegidas? De no querer se volvera al menu")
    continuar = input("$-Si(s) o No(n) : ").lower()
    if continuar == "n" or continuar == "no":return 

    matriz = [[0] * len(m2[0]) for _ in range(len(m1))]
    
    base = 0
    
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):

            for x in range(len(m1[0])):
                base += m1[fila][x] * m2[x][columna]


            matriz[fila][columna] = base
            base = 0

    while True:
        name = input("Ingrese el nombre de la matriz creada: ").upper()
        if name in nombres:
            print(duplicated_name)
            continue
        nombres.add(name)
        break

    matrices[name] = matriz
    clear_console()
    resultados()
    mostrar_matrices(name)
    input(enter)

def det_comun(mtz,*args):
    for i in args:
        i = mtz[i]
        if len(i) != len(i[0]):
            print(len_error)
            return 
    determinantes = []

    for name in args:
        det_matriz = mtz[name]
        if len(det_matriz) == 1:
            determinantes.append(det_matriz[0][0])

        if len(det_matriz) == 2:
            c,u = 0,1
            variable_apoyo = det_matriz[c][c] * det_matriz[u][u] - det_matriz[u][c] * det_matriz[c][u]
            determinantes.append(variable_apoyo)

        elif len(det_matriz) == 3:
            m = det_matriz
            signo = True
            x,y = 0,0
            apoyo_suma = [0,0]
            apoyo_mult = 1

            for i in range(6):
                x = 0
                x += i
                if i == 3:signo = False

                if signo:
                    for _ in range(3):
                        apoyo_mult *= m[x][y]
                        x+=1
                        y+=1
                        if x > 2:x=0
                        if y > 2:y=0
                    apoyo_suma[0] += apoyo_mult
                    apoyo_mult = 1
                if not signo:
                    y = 0
                    x -= 3
                    for _ in range(3):
                        apoyo_mult *= m[x][y]
                        x-=1
                        y+=1
                        if x < 0:x=2
                        if y > 2:y=0

                    apoyo_suma[1] += apoyo_mult
                    apoyo_mult = 1
                    
            determinantes.append(apoyo_suma[0] - apoyo_suma[1])
            

    if len(determinantes) <= 1:
        determinante = determinantes[0]
        return determinante
    return determinantes

def menor(x,y,matriz):
    n = len(matriz)
    menor_resultante = [[0] * (n-1) for _ in range(n -1)]

    for fila in range(n):
        if fila == x:
            continue
        for columna in range(n):
            if columna == y:
                continue
            
            nueva_fila = fila - (1 if fila > x else 0)
            nueva_columna = columna - (1 if columna > y else 0)
            menor_resultante[nueva_fila][nueva_columna] = matriz[fila][columna]

    return menor_resultante

def det_inusual(m):
    lista = []
    temp = {}
    resultado = 0
    temp2 = 0
    for i in range(len(m)):
        temp[i] = menor(i,0,m)
        tam = len(temp[i])

        if tam <= 3:
            auxiliar = det_comun({0: temp[i]}, 0)
        else:
            auxiliar = det_inusual(temp[i])

        if i%2 != 0:
            temp2 = m[i][0] * (auxiliar * (-1))
        else:
            temp2 = m[i][0] * auxiliar
        lista.append(temp2)
    
    for i in lista:
        resultado += i

    return resultado

def cofactores(m):
    lista = [[0]* len(m[0]) for _ in range(len(m))]
    for x in range(len(m)):
        for y in range(len(m)):
            menor_xy = menor(x,y,m)
            if len(menor_xy) <= 3:
                temp2 = det_comun({0: menor_xy}, 0)
            else:
                temp2 = det_inusual(menor_xy)
            if (x+y)%2 != 0:
                temp2 *= -1
            lista[x][y] = temp2
    return lista

def determinante(name):
    retorno = 0
    if len(matrices[name]) <=3:
        retorno = det_comun(matrices, name)
    else:
        retorno = det_inusual(matrices[name])
        
    return retorno

def traspuesta(matriz):
    matriz_traspuesta = [[0]*len(matriz) for _ in range(len(matriz))]
    for fila in range(len(matriz)):
        for columna in range(len(matriz)):
            matriz_traspuesta[columna][fila] = matriz[fila][columna]
    
    return matriz_traspuesta

def inversa(name):
    m = matrices[name]
    cofactor = cofactores(m)
    adj = traspuesta(cofactor)
    inv = mult_esc(adj, 1/determinante(name))
    clear_console()
    resultados()
    matrices[f"-{name}"] = inv
    mostrar_matrices(f"-{name}")
    return inv