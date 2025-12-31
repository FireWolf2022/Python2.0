class Padre:
    color_ojos = "cafe"
    color_pelo = "negro"

    @staticmethod
    def ocupacion():
        print("Trabaja")
    @staticmethod
    def hobbie():
        print("Ver peliculas")

class Hijo(Padre):
    @staticmethod
    def ocupacion():
        print("Estudiante")

    @staticmethod
    def hobbie():
        print("Ver series")
