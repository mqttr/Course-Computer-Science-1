from turtle import *
from random import *

bgcolor('black')
t = Turtle()

t.speed(0)
colors = ("yellow","white","blue","green","purple")
border = 400

while True:
    x = randint(-border,border)
    y = randint(-border,border)
    colorNum = randint(0,4)
    t.color(colors[colorNum])
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(210):
        t.forward(i)
        t.right(i)



done()