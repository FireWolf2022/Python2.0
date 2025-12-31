class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True

j1 = Jugador()
print(j1.vivo)
j1.revivir()
print(j1.vivo)
