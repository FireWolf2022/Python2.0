from pathlib import Path
print("Bienvenido al Recetario")
ruta_recetas = Path(Path.home(), "Recetas")
print(f"La recetas se encuentran en la siguiente ruta: {ruta_recetas}")
cant_recetas = 0
for item in Path(ruta_recetas).glob("**/*.txt"):
    cant_recetas+=1
print(f"Tienes {cant_recetas} recetas")

#Lista para comprobar que las opciones ingresadas en el match son correctas B)
opciones = [i for i in range(1,7)]

#Primera opcion de las 6 en el match
def leer_receta():
    categoria = elegir_categoria()
    receta = mostrar_recetas(categoria)
    print(Path.read_text(receta))

#Segunda opcion del match
def crear_recetas():
    existe = False
    categoria = elegir_categoria()
    nombre_receta = input("Ingrese el nombre de su receta: ") + ".txt"
    if Path(categoria, nombre_receta).exists():
        print("La receta ya existe en este directorio")
    else:
        _ = open(nombre_receta, "w")
        existe = True
    if existe:
        contenido = input("Ingrese el contenido de su receta: ")
        Path(categoria, nombre_receta).write_text(contenido)

#Tercera opcion del match
def crear_categoria():
    nombre_categoria = input("Diga el nombre de la categoria que quiere crear: ")
    if Path(ruta_recetas, nombre_categoria).exists():
        print("La categoria ya existe")
    else:
        Path(ruta_recetas, nombre_categoria).mkdir()

#Cuarta opcion del match
def eliminar_receta():
    categoria = elegir_categoria()
    receta = mostrar_recetas(categoria)
    Path(receta).unlink()  #missing_ok=True deberia ponerlo, pero las opciones ya fueron elegidas, no hay margen de error

#Quinta opcion del match
def eliminar_categoria():
    categoria = elegir_categoria()
    try:
        Path(categoria).rmdir()
    except OSError:
        for i in Path(categoria).glob("*.*"):
            i.unlink()
        Path(categoria).rmdir()

#Elegir la categoria, devuelve la ruta de la categoria elegida
def elegir_categoria():
    print("Categorias:")
    cont = 0
    lista_categorias = []
    for direct in ruta_recetas.iterdir():
        cont += 1
        print(f"{cont}-{direct.stem}")
        lista_categorias.append(direct)
    suport = [i for i in range(1,cont+1)]
    categoria = 0
    if len(lista_categorias) == 0:
        print("No hay ninguna categoria")
        return 0

    else:
        while categoria not in suport:
            categoria = int(input(f"A que categoria quiere ingresar? Hasta {cont} categorias elegibles : "))

    return lista_categorias[categoria-1]


#mostrar las recetas txt de una ruta que le pasaste por parametros, retorna una receta elegida
def mostrar_recetas(ruta):
    lista_recetas = []
    cont = 0
    for txt in Path(ruta).glob("*.txt"):
        cont+=1
        print(f"{cont}-{txt.stem}")
        lista_recetas.append(txt)
    receta = int(input(f"Que receta quiere elegir? (Hasta {cont} recetas elegibles) : "))
    return lista_recetas[receta-1]


while True:
    print("=" * 60)
    print("A continuacion, le mostramos las opciones: ")
    print("1-Leer receta.\n2-Crear receta\n3-Crear categoría\n4-Eliminar receta\n5-Eliminar categoria\n6-Finalizar programa")
    op = input("Que opcion desea realizar: ")
    try:
        op = int(op)
        if op not in opciones:
            print("Elija una opcion en el rango especificado (1-6)")
            continue
    except ValueError:
        print("A ocurrido un error al intentar elegir la opcion, por favor, intente de nuevo")
        continue

    match op:
        case 1:
            print("1" * 60)
            leer_receta()
        case 2:
            print("2" * 60)
            crear_recetas()
        case 3:
            print("3" * 60)
            crear_categoria()
        case 4:
            print("4" * 60)
            eliminar_receta()
        case 5:
            print("5" * 60)
            eliminar_categoria()
        case 6:
            break
        case _:
            pass
