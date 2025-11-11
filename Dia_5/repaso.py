lista = [n if n%2 == 0 else "*" for n in range(1,11)]
print(lista)
"""
l = int(input("Digite el limite: "))
verda = [True] * (l+1)
verda[0] = verda[1] = False

for p in range(2, int(l**0.5) +1):
    if verda[p]:
        for m in range(p*p, l+1, p):
            verda[m] = False

primos = [n for n in range(l+1) if verda[n]]
print(primos)
"""
"""
l = int(input("DIgite el limite: "))
lista_primos = [2]
for num in range(3, l+1, 2):
    primo = True
    for i in range(3, int(num**0.5)+1, 2):
        if num%i == 0:
            primo = False
            break
    if primo:
        lista_primos.append(num)

print(lista_primos)
"""
def recursividad(n):
    if n == 0: return
