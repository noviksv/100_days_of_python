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
data.state = data.state.str.lower()
correct_states = []

while game_is_on:  
    answer_state = screen.textinput(f"{score}/50 What is the state's name?", "What's another state's name?").title().lower()
    if answer_state == "exit":
        break
    if answer_state in data.state.to_list() and  answer_state not in correct_states:
        print(data.state.to_list())
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(data[data.state == answer_state].x.item(), data[data.state == answer_state].y.item())
        t.write(answer_state)
        score += 1
        correct_states.append(answer_state)
        screen.update()
    if score == 50:
        game_is_on = False
        print("You won!")
        break


    print(answer_state)




screen.exitonclick()

