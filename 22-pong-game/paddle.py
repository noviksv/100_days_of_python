from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        # define coordinates for the paddle
        self.goto(coordinates)
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

