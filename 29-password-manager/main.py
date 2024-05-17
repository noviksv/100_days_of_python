# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
YELLOW = "#f7f5dd"
# add logo to screen


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#add a canvas
canvas = Canvas(width=200, height=200,  highlightthickness=0)
tomato_img = PhotoImage(file="logo.png")
img = canvas.create_image(100, 100, image=tomato_img)
canvas.create_image(100, 100, image=tomato_img)
canvas.grid()




window.mainloop()

