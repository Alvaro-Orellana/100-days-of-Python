from turtle import Screen
from snake import Snake
from time import sleep

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
MAX_X_COORDINATE, MIN_X_COORDINATE = SCREEN_WIDTH / 2, -SCREEN_WIDTH / 2
MAX_Y_COORDINATE, MIN_Y_COORDINATE = SCREEN_HEIGHT / 2, -SCREEN_HEIGHT / 2

def detect_walls_collision(snake: Snake) -> bool:
    """Returns true if a collision is detected, otherwise false."""
    if snake.is_going_right(): return snake.head_edge_coordinate() > MAX_X_COORDINATE
    if snake.is_going_left(): return snake.head_edge_coordinate() < MIN_X_COORDINATE
    if snake.is_going_up(): return  snake.head_edge_coordinate() > MAX_Y_COORDINATE
    if snake.is_going_down(): return  snake.head_edge_coordinate() < MIN_Y_COORDINATE

    return False

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My snake game 🐍🐍🐍")
screen.listen()

screen.tracer(0)
snake = Snake()
screen.update()

screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

while True:
    if detect_walls_collision(snake):
        break
    snake.move()
    screen.update()
    sleep(0.2)

screen.title("Game Over")

screen.exitonclick()