archivo = open("otro_archivo.txt", "w")

def sobreescribir(n):
    archivo.write("contenido eliminado")
    archivo.close()


sobreescribir(archivo)

