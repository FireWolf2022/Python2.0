def dtodo(num1, *args, **kwargs):
    print(f"Numero {num1}")

    for i in args:
        print(f"Numerosss {i}")

    for a,b in kwargs.items():
        print(f"Clave ({a}) : Valor ({b})")

lista = [2,34,6,8]
dic = {
    "x" : 2,
    "v" : 3
}

dtodo(3,*lista ,**dic)
