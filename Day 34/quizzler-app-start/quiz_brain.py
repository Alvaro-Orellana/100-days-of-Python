import html
from question_model import Question

class QuizBrain:
    def __init__(self, q_list: list[Question]):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self) -> str | None:
        self.question_number += 1
        if self.question_number < len(self.question_list): # there are quetions left
            current_question = self.question_list[self.question_number]
            return f"Q.{self.question_number}: {html.unescape(current_question.text)} (True/False): "
        else:
            return None

    def answer_is_correct(self, user_answer: bool) -> bool:
        current_question = self.question_list[self.question_number]
        if str(user_answer) == current_question.answer:
            self.score += 1
            return True
        else:
            return False
