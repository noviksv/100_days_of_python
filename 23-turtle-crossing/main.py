import time
from turtle import Screen, exitonclick
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")

scoreboard = Scoreboard()
screen.listen()
screen.update()

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    if player.ycor() > 220:
        scoreboard.increase_score()
        player.start_next_level()
    screen.update()

exitonclick() 