from turtle import *

m = 30
speed(100)
left(90)
for i in range(6):
    forward(7 * m)
    right(120)
penup()
forward(3 * m)
right(90)
pendown()
for i in range(8):
    forward(5 * m)
    right(90)

penup()
for x in range(-3, 10):
    for y in range(-5, 10):
        setpos(x * m, y * m)
        dot(3, 'red')
done()