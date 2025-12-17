class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    @staticmethod
    def nacer():
        print("Este animal ha nacido")

    def hablar(self):
        print(f"Este animal {self.color} emite un sonido")

class Pajaro(Animal):
    def __init__(self, edad, color, tipo):
        super().__init__(edad,color)
        self.tipo = tipo

    def hablar(self):
        print(f"El pajaro de {self.edad} años ha emitido un sonido")

piolin = Pajaro(3, "amarillo", "canario")
piolin.hablar()