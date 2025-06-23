import turtle
turtle.Screen()
turtle.screensize(500,500)
t=turtle.Turtle()
turtle.bgcolor("cyan")
n=3
a=120
t.width(5)
t.color("green")
for i in range(n):
    t.forward(100)
    t.left(a)

t.left(90)    
t.penup()
t.forward(60)
t.right(90)
t.pendown()

for i in range(n):
    t.forward(100)
    t.right(a)



turtle.done()