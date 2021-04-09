import random as r
a = r.randrange(1,100)
n = int(input())
while n != a:   
    if n > a:
        print("Калон")
    else:
        print("Хурд")
    n = int(input())
else :
        print("Шумо ададро ёфтед!")
