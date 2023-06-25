from turtle import *
import turtle as tur
import random

tur.setup(900,500)
tur.bgcolor("black")
tur.title("Python Guides")
a1 = tur.Turtle()
b1 = tur.Turtle()

a1.color('yellow')
b1.color('red')


turtlist = []
turtlist.append(a1)
turtlist.append(b1)


tur.speed(0)
tur.tracer(0)
tur.hideturtle()
sum = 0
count = 0
for i in range(5000):
    for turt in turtlist:
        angle = turt.heading() + 90
        turt.seth(angle)
        turt.fd(10)
        turt.fd(10)
        turt.fd(10)
        turt.fd(10)
        angle = 0
    tur.update()
