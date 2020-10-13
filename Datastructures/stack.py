from turtle import *
from random import randint
speed(0)
bgcolor('black')
x=1
while x<500:
    w = randint(0,255)
    y = randint(0,255)
    p = randint(0,255)

    colormode(255)
    pencolor(w,y,p)
    fd(50 + x)
    rt(90.911)
    x = x+1
exitonclick()
