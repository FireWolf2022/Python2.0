letras = ["a", "b", "c", "a"]
cadena = "".join(letras)
cont = 0
for i in letras:
    if i.lower() == "a":
#        print(cadena.find(i, cont))
        cont+=1

num = [[1,2,7],[3,4,8],[5,6,9]]

for i in num:
    for e in i:
       # print(e)
        pass

for a,b,c in num:
    print(a)
    print(b)
    print(c)

dick = {"c1" : ["Leo", "nel"], "c2" : ["Jesu", "s"], "c3" : ["Dio", "nairka"]}
for a,b in dick.values():
    print(a)
    print(b)
