from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.left(90)
        self.start_next_level()


    def move(self):
        self.forward(MOVE_DISTANCE)

    def start_next_level(self):
        self.goto(STARTING_POSITION)

