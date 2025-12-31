class Personaje:
    def __init__(self, cant_flechas):
        self.flechas = cant_flechas

    def lanzar_flecha(self):
        self.flechas -= 1
        print(f"Se lanzó una flecha, te quedan {self.flechas}")

player = Personaje(20)
player.lanzar_flecha()

