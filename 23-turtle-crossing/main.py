import time
from turtle import Screen, exitonclick
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

screen.onkey(player.move, "Up")
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.update()

i = 0
#prepare game loop


game_is_on = True
while game_is_on:
    i +=1
    if i % 8 == 0:
        if len(car_manager) < 20:
            car_manager.add_cars()
        car_manager.reset_position()
    print(f"{i}: cars count={len(car_manager)}")
    car_manager.move_cars()
    if i >=120:
        screen.update()
        time.sleep(0.1)
    #detect collision with car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            break

    if player.ycor() > 220:
        scoreboard.increase_score()
        screen.update()
        player.start_next_level()
        car_manager.increase_speed()
    

exitonclick() 
