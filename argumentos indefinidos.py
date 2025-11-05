def suma(*args):
    total = 0
    for i in args:
        total += i

    return total

def potencia(base, *exp):
    exponentes = sum(exp)
    return base**exponentes

print(suma(4,5,6,45,-34,7))

print(potencia(2, 2, 2, 2, 5))