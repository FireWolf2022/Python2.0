from pathlib import Path

ruta = Path(Path.cwd(), "otro_archivo.txt")

def abrir_leer(archivo):
    n = open(archivo)
    return n.read()

print(abrir_leer(ruta))