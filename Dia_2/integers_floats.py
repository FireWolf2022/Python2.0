a = ""
b = 0
print(type(a))
try:
    a = 2 / 0
    b = int("123g")
except ValueError:
    print("No admite caracteres strings, solo numericos")
except ZeroDivisionError:
    print("No se puede ividir por cero")


print("Final del programa")