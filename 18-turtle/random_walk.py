import turtle
from random import random,choice

angles = [90, 180, 270, 360]

# Create a turtle object
franak = turtle.Turtle()
franak.pensize(5)
franak.speed(10)

def random_walk(steps):
    for _ in range(steps):
        franak.pencolor((random(), random(), random()))
        franak.forward(30)
        franak.right(choice(angles))

random_walk(100)

turtle.done()