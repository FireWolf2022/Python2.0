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
print("Probando desde PyCharm por segunda vez")

def new(*cositas):
    for i in cositas:
        if i %2 == 0:
            print(f"{i} es par")
        else:
            print(f"{i} es impar")

new(1,2,3,4,5,6,7,8,9,10)
