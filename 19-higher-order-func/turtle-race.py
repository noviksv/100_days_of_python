from turtle import Turtle, Screen, done
import random


screen = Screen()

is_race_on = False
screen.setup(width=600, height=600)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

bet = screen.textinput("Enter your bet", "Which turtle?")
print(f"Your bet is on {bet}")

all_turtles = []

for colour in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(colour)
    new_turtle.penup()
    new_turtle.goto(-250, 100- colors.index(colour) * 50)
    all_turtles.append(new_turtle)


if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 250:
            is_race_on = False
            print(f"{turtle.pencolor()} won!")
            if turtle.pencolor() == bet:
                print("You won!")
            else:
                print("You lost!")
            break

    

done()