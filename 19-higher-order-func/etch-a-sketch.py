import turtle as t

franak = t.Turtle()

def go_forward():
    franak.forward(10)

def go_backward():
    franak.backward(10)

def rotate_right():
    franak.right(15)

def rotate_left():
    franak.left(15)

def clear():
    franak.clear()
    franak.penup()
    franak.home()
    franak.pendown()

# Bind the go_forward function to the 'w' key
t.listen()

t.onkey(go_forward, "w")
t.onkey(rotate_right, "d")
t.onkey(rotate_left, "a")
t.onkey(go_backward, "s")
t.onkey(clear, "c")

t.done()