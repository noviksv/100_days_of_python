BACKGROUND_COLOR = "#B1DDC6"

FOREIGN_WORD = "polski"
NATIVE_WORD = "english"

from tkinter import *
import pandas as pd
import random

global random_word
# ---------------------------- LOAD DATA FROM FILE ------------------------------- #

def load_data():
    try:
        data = pd.read_csv("data/words_to_learn.csv")
        return data 
    except FileNotFoundError:
        data = pd.read_csv("data/foreign_words.csv")
        return data
    except Exception as e:
        print(e)
        return None

    

def get_random_word(data):
    return random.choice(data.to_dict(orient="records"))

# ---------------------------- BUTTON COMMANDS ------------------------------- #


def flip_card():
    global random_word
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(title_label, text=NATIVE_WORD)
    canvas.itemconfig(word_label, text=random_word["native"])
    
    
def next_word(status="wrong"):
    global random_word
    random_word = get_random_word(data)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(title_label, text=FOREIGN_WORD)
    canvas.itemconfig(word_label, text=random_word["foreign"])
    if status == "right":
        remove_word(random_word["foreign"])
    window.after(3000, flip_card)

def remove_word(word):
    data.drop(data[data["foreign"] == word].index, inplace=True)
    data.to_csv("data/words_to_learn.csv", index=False)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

data = load_data()

#add canvas 2x2 grid
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.configure(bg=BACKGROUND_COLOR, highlightthickness=0)
#add labels
title_label = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_label = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

#add buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=lambda: next_word("right"))
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=lambda: next_word("wrong"))
wrong_button.grid(row=1, column=0)


next_word()



window.mainloop()



