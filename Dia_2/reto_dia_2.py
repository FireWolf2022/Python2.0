nombre = input("Nombre del trabajador: ")
ventas = float(input("Cuanto vendiste esta semana: "))
ganancia = round(ventas * 0.13, 2)
print(f"Ok {nombre}, este mes ganaste {ganancia}")