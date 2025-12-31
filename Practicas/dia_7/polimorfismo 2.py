class Arquero:
    def atacar(self):
        print("Flechas de Fuego!!")

class Mago:
    def atacar(self):
        print("Mar de LLamas")

class Samurai:
    def atacar(self):
        print("Cortes del Mal")

personaje1 = Arquero()
personaje2 = Mago()
personaje3 = Samurai()

for p in [personaje1, personaje2, personaje3]:
    p.atacar()