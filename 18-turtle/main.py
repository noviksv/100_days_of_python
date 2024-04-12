import turtle

# Create a turtle object
franak = turtle.Turtle()

# size of the pen
franak.pensize(5)
# color of the pen
franak.pencolor("red")
#form of the pen
franak.shape("turtle")
for _ in range(4):
    franak.forward(100)
    franak.right(90)


turtle.done()