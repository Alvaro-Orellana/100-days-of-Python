import turtle

FONT = ("Arial", 24, "normal")

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-240, 260)
        self.write("Score: 0", align="center", font=FONT)

    def update_score(self, score):
        self.clear()
        self.write(f"Score: {score}", align="center", font=FONT)

    def display_game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=("Arial", 44, "normal"))
