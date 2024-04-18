from turtle import Screen, exitonclick
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

INITIAL_SPEED = 0.1
speed = INITIAL_SPEED

# Screen setup
screen = Screen()
screen.setup(width=800, height=600,startx=300, starty=300)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle(coordinates=(-350, 0))
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")


right_paddle = Paddle(coordinates=(350, 0))
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.update()

is_game_on = True
while is_game_on:
    time.sleep(speed)
    ball.move()
    
    #detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #detect collision with the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        speed /=2
        print (speed)

    #detect when R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        speed = INITIAL_SPEED
        scoreboard.increase_left_score()
        
    #detect when L paddle misses
    if  ball.xcor() < -380:
        ball.reset_position()
        speed = INITIAL_SPEED
        scoreboard.increase_right_score()
        

    screen.update()
    
exitonclick() 