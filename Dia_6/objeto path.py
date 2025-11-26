from pathlib import Path

base = Path.home()
ruta = Path(base,"Universidad", "UCI.txt")

ruta2 = ruta.with_name("CUJAE.txt")

mostrar_videos = Path(Path.home(), "Vídeos", "python-total")
lista = []
for video in Path(mostrar_videos).glob("**/*.mp4"):
    lista.append(video.stem)
lista.sort()
for i in lista:
    #print(i)
    pass
"""
ruta = Path(Path.home(),"Descargas")
cont = 0
tipo = input("Ingrese el tipo de dato a contar en la carpeta de superusuario: ")
for i in Path(ruta).glob(f"**/*.{tipo}"):
    cont+=1

print(f"Hay {cont} archivos de tipo {tipo}")
"""
nueva = Path(Path.home(), "Vídeos", "humor")
for i in Path(nueva).glob("*.*"):
    #print(i.name)
    pass

orden = []
prueba = Path(Path.home(), "europa")
for item in Path(prueba).glob("**/*.txt"):
    orden.append(item.name)
orden.sort()
for i in orden:
    print(i)