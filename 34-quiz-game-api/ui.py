THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
from tkinter import *

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        
        self.score_label = Label(self.window, text="Score: 0", font=("Arial", 20),fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.question_text = self.canvas.create_text(150, 
                                                     125, 
                                                     text="Question is HERE", 
                                                     font=("Arial", 20, "italic"), 
                                                     fill="black", width=280, 
                                                     justify="center")
        self.canvas.config(bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        right_button_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_button_img, highlightthickness=0, padx=20, pady=20, 
                                   command=self.got_it_right)
        self.right_button.grid(row=2, column=0, pady=20)

        wrong_button_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_button_img, highlightthickness=0, padx=20, pady=20,
                                    command=self.got_it_wrong)
        self.wrong_button.grid(row=2, column=1, pady=20)  # Add padx=10 for left and right padding
        
        
        self.get_next_question()

        
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
        


    def got_it_right(self):
        is_right = self.quiz.check_answer(user_answer='True')
        self.give_feedback_to_user(is_right=is_right)

        

    def got_it_wrong(self):
        is_right =  self.quiz.check_answer('False')
        self.give_feedback_to_user(is_right=is_right)


    def give_feedback_to_user(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000 ,self.get_next_question)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        #self.window.after(1000 ,lambda: self.canvas.config(bg="white")  )  