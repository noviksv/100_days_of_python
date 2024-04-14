from turtle import Screen, Turtle, done
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Snake setup
snake = []

for i in range(3):
    tim = Turtle()
    tim.shape("square")
    tim.color("white")
    #tim.pensize(20)
    tim.penup()
    tim.setpos(x=-20*i, y=0)
    snake.append(tim)
    screen.update()

# Game loop
is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    for i in range(len(snake)-1, 0, -1):
        x = snake[i-1].xcor()
        y = snake[i-1].ycor()
        snake[i].goto(x, y)
    snake[0].forward(20)
    snake[0].left(90)
    
    
done()