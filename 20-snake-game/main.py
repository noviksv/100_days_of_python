from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
from snake import Snake

# Screen setup
screen = Screen()
screen.setup(width=600, height=600,startx=300, starty=300)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)



# Snake setup

snake = Snake()
food = Food()
score = Scoreboard()

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
    time.sleep(0.2)
    screen.update()
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        #is_game_on = False
        #score.game_over()
        score.reset()
        snake.reset()

    # Detect collisions with the tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            #is_game_on = False
            #score.game_over()
            score.reset()
            snake.reset()

    
    
screen.exitonclick()