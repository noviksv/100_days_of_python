import tkinter

def button_click():
    print("Button was clicked!")

def main():
    root = tkinter.Tk()
    root.title("Hello, World!")
    #define the size of the window
    root.geometry("800x600")
    #create a label widget
    label = tkinter.Label(root, text="Hello, World!", font=("Arial", 24, "bold"))
    #pack the label widget
    label.pack(side="left")

    #create a button widget
    button = tkinter.Button(root, text="Click me!", font=("Arial", 24, "bold"))
    #pack the button widget
    button.pack(side="right")
    #bind the button to a function
    button.config(command=button_click)
    root.mainloop()

if __name__ == "__main__":
    main()