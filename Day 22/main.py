import time
from turtle import Turtle, Screen
from ball import Ball, Paddle, Scoreboard

BALL_SPEED = 2
WIDTH = 800
HEIGHT = 600
MIN_X_COORDINATE, MAX_X_COORDINATE = -WIDTH // 2, WIDTH // 2
MIN_Y_COORDINATE, MAX_Y_COORDINATE = -HEIGHT // 2, HEIGHT // 2

def position_paddles():
    left_paddle.setx(MIN_X_COORDINATE + 40)
    right_paddle.setx(MAX_X_COORDINATE - 40)

def draw_middle_line():
    t = Turtle()
    t.penup()
    t.color("white")
    t.goto(0, MAX_Y_COORDINATE) # Start at the top center
    t.setheading(270)  # Face down

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
left_paddle = Paddle()
right_paddle = Paddle()
ball = Ball(BALL_SPEED)
scoreboard = Scoreboard()

# setup screen
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.onkey(key="w", fun=left_paddle.move_up)
screen.onkey(key="s", fun=left_paddle.move_down)
screen.onkey(key="Up", fun=right_paddle.move_up)
screen.onkey(key="Down", fun=right_paddle.move_down)
screen.listen()

scoreboard.goto(0, MAX_Y_COORDINATE - 20)
position_paddles()
draw_middle_line()

while True:
    ball.move()
    screen.update()

    paddle = left_paddle if ball.is_going_left() else right_paddle
    if paddle.touches(ball):
        ball.bounce_x()
        ball.increase_speed()

    if ball_touches_up_or_down_wall(ball):
        ball.bounce_y()

    if ball_touches_left_or_right_wall(ball):
        if ball.is_going_left():
            scoreboard.left_paddle_score += 1
        else:
            scoreboard.right_paddle_score += 1
        ball.reset()
        scoreboard.update_score()
        time.sleep(0.8)