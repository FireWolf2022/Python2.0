letras = []

texto = input("Ingrese el texto a analizar: ")
letras.append(input("Ingrese la primera letra: "))
letras.append(input("Ingrese la segunda letra: "))
letras.append(input("Ingrese la tercera letra: "))
incidencia = texto.lower()
print(f"La letra '{letras[0]}' aparece {incidencia.count(letras[0].lower())} veces en el texto, la '{letras[1]}' aparece {incidencia.count(letras[1].lower())} en el texto, y '{letras[2]}' aparece {incidencia.count(letras[2].lower())} veces en el texto")

cant = texto.split(" ")
print(f"Hay {len(cant)} palabras en el texto ingresado")

print(f"La primera letra es {texto[0]} y la ultima es {texto[-1]}")
cant.reverse()
inverso = " ".join(cant)
print(inverso)

python = "Python" in texto

respuesta = {
    True : "si",
    False : "no"
}

print(f"La palabra Python {respuesta[python]} esta en el texto")


