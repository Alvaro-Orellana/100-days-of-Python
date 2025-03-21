from question_model import Question

class QuizBrain():
    def __init__(self, question_list: list[Question]):
        self.question_list = question_list
        self.question_number = 0
        self.current_question = None

    def next_question(self) -> Question:
        if self.there_are_questions_left():
            question = self.question_list[self.question_number]
            self.current_question = question
            self.question_number += 1
            return question

    def get_user_answer(self) -> str:
        return input(f"Q.{self.question_number} {self.current_question.question}. (True/False)?: ").lower()

    def there_are_questions_left(self) -> bool:
        return self.question_number < len(self.question_list)

