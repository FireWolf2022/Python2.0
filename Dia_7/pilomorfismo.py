class Vaca:
    
    tipo = 'Moras'
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        print(f"{self.nombre} hace muu")
        
    def tipo(cls):
        print(f"Las vacas son tipo {cls.tipo}")
        
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        print(f'{self.nombre} hace Wau!')
        

aurora = Vaca('Aurora')
blanca = Perro('Blanca')
    
for i in [aurora, blanca]:
    i.hablar()