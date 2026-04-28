import os
from pathlib import Path
from random import *
import shutil


def carpeta_sistema():

    mostrar_videos = Path(Path.home(), ".private", ".nuevo")
    lista = []
    for video in Path(mostrar_videos).glob("**/*.mp4"):
        lista.append(video.name)

    count = [i for i in range(len(lista))]
    selected = []

    videos_vistos = Path(os.getcwd(), "lista.txt")

    def generar(tam):
        num = randint(0,len(count))
        return num

    def leer():
        archivo = open(videos_vistos, "r" )
        contenido = archivo.readlines()
        archivo.close()
        return contenido

    def actualizar(num):
        archivo = open(videos_vistos, "a")
        archivo.write(f"{num}\n")
        archivo.close()


    selected = leer()

    def copiar(video):
        Path(os.getcwd(), "provider").mkdir(parents = True, exist_ok = True)
        shutil.copy(Path(mostrar_videos, lista[video]), Path(os.getcwd(), "provider"))
        print(f"Archivo {lista[video]} copiado con exito")
        input("Presione Enter al terminar para eliminar...")
        shutil.rmtree(Path(os.getcwd(), "provider"))
        print("Directorio y contenido eliminado satisfactoriamente, disfrute...")



    while True:


        if  len(selected) == len(lista):
            print("Ya has visto todos los videos pillín")
            op = input("Desea empezar otra rondita B) ? (s/n)").lower()
            if op == "s" or op == "si":
                Path(videos_vistos).unlink()
                open(Path(os.getcwd(),"lista.txt"), "x")
            break

        temporal = generar(len(count))
        if str(count[temporal]) + "\n" not in selected:
            actualizar(count[temporal])
            copiar(count[temporal])
            selected.append(str(count.pop(temporal)) + "\n")

            break

