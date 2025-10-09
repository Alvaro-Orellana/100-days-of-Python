from data import questions
from quiz_brain import QuizBrain

quizBrain = QuizBrain(questions)

while question := quizBrain.get_question():
    correct_answer = question.correct_answer.lower()
    user_answer = quizBrain.get_user_answer()

    if user_answer == correct_answer:
        quizBrain.score += 1
        print("You got it right!")
    else:
        print("Sorry, that's wrong.")

    print(f"The correct answer was {correct_answer}.")
    print(f"Your current score is {quizBrain.score}.")

print("You completed the quiz", f"Your final score was {quizBrain.get_final_score()}.")


