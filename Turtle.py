from turtle import *
import random
import TraceTur as TT
import math
from multiprocessing import Process

screen = Screen()
screen.setup(900,500)
screen.bgcolor("black")
screen.title("Python Guides")
Tracelength = 400
a1 = TT.TraceTur(Tracelength)
b1 = TT.TraceTur(Tracelength)
c1 = TT.TraceTur(Tracelength)
d1 = TT.TraceTur(Tracelength)
e1 = TT.TraceTur(Tracelength)
    
a1.color(f'#{random.randrange(256**3):06x}')
b1.color(f'#{random.randrange(256**3):06x}')
c1.color(f'#{random.randrange(256**3):06x}')
d1.color(f'#{random.randrange(256**3):06x}')
e1.color(f'#{random.randrange(256**3):06x}')

turtlist = []
turtlist.append(a1)
turtlist.append(b1)
turtlist.append(c1)
turtlist.append(d1)
turtlist.append(e1)

screen.tracer(0, 0)

for TU in turtlist:
    TU.hideturtle()

def RunTurtle(TU: TT.TraceTur):
        if (math.sqrt(TU.xcor()**2 + TU.ycor()**2)) <= 200:
            TU.seth(random.randrange(0,270,90))
            TU.forward(10)
            TU.vanishTrace()
            screen.update()
        if (math.sqrt(TU.xcor()**2 + TU.ycor()**2)) > 200:
            if TU.Trace:
                TU.vanishTraceBasic()
                screen.update()
            else:              
                TU.clear()
                TU.cleaner.clear()
                TU.pu()
                TU.setpos(0, 0)
                TU.color(f'#{random.randrange(256**3):06x}')
                TU.pd()
                screen.update()

while True:
    for Turt in turtlist:
        RunTurtle(Turt)




