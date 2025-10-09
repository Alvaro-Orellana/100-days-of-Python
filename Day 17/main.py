from data import questions
from quiz_brain import QuizBrain

quiz_brain = QuizBrain(questions)

while question := quiz_brain.get_question():
    correct_answer = question.correct_answer.lower()
    user_answer = quiz_brain.get_user_answer()

    if user_answer == correct_answer:
        quiz_brain.score += 1
        print("You got it right!")
    else:
        print("Sorry, that's wrong.")

    print(f"The correct answer was {correct_answer}.")
    print(f"Your current score is {quiz_brain.score}.")

print("You completed the quiz", f"Your final score was {quiz_brain.get_final_score()}.")


