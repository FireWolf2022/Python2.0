"""
Forma basica de encontrar un numero primo
n = 60
for num in range(3, n +1,2):
    primo = True
    for i in range(3, int(num**0.5)+1,2):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(f"{num} es primo")
"""
"""
# Cibra de Erastóstenes
n = int(input("Ingrese el limite: "))
lista = [True] * (n +1)
lista[0] = lista[1] = False

for p in range(2, int(n**0.5) +1):
    if lista[p]:
        for i in range(p*p, n+1, p):
            lista[i] = False
primos = [i for i in range(n+1) if lista[i]]
print(primos)
"""

"""

n = 10
lista_primos = [2]
for num in range(3, n+1, 2):
    primo = True
    for i in range(3, int(num**0.5) +1, 2):
        if num % i == 0:
            primo = False
            break
    if primo:
        lista_primos.append(num)
print(lista_primos)


array = [True] * (n+1)
array[0] = array[1] = False

for p in range(2, int(n**0.5)+1):
    if array[p]:
        for i in range(p*p, n+1,p):
            array[i] = False

new = [i for i in range(n+1) if array[i]]
print(new)
"""













"""
n = int(input("Ingrese el limite: "))
verda = [True] * (n+1)
verda[0] = verda[1] = False

for p in range(2, int(n**0.5)+1):
    if verda[p]:
        for i in range(p*p, n+1, p):
            verda[i]= False

lista = [i for i in range(n+1) if verda[i]]
print(lista)
"""


#Ya ésta es la verdadera :)

def primos(n):
    lista = [True] * (n+1)
    lista[0] = lista[1] = False
    for p in range(2, int(n**0.5)+1):
        for m in range(p*p, n+1, p):
            lista[m] = False
    lista_primos = [i for i in range(n+1) if lista[i]]
    print(lista_primos)
    return len(lista_primos)

print(primos(30))

#Fede
def contar_primos(n):
    cousin = [2]
    iteracion = 3

    if n < 2:
        return 0

    while iteracion <= n:
        for i in range(3,iteracion,2):
            if iteracion % i == 0:
                iteracion +=2
                break
        else:
            cousin.append(iteracion)
            iteracion +=2

    print(cousin)
    return len(cousin)

print(contar_primos(50))





