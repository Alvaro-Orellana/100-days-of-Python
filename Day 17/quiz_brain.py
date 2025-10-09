from typing import Optional
from question_model import Question

class QuizBrain:
    def __init__(self, questions: list[Question]):
        self.questions = questions
        self.current_question: Optional[Question] = questions[0]
        self.score = 0

    def get_question(self) -> Optional[Question]:
        try:
            # Get index of the next question and update current_question with it
            current_index = self.questions.index(self.current_question)
            current_question = self.current_question
            self.current_question = self.questions[current_index + 1]
            return current_question

        except (ValueError, IndexError):
            return None



    def get_final_score(self) -> str:
        return f"{self.score}/{len(self.questions)}"

    def get_user_answer(self) -> str:
        return input(f"Q.{self.question_number} {self.current_question.question}. (True/False)?: ").lower()
