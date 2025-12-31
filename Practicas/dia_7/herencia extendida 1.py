class Padre:
    @staticmethod
    def reir():
        print("ja ja")

    @staticmethod
    def vocacion():
        print("Trabajando sabe Dios donde")

class Madre:
    @staticmethod
    def vocacion():
        print("Trabajando en la Fiscalía")

class Hija(Madre, Padre):
    pass

print(Hija.vocacion())
