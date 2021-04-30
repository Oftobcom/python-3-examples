import math

func = lambda a: a ** 2
a = int(input("a = "))
print(func(a))


func = lambda a, b: math.sqrt(a ** 2 + b ** 2)
a = int(input("a = "))
b = int(input("b = "))
print(func(a, b))

