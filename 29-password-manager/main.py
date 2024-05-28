# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
YELLOW = "#f7f5dd"
# add logo to screen


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#add a canvas 3x5 grid
canvas = Canvas(width=200, height=200,  highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
img = canvas.create_image(100, 100, image=logo_img)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
entry_website = Entry(width=35)
entry_website.grid(row=1, column=1, columnspan=2)
label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)
entry_email = Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2)
label_password = Label(text="Password:")
label_password.grid(row=3, column=0)
entry_password = Entry(width=21)
entry_password.grid(row=3, column=1)
button_generate_password = Button(text="Generate Pass", width=10)
button_generate_password.grid(row=3, column=2)
button_add = Button(text="Add", width=36)
button_add.grid(row=4, column=1, columnspan=2)



window.mainloop()

