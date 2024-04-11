class QuizBrain:
    # static variable, common to all instances of the class
    description = "This class will be responsible for keeping track of the score and asking the questions."

    # constructor, attributes inside are specific to each instance of the class
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.correct_answers = 0

    #methods, functions inside are specific to each instance of the class
    def next_question(self):
        user_answer = input(
            f"Q{self.question_number + 1}. {self.question_list[self.question_number].text} (True/False):"
        )
        self.question_number += 1
        self.check_answer(
            user_answer, self.question_list[self.question_number - 1].answer
        )

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.correct_answers += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.correct_answers}/{self.question_number}")
