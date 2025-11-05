nombres = ["Maria", "Roberto", "Neida"]
edades = [25,35,47]

juntos = list(zip(nombres, edades))
print(juntos)

for name, age in juntos:
    print(f"{name} tiene {age}")
