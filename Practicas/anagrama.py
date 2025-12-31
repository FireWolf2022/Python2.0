palabra1 = input("Ingrese una palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

class Anagrama:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def paso1(self):
        tam = False
        igualdad = False
        if len(self.p1) == len(self.p2):
            tam = True
            if self.p1 in self.p2:
                print("Las palabras iguales no son anagramas")
                igualdad = True

        self.paso2(tam,igualdad)

    def paso2(self, tamanio, igualdad):
        result = True
        if tamanio and not igualdad:
            for i in range(len(self.p1)):
                if self.p1.count(self.p1[i]) != self.p2.count(self.p1[i]):
                    result = False
        else:
            result = False

        if result:
            print("Son anagramas!!!")
        else:
            print("No son anagramas :(")

caso1 = Anagrama(palabra1, palabra2)
caso1.paso1()