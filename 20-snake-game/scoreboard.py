from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.read_high_score()


    def increase_score(self):
        self.score += 1
        # self.update_high_score()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High score: {self.high_score}" , align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.update_high_score()
        self.score = 0

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_score()
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))

    def read_high_score(self):
        #crete file if it does not exist
        try:
            with open("data.txt", "r") as file:
                self.high_score = int(file.read())
                self.update_score()
        except FileNotFoundError:
            with open("data.txt", "w") as file:
                file.write("0")


            