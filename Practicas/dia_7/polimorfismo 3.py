class Arquero:
    def atacar(self):
        print("Flechas de Fuego!!")
        
    def defender(self):
        print("Capa de Hierro")

class Mago:
    def atacar(self):
        print("Mar de LLamas")
        
    def defender(self):
        print("Muro de Hielo")

class Samurai:
    def atacar(self):
        print("Cortes del Mal")
        
    def defender(self):
        print("Movimiento Sombra")

personaje1 = Arquero()
personaje2 = Mago()
personaje3 = Samurai()

def personaje_defender(personaje):
    personaje.defender()
    
personaje_defender(personaje3)