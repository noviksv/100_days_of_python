THEME_COLOR = "#375362"

from tkinter import *

class QuizInterface:

    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        
        self.score_label = Label(self.window, text="Score: 0", font=("Arial", 20),fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.question_text = self.canvas.create_text(150, 125, text="Question is HERE", font=("Arial", 20, "italic"), fill="black", width=250, justify="center")
        self.canvas.config(bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        right_button_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_button_img, highlightthickness=0, padx=20, pady=20)
        self.right_button.grid(row=2, column=0, pady=20)

        wrong_button_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_button_img, highlightthickness=0, padx=20, pady=20)
        self.wrong_button.grid(row=2, column=1, pady=20)  # Add padx=10 for left and right padding

        
        self.window.mainloop()
