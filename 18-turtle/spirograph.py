import turtle
from random import random,choice

franak = turtle.Turtle()

franak.pensize(5)
franak.speed(0)

def spirograph(count_shapes):

    for _ in range(count_shapes):
        franak.pencolor((random(), random(), random()))
        franak.circle(100)
        franak.right(360/count_shapes)

spirograph(count_shapes=10)

turtle.done()
