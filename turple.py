import turtle

def sq(a):
    for i in range(4):
        
        joe.forward(a)
        joe.left(90)

colors = ['red','brown','green','blue','yellow','grey','orange','aqua']
joe = turtle.Turtle()
joe.speed(20)

dlina = 5
for i in range(65):
    joe.color(colors[i%len(colors)])
    sq(dlina)
    joe.right(10)
    dlina+=5
