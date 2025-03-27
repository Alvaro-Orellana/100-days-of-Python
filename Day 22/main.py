from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
import random

WIDTH = 600
HEIGHT = 600

MIN_X_COORDINATE, MAX_X_COORDINATE = -WIDTH // 2, WIDTH // 2
MIN_Y_COORDINATE, MAX_Y_COORDINATE = -HEIGHT // 2, HEIGHT // 2

def position_paddles():
    left_paddle.move_xcoor(MIN_X_COORDINATE + 40)
    right_paddle.move_xcoor(MAX_X_COORDINATE - 40)

def draw_middle_line():
    t = Turtle()
    t.penup()
    t.color("white")
    t.goto(0, MAX_Y_COORDINATE) # Start at the top center
    t.setheading(270)  # Face downward

    for _ in range(HEIGHT // 20):
        t.pendown()
        t.forward(10)  # Draw a short segment
        t.penup()
        t.forward(10)  # Leave a gap

def ball_touches_wall(ball: Turtle, wall_name: str) -> bool:
    if wall_name == "left": return ball.xcor() <= MIN_X_COORDINATE
    if wall_name == "right": return ball.xcor() >= MAX_X_COORDINATE
    if wall_name == "up": return ball.ycor() >= MAX_Y_COORDINATE
    if wall_name == "down": return ball.ycor() <= MIN_Y_COORDINATE

    return False

screen = Screen()
canvas = screen.getcanvas()
left_paddle = Paddle()
right_paddle = Paddle()
scoreboard = Scoreboard()
ball = Turtle(shape="circle")

ball.penup()
ball.color("white")

scoreboard.goto(0, MAX_X_COORDINATE - 40)
scoreboard.show_score()

screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.tracer(0)
screen.onkey(key="q", fun=left_paddle.move_up)
screen.onkey(key="a", fun=left_paddle.move_down)
screen.onkey(key="Up", fun=right_paddle.move_up)
screen.onkey(key="Down", fun=right_paddle.move_down)
screen.listen()

position_paddles()
draw_middle_line()

x_direction = 1
y_direction = 1


while True:
    ball.forward(3 * x_direction)

    if ball_touches_wall(ball, "up"):
        pass
    elif ball_touches_wall(ball, "down"):
        pass

    if x_direction == 1: # ball going to the right
        if right_paddle.touches(ball):
            x_direction *= -1

        if ball_touches_wall(ball, "right"):
            scoreboard.left_paddle_score += 1
            ball.goto(0, 0)
            x_direction = random.choice([-1, 1])


    elif x_direction == -1: # ball going to the left
        if left_paddle.touches(ball):
            x_direction *= -1

        if ball_touches_wall(ball, "left"):
            scoreboard.right_paddle_score += 1
            ball.goto(0, 0)
            x_direction = random.choice([-1, 1])


    scoreboard.show_score()
    screen.update()
