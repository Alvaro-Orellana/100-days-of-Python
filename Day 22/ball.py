import random
import time
import turtle

class Ball(turtle.Turtle):

    def __init__(self, ball_speed: int):
        super().__init__()
        self.ball_speed = ball_speed
        self.shape("circle")
        self.color("white")
        self.penup()

        self.dx = 1 # x direction either 1 for left or -1 for right
        self.dy = 1 # y direction either 1 for up or -1 for down
        self.reset()

    def move(self):
        new_x = self.xcor() + self.ball_speed * self.dx
        new_y = self.ycor() + self.ball_speed * self.dy
        self.goto(new_x, new_y)

    def bounce_x(self):
       self.dx *= -1

    def bounce_y(self):
        self.dy *= -1

    def is_going_left(self) -> bool:
        return self.dx == 1

    def reset(self):
        self.goto(0, 0)
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        time.sleep(0.8)
