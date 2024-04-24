import turtle
import pandas as pd


screen = turtle.Screen()  
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
game_is_on = True
score = 0 

data = pd.read_csv("50_states.csv")

while game_is_on:  
    answer_state = screen.textinput(f"{score}/50 What is the state's name?", "What's another state's name?").title().lower()
    if answer_state == "exit":
        break
    if answer_state in data.state.to_list():
        print(data.state.to_list())
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(data[data.state == answer_state].x.item(), data[data.state == answer_state].y.item())
        t.write(answer_state)


    print(answer_state)




screen.exitonclick()

