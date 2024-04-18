from turtle import Screen, exitonclick
import time
from paddle import Paddle
from ball import Ball

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
screen.listen()
screen.update()

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    ball.move()
    
    #detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #detect collision with the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect when the ball goes out of bounds
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.reset_position()
        

    screen.update()
    
exitonclick() 