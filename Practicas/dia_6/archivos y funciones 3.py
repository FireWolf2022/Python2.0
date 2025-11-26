archivo = open("otro_archivo.txt", "a")
def registro_error(n):
    n.write("Se ha registrado un error de ejecucion\n")


registro_error(archivo)

archivo.close()

