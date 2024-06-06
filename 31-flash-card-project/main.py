BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random

global random_word
# ---------------------------- LOAD DATA FROM FILE ------------------------------- #

def load_data():
    try:
        data = pd.read_csv("data/french_words.csv")
        return data 
    except FileNotFoundError:
        print("File not found")
    

def get_random_word(data):
    return random.choice(data.to_dict(orient="records"))

# ---------------------------- BUTTON COMMANDS ------------------------------- #

def next_word():
    global random_word
    random_word = get_random_word(data)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(title_label, text="French")
    canvas.itemconfig(word_label, text=random_word["French"])

def flip_card():
    global random_word
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(title_label, text="English")
    canvas.itemconfig(word_label, text=random_word["English"])
    



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

#add buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=next_word)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_word)
wrong_button.grid(row=1, column=0)

#add labels
title_label = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
# title_label = Label(text="French", font=("Ariel", 40, "italic"))
# title_label.grid(row=0, column=0, columnspan=2)
#title_label.config(bg="white")
#title_label.place(x=400, y=150, anchor="center")
word_label = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

# word_label = Label(text="Word", font=("Ariel", 60, "bold"))
# word_label.grid(row=0, column=0, columnspan=2)
# word_label.config(bg=BACKGROUND_COLOR)
# word_label.place(x=400, y=263, anchor="center")
next_word()

window.after(3000, flip_card)

window.mainloop()



