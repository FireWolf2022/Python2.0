class Animal:
    vivo = True

class Pajaro(Animal):

    pass

print(Pajaro.vivo)
Pajaro.vivo = False
print(Animal.vivo)
print(Pajaro.vivo)


