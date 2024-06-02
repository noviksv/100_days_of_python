BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#add canvas 2x2 grid
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.configure(bg=BACKGROUND_COLOR, highlightthickness=0)

#add buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(row=1, column=0)

#add labels
title_label = Label(text="Title", font=("Ariel", 40, "italic"))
title_label.grid(row=0, column=0, columnspan=2)
title_label.config(bg=BACKGROUND_COLOR, fg="white")
title_label.place(x=400, y=150, anchor="center")

word_label = Label(text="Word", font=("Ariel", 60, "bold"))
word_label.grid(row=0, column=0, columnspan=2)
word_label.config(bg=BACKGROUND_COLOR, fg="white")
word_label.place(x=400, y=263, anchor="center")


window.mainloop()