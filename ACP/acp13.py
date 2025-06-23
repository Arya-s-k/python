import turtle
turtle.Screen()
turtle.screensize(500,500)
t=turtle.Turtle()
turtle.bgcolor("cyan")
n=4
a=90
t.width(5)
t.color("red")
t.begin_fill()
for i in range(n):
    t.forward(100)
    t.right(a)
t.end_fill()


turtle.done()