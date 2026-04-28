from pathlib import Path
from random_videos import carpeta_sistema
from externos import dispositivos_externos

variedad =Path(Path.home(), ".private", ".nuevo")
contador = []
for video in Path(variedad).glob("**/*.mp4"):
    contador.append(video.name)


def main():
    print(f"Bienvenido al sistema de distribucion de videos, actualmente contamos con {len(contador)} videos disponibles")
    while True:
        print("Elija a continuacion la modalidad que desea implementar\n1-Carpeta del sistema\n2-Dispositivo externo")
        try:
            op=int(input("\n$-"))
            if op not in [1,2]:
                op = 1/0
        except :
            print("Debe ingresar una opcion valida")
            continue
        
        match(op):
            case 1:
                carpeta_sistema()
            case 2:
                dispositivos_externos()

        
    



if __name__ == __name__:
    main()
