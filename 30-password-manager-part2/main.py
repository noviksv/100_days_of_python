from tkinter import messagebox
from tkinter import *
import json

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
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if not website or not email or not password:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return
    try:
        with open("data.json", "r") as data:
            #read old data
            python_data = json.load(data)
            
    except FileNotFoundError:
        with open("data.json", "w") as data:
            #create new file with first data
            json.dump(new_data, data, indent=4)
    else:
        #update old data with new data
        python_data.update(new_data)
        with open("data.json", "w") as data:
            json.dump(python_data, data, indent=4)
    finally:

        entry_website.delete(0, END)
        entry_password.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = entry_website.get()
    try:
        with open("data.json", "r") as data:
            #read old data
            python_data = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in python_data:
            email = python_data[website]["email"]
            password = python_data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

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
entry_website = Entry(width=21)
entry_website.grid(row=1, column=1, columnspan=1)
entry_website.focus()
button_search = Button(text="Search", width=10)
button_search.grid(row=1, column=2)
button_search.config(command=search_password)
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

