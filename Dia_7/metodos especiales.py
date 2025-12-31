class CD:
    def __init__(self, autor, album, canciones) -> None:
        self.autor = autor
        self.album = album
        self.canciones = canciones
        
    def __str__(self):
        return f'{self.album} : produced by {self.autor}, {self.canciones} songs'
    
    def __len__(self):
        return self.canciones
    
    def __del__(self):
        print('Se ha eliminado el CD')

num = '123'
num = int(num)

print(type(num))