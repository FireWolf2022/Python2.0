import os

obj = {
    1:0,
    3:0,
    5:0,
    10:0,
    20:0,
    50:0,
    100:0,
    200:0,
    500:0,
    1000:0
}
names = ["Uno", "Tres", "Cinco", "Dies", "Veinte", "Cincuenta", "Cien", "Doscientos", "Quinientos", "Mill"]
indices = list(obj.keys())

def mostrar():
    total = 0
    primero = False
    for i in obj.values():
        if i != 0:
            primero = True
    if not primero:
        return

    #os.system("clear")
    print("")
    print("*".center(30,"*"))
    for i in obj.keys():
        temp = indices.index(i)
        if obj[i] != 0:
            print(f"=> {names[temp]} : {obj[i]}")
        total += i * obj[i]
    print(f"Total : {total}")
    print("*".center(30, "*"))
    print("")

def estadisticas():
    print("Haz salido del programa, espero te halla ayudado")
    print("A continuacion, tus estadisticas de conteo")
    mostrar()

    total_billetes = 0
    porcentaje = 0

    for value in obj.values():
        if value != 0:
            total_billetes += value
    print(f"Se contaron en total : {total_billetes} billetes")
    print("Porcentajes de billetes:")
    for key, value in obj.items():
        if value != 0:
            porcentaje = (value * 100) / total_billetes
            print(f"{names[indices.index(key)]} => {round(porcentaje,3)}%")





def main():
    print("Bienvenido, a continuacion va a tener dos opciones, agregar (en el caso de que no halla se crea uno nuevo) editar (se sumara)")
    input("Presione 'Enter' para continuar...")

    while True:
        mostrar()
        op = input("1-Asignar\n2-Editar (sumar)\n0-Salir \n$- ")

        try:
            op = int(op)
            if op == 0:break
            if op not in [0,1,2]:
                print("Elija una de las opciones mostradas")
                continue
        except ValueError:
            print("Debe elegir una opcion valida")
        print("Presione 0 para salir")
        match op:
            case 1:
                while True:
                    llave = input("Ingrese el valor: ")
                    try:
                        llave = int(llave)

                        if llave == 0:break

                        if llave not in obj.keys():
                            print("Ese billete no existe")
                            continue
                    except ValueError:
                        print("Digite una opcion coherente")
                        continue

                    valor = input("Ingrese la cantidad: ")
                    try:
                        valor = int(valor)
                        if valor < 0:
                            print("La cantidad no puede ser negativa")
                            continue
                    except ValueError:
                        print("Digite una opcion coherente")
                        continue

                    obj[llave] = valor
                    mostrar()

            case 2:
                while True:
                    mostrar()
                    key = input("Ingrese de cuanto es el billete: ")
                    try:
                        key = int(key)
                        if key == 0: break
                        if key not in obj.keys():
                            print("Ese billete no existe")
                            continue
                    except ValueError:
                        print("Digite una opcion coherente")
                        continue
                    while True:
                        value = input(f"Cuantos billetes de {key} quieres agregar: ")
                        try:
                            value = int(value)
                            if value == 0:break
                            #agregar algo para verificar que no reste mas que el valor que esta almacenado en el obj
                        except ValueError:
                            print("Digite una opcion coherente")
                            continue
                        obj[key] += value

    estadisticas()




if __name__ == __name__:
    main()
