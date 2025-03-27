from turtle import Turtle

FONT = ('Arial', 30, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_paddle_score = 0
        self.right_paddle_score = 0
        self.color("white")
        self.hideturtle()


    def show_score(self):
        self.clear()
        self.write(f"{self.left_paddle_score}\t\t{self.right_paddle_score}", align="center", font=FONT)