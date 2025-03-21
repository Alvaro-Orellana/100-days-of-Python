from data import questions
from quiz_brain import QuizBrain

quizBrain = QuizBrain(questions)
score = 0

while quizBrain.there_are_questions_left():
    q = quizBrain.next_question()
    user_answer = quizBrain.get_user_answer()

    if user_answer == q.correct_answer.lower():
        score += 1
        print("You got it right!")
    else:
        print("Sorry, that's wrong.")

    print(f"The correct answer was {q.correct_answer}.")
    print(f"Your current score is {score}/{quizBrain.question_number}.")
    print("\n")

print("You completed the quiz")
print(f"Your final score was {score}/{quizBrain.question_number}.")


