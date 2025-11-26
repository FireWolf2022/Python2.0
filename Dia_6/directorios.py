import os
from libreria_pathlib import Path

ruta = os.getcwd()

general = Path(ruta) / "archivo.txt"

archivo = open(general)
print(archivo.read())

