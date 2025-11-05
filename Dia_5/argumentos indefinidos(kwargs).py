def dic(**kwargs):
    for a,b in kwargs.values():
        print(f"El primer valor es {a}, y el segundo valor es {b}")


dic(x = [1,2], y = [3,4], z = [5,6])
