archivo = open("prueba.txt","w")
archivo.write("""Hola mundo desde python manito \n""")
archivo.close()

archivo = open("prueba.txt","r")
lineas = archivo.readlines()
print(lineas)
archivo.close()

archivo = open("prueba.txt", "a")
archivo.write("Ultima linea")
archivo.close()

try:
    nuevo = open("nuevo_archivo.txt", "x")
except:
    print("El archivo ya existe")