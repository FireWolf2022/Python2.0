def  describir_persona(name,**kwargs):
    print(f"Características de {name}: ")
    for a,b in kwargs.items():
        print(f"{a} : {b}")

describir_persona("Leonel", color_pelo = "Negro", tamanio = 185, edad = 19)