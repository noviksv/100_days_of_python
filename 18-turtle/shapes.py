import turtle
from random import random

# Create a turtle object
franak = turtle.Turtle()
franak.pensize(5)


def draw_shape(sides):
    franak.pencolor((random(), random(), random()))
    for _ in range(sides):
        #add a random color
        
        franak.forward(100)
        franak.right(360/sides)

for i in range(3,11):
    draw_shape(i)

turtle.done()