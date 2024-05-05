import tkinter

def button_click():
    print("Button was clicked!")
    #change the text of the label
    label.config(text=input_field.get())



root = tkinter.Tk()
root.title("Hello, World!")
#define the size of the window
root.geometry("800x600")
#create a label widget
label = tkinter.Label(root, text="Hello, World!", font=("Arial", 24, "bold"))
#pack the label widget
label.pack(side="left")

#add input field with default text

input_field = tkinter.Entry(root, width=10)
input_field.insert(0, 'Default')
input_field.pack()
print(input_field.get())


#create a button widget
button = tkinter.Button(root, text="Click me!", font=("Arial", 24, "bold"))
button.pack(side="right")
#bind the button to a function
button.config(command=button_click)



root.mainloop()