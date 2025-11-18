from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg='white', bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250)
        self.main_text = self.canvas.create_text(150, 125, text="Kanye Quote Goes HERE", width=290, font=("Arial", 20, "italic"), fill="black")

        check_img = PhotoImage(file="images/true.png")
        cross_img = PhotoImage(file="images/false.png")
        self.check_button = Button(image=check_img, highlightthickness=0, command=lambda : self.user_submitted_answer(True))
        self.cross_button = Button(image=cross_img, highlightthickness=0, command=lambda : self.user_submitted_answer(False))

        # ui positioningx1
        self.score_label.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.check_button.grid(row=2, column=0)
        self.cross_button.grid(row=2, column=1)

        self.next_question()
        self.window.mainloop()

    def user_submitted_answer(self, user_answer: bool):
        if self.quiz_brain.answer_is_correct(user_answer):
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            self._flash_canvas(correct=True)
        else:
            self._flash_canvas(correct=False)
        self.next_question()

    def _flash_canvas(self, correct: bool):
        self.canvas.config(bg='green' if correct else 'red')
        self.window.after(400, lambda: self.canvas.config(bg='white'))

    def next_question(self):
        if next_question := self.quiz_brain.next_question():
            self.canvas.itemconfig(self.main_text, text=next_question)
        else:
            self.check_button.config(state='disabled')
            self.cross_button.config(state='disabled')
            final_message = f"You've completed the quiz \nYour final score was: {self.quiz_brain.score}/{self.quiz_brain.question_number}"
            self.canvas.itemconfig(self.main_text, text=final_message)
