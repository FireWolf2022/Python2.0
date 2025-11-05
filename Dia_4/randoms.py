from random import *
#Numero random entero desde a hasta b
num = randint(0,10)

#Numero random decimal desde a hasta b
num2 = uniform(1,5)

#Numero random entre 0 y 1
num3 = random()

#Elige una un elemento random de la lista
lista = ["azul", "verde", "rojo", "amarillo", "blanco", "negro"]
aleatorio = choice(lista)

#Cambia el orden de los elementos de forma aleatoria
shuffle(lista)
print(lista)



a = int(input("Indica inicio "))
b = int(input("Indica fin "))

print(choice(range(a,b)))