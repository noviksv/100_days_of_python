from turtle import Screen, Turtle, done
import time
from snake import Snake
from turtle import done
import time
from snake import Snake

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Snake setup

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


screen.update()
# print(len(snake))

# Game loop
is_game_on = True
while is_game_on:
    time.sleep(0.5)
    screen.update()
    snake.move()
    
    
screen.exitonclick()