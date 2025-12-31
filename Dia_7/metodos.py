class Pajaro:
    alas = True
    def __init__(self, tipo, color):
        self.tipo = tipo
        self.color = color

    @staticmethod
    def piar():
        print("Pío")

    @staticmethod
    def info():
        print("Es un pajaro")


piolin = Pajaro("Canario", "Amarillo")
algo = Pajaro("Canario", "Amarillo")
piolin.info()
algo.piar()


class Prueba:
    prueba = True
    def __inti__(self, tipo):
        self.tipo = tipo

    def info(self):
        print(f"El tipo de prueba es {self.tipo}")

print(Prueba.prueba)