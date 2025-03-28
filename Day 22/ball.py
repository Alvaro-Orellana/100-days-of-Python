import random
from turtle import Turtle

class Ball(Turtle):
    def __init__(self, initial_speed: int):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.initial_speed = initial_speed
        self.dx = initial_speed
        self.dy = initial_speed
        self.reset()

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_x(self): self.dx *= -1
    def bounce_y(self): self.dy *= -1
    def is_going_left(self) -> bool: return self.dx < 0
    def increase_speed(self):
        d_velocity = -0.5 if self.dx < 0 else 0.5
        self.dx += d_velocity

    def reset(self):
        self.goto(0, 0)
        self.dx = self.initial_speed * random.choice([-1, 1])
        self.dy = self.initial_speed * random.choice([-1, 1])


class Paddle(Turtle):
    def __init__(self, pad_length: int=4, velocity: int=18):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.setheading(90) # point up
        self.shapesize(stretch_len=pad_length)
        self.velocity = velocity

    def move_up(self): self.forward(self.velocity)
    def move_down(self): self.backward(self.velocity)
    def touches(self, object: Turtle) -> bool: return self.distance(object) < 20


class Scoreboard(Turtle):
    FONT = ('Arial', 30, 'normal')

    def __init__(self):
        super().__init__()
        self.left_paddle_score = 0
        self.right_paddle_score = 0
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.left_paddle_score}\t\t{self.right_paddle_score}", align="center", font=self.FONT)