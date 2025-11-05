lista = input("Introduce los numeros separados por comas: ")
new = lista.split(",")
new.sort()
a,b,c = new
a,b,c = int(a), int(b), int(c)

def devolver_distintos(n1, n2, n3):
    suma = n1+n2+n3
    if suma > 15:
        print(max(n1,n2,n3))
    elif suma < 10:
        print(min(n1,n2,n3))
    else:
        print(new[1])

devolver_distintos(a,b,c)

