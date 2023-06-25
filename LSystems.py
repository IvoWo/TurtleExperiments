import string
import turtle

def lSysGenerate(s, order):
    for i in range(order):
        s = lSysCompute(s)
    return s

def lSysCompute(s):
    d = {'F': 'FF',
         'X': 'F+[[X]-X]-F[-FX]+X'}
    return ''.join([d.get(c) or c for c in s])

def draw(t, s, length, angle):
    Stack = []
    for c in s:
        if c == 'F':
            t.forward(length)
        elif c == '-':
            t.right(angle)
        elif c == '+':
            t.left(angle)
        elif c == '[':
            Stack.append((t.xcor(), t.ycor(),t.heading()))
        elif c == ']':
            t.pu()
            t.goto(Stack[-1][0],Stack[-1][1])
            t.seth(Stack[-1][2])
            t.pd()
            Stack.pop(-1)


def main():
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor('black')

    t.color('orange')
    t.pensize(1)
    t.penup()
    t.setpos(0, -200)
    t.pendown()
    t.speed(0)
    wn.tracer(0,0)
    t.left(70)

    axiom = 'X'
    length = 2.5
    angle = 25
    iterations = 6

    draw(t, lSysGenerate(axiom, iterations), length , angle)  # (length/(2 ** (iterations-1)))
    wn.update()
    wn.exitonclick()

main()