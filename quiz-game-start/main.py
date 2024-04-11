from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# add type ann anotations to the question_bank list
question_bank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)
print(quiz_brain.next_question())

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz_brain.correct_answers}/{quiz_brain.question_number}")