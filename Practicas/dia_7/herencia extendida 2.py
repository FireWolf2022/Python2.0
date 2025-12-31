class Vertebrado:
    vertebrado = True
    @staticmethod
    def caminar():
        print("El animal puede caminar")
    @staticmethod
    def amamantar():
        print("El animal puede amamantar")

class Pez:
    @staticmethod
    def nadar():
        print("El animal puede nadar")

class Reptil:
    venenoso = True

class Ave:
    tiene_pico = True
    @staticmethod
    def poner_huevos():
        print("El animal puede poner huevos")

class Mamifero:
    @staticmethod
    def caminar():
        print("El animal puede caminar")

    @staticmethod
    def amamantar():
        print("El animal puede amamantar")

class Ornitorrinco(Vertebrado, Pez, Reptil, Ave, Mamifero):
    pass

print(Ornitorrinco)