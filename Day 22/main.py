from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

BALL_SPEED = 2
WIDTH = 800
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

def ball_touches_left_or_right_wall(ball: Ball) -> bool:
    return ball.xcor() <= MIN_X_COORDINATE or ball.xcor() >= MAX_X_COORDINATE

def ball_touches_up_or_down_wall(ball: Ball) -> bool:
    return ball.ycor() >= MAX_Y_COORDINATE or ball.ycor() <= MIN_Y_COORDINATE

screen = Screen()
canvas = screen.getcanvas()
left_paddle = Paddle()
right_paddle = Paddle()
ball = Ball(BALL_SPEED)
scoreboard = Scoreboard()

scoreboard.goto(0, MAX_X_COORDINATE - 40)

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

while True:
    ball.move()

    paddle = right_paddle if ball.is_going_left() else left_paddle
    if paddle.touches(ball):
        ball.bounce_x()
        continue

    if ball_touches_up_or_down_wall(ball):
        ball.bounce_y()
        continue

    if ball_touches_left_or_right_wall(ball):
        if ball.is_going_left():
            scoreboard.left_paddle_score += 1
        else:
            scoreboard.right_paddle_score += 1
        ball.reset()
        scoreboard.show_score()

    screen.update()

