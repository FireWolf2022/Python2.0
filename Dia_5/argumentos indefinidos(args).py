def suma(*args):
    final = 0
    for i in args:
        final+=i
    return final
print(suma(4,5,6))