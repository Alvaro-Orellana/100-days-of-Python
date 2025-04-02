import turtle

FONT = ("Arial", 24, "bold")

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        self.max_score = 0
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
        self.score = 0
        self.write_score()