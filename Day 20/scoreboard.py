from turtle import Turtle

FONT = ("Arial", 24, "bold")

def read_max_score():
    with open("data.txt") as file:
        max_score = file.read()
        return int(max_score)

def write_max_score(max_score: int):
    with open("data.txt", "w") as file:
        file.write(str(max_score))

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        self.max_score = read_max_score()
        self.penup()
        self.color("white")
        self.sety(270)
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Your score: {self.score}  Max Score: {self.max_score}", align="center", font=FONT)

    def reset(self):
        if self.score > self.max_score:
            self.max_score = self.score
            write_max_score(self.max_score)
        self.score = 0
        self.write_score()