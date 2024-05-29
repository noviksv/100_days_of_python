from tkinter import messagebox
from tkinter import *
YELLOW = "#f7f5dd"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    import random
    import string
    entry_password.delete(0, END)
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
    entry_password.insert(0, password)
    #copy to clipboard
    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()
    messagebox.showinfo(title="Password", message="Password copied to clipboard")
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    if not website or not email or not password:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return
    msgbx = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
    if msgbx:
        with open("data.txt", "a") as data:
            data.write(f"{website} | {email} | {password}\n")
            entry_website.delete(0, END)
            entry_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
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
entry_website.focus()
label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)
entry_email = Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0,"test@gmail.com")
label_password = Label(text="Password:")
label_password.grid(row=3, column=0)
entry_password = Entry(width=21)
entry_password.grid(row=3, column=1)
button_generate_password = Button(text="Generate Pass", width=10)
button_generate_password.grid(row=3, column=2)
button_generate_password.config(command=generate_password)
button_add = Button(text="Add", width=36)
button_add.grid(row=4, column=1, columnspan=2)
button_add.config(command=save)



window.mainloop()

