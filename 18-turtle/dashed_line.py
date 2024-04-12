import turtle

# Create a turtle object
franak = turtle.Turtle()

# size of the pen
franak.pensize(5)
# color of the pen
franak.pencolor("red")
#form of the pen
franak.shape("turtle")

# Dashed line
for _ in range(10):
    franak.forward(10)
    franak.penup()
    franak.forward(10)
    franak.pendown()


turtle.done()