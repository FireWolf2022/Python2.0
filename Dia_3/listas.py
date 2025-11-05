lista = ["a", "b", "c", "d", "f", "g"]
des = [7,2,0,6,1,6,3,5,9,2,6]
#lista2 = ["h", "i", "j"]
print(des)

des.sort()
des.reverse()

print(des)
"""
lista_1 = ["C", "C++", "Python", "Java"]
lista_2 = ["PHP", "SQL", "Visual Basic"]
indexado: podemos acceder a los elementos de una lista a través de sus
índices [inicio:fin:paso]
print(lista_1[1:3])
>> ["C++", "Python"]
cantidad de elementos: a través de la propiedad len( )
print(len(lista_1))
>> 4
concatenación: sumamos los elementos de varias listas con el símbolo +
print(lista_1 + lista_2)
>> ['C', 'C++', 'Python', 'Java', 'PHP', 'SQL', 'Visual Basic']

lista_1 = ["C", "C++", "Python", "Java"]
lista_2 = ["PHP", "SQL", "Visual Basic"]
lista_3 = ["d", "a", "c", "b", "e"]
lista_4 = [5, 4, 7, 1, 9]
función append( ): agrega un elemento a una lista en el lugar
lista_1.append("R")
print(lista_1)
>> ["C", "C++", "Python", "Java", "R"]
función pop( ): elimina un elemento de la lista dado el índice, y devuelve el
valor quitado
print(lista_1.pop(4))
>> "R"
función sort( ): ordena los elementos de la lista en el lugar
lista_3.sort()
print(lista_3)
>> ['a', 'b', 'c', 'd', 'e']
función reverse( ): invierte el orden de los elementos en el lugar
lista_4.reverse()
print(lista_4)
>> [9, 1, 7, 4, 5]
reverse no es lo opuesto a sort
"""