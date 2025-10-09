from typing import Optional
from question_model import Question

class QuizBrain:
    def __init__(self, question_list: list[Question]):
        self.question_list = question_list
        self.next_question: Optional[Question] = question_list[0]
        self.score = 0

    def get_question(self) -> Optional[Question]:
        question = self.next_question
        try:
            current_index = self.question_list.index(question)
            self.next_question = self.question_list[current_index + 1]
        except ValueError:
            return None

        return question


    def get_final_score(self) -> str:
        return f"{self.score}/{len(self.question_list)}"

    def get_user_answer(self) -> str:
        return input(f"Q.{self.question_number} {self.next_question.question}. (True/False)?: ").lower()
