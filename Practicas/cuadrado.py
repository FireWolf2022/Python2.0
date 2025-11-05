a = int(input("De cuantos caracteres quieres el cuadrado: "))
medio = a/2
first = True
condi = True
fila1 = []
filaa = []
if a%2 == 1:
    condi = True
    medio +=.5
    medio -=1
izq = medio
der = medio

for i in range(a):
    fila1.append("*")
print("  ".join(fila1))
if a%2==0:
    for i in range(a-2):
        for e in range(a):
            if len(filaa) == 0:
                filaa.append("*")
            elif i == a-1:
                filaa.append("*")
            else:
                filaa.append(" ")

else:
    for i in range(a-2):
        if i == medio:
            first = False
        for n in range(a):
            if len(filaa) == 0:
                filaa.append("*")
            elif n == a-1:
                filaa.append("*")
            else:
                if condi:
                    if n == medio:
                        filaa.append("*")
                        izq = medio-1
                    else:
                        filaa.append(" ")
                else:
                    if first:
                        if n == izq:
                            filaa.append("*")
                            izq -=1
                        elif n == der:
                            filaa.append("*")
                        else:
                            filaa.append(" ")
                    else:
                        if izq <= 0:
                            izq = 2
                        if der == a-1:
                            der = a-3
                        if n == izq:
                            filaa.append("*")
                        elif n == der:
                            filaa.append("*")
                            der -= 1
                        else:
                            filaa.append(" ")
        condi = False

        der +=1
        if not first:
            der-=1
            izq += 1

        print("  ".join(filaa))
        filaa.clear()

print("  ".join(fila1))























"""


superior = ""
intermedio = ""
c = ""
cont = 0
sentido = False
validar1 = False
validar2 = False
first = True
posicion = a/2
if a%2 == 0:
    pass
else:
    posicion+=.5

apoyo = posicion
apoyo2 = posicion

print(posicion)

for i in range(a):
    superior +="*"
print(superior)

for i in range(a-2):
    for e in range(a):
        if intermedio == "":
            intermedio = "1"
        elif e == a-1:
            intermedio += "1"
            first = False
        else:
            if first:
                if (e+1) != posicion:
                    intermedio +="-"
                else:
                    intermedio += "2"
                    apoyo -=1
                    apoyo2 +=1
            else:
                if (e+1) != apoyo:
                    intermedio += "-"
                elif (e+1) != apoyo2:
                    intermedio += "-"

                if (e+1) == apoyo:
                    intermedio += "2"
                    if e == 1:
                        sentido = True
                    if sentido :
                        apoyo+=1
                    else:
                        apoyo -= 1
                elif (e+1) == apoyo2:
                    intermedio += "2"




    print(intermedio)
    intermedio = ""







"""


