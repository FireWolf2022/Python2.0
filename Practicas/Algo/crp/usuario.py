usuario = {}

def crear_usuario():
    while True:
        name = input("Ingrese el nombre de usuario: ")
        if name in usuario.keys():
            print("El nombre de usuario ya esta en uso, intente con otro")
            continue
        if not name.isalpha():
            print("El nombre no debe contener otros caracteres que no sean alfabeticos")
            continue
        break
    
def crear_clave():
    req = input("Desea crear la clave de forma automatica?: ").lower()
    if req != "n" or req != "no":
        