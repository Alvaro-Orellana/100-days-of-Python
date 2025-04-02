import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
SCREEN_HEIGHT = 600

class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=2)
        self.setheading(180)
        random_y = random.randint(-SCREEN_HEIGHT // 2 + 50, SCREEN_HEIGHT // 2 -50)
        self.goto(300, random_y)
