from turtle import Turtle

FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-250, 270)
        self.write(f"Score: {self.l_score}", font=FONT)
        self.goto(150, 270)
        self.write(f"Score: {self.r_score}", font=FONT)

    def increase_left_score(self):
        self.l_score += 1
        self.update_score()

    def increase_right_score(self):
        self.r_score += 1
        self.update_score()