class Pajaro:
    alas = True
    def __init__(self, tipo, color):
        self.tipo = tipo
        self.color = color


    def piar(self):
        print("Pio Pio Pio")
        self.cantar()

    def cantar(self):
        print(f"El {self.tipo} esta cantando")


    def pintar_negro(self):
        self.color = "negro"
        print("Ahora el pajaro es {}".format(self.color))

    def info(self):
        print(f"El {self.tipo} es {self.color}")

piolin = Pajaro("canario", "amarillo")
piolin.piar()
piolin.pintar_negro()
piolin.info()