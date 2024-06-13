THEME_COLOR = "#375362"
from tkinter import *

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, background=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, background=THEME_COLOR, highlightthickness=0)
        self.score_text = Label(text='Score: 0',  font=("Arial", 20, "bold"), bg=THEME_COLOR, fg='white')
        self.score_text.grid(row=0, column=1)

        self.question_text = self.canvas.create_text(150, 125, text='Question is here', 
                                                     font=("Arial", 20, "italic"), justify='center',
                                                     )
        self.canvas.config(bg='white')
        self.canvas.grid(row=1,column=0, columnspan=2)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, padx=20, pady=20)
        self.true_button.grid(row=2, column=0, pady=20)
    
        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, padx=20, pady=20)
        self.false_button.grid(row=2, column=1, pady=20)




        self.window.mainloop()
    
