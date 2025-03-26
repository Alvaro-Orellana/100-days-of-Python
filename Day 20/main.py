import turtle
from turtle import Screen, Turtle
from snake import Snake
from time import sleep
from random import randrange

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
MAX_X_COORDINATE, MIN_X_COORDINATE = SCREEN_WIDTH // 2, -SCREEN_WIDTH // 2
MAX_Y_COORDINATE, MIN_Y_COORDINATE = SCREEN_HEIGHT // 2, -SCREEN_HEIGHT // 2
DELAY_IN_SECONDS = 0.1

def move_food_to_random_location(food: Turtle):
    random_x = randrange(start=MIN_X_COORDINATE + snake.square_width,
                         stop=MAX_X_COORDINATE + 1 - snake.square_width,
                         step=snake.square_width)

    random_y = randrange(start=MIN_Y_COORDINATE + snake.square_width,
                         stop=MAX_Y_COORDINATE + 1 - snake.square_width,
                         step=snake.square_width)
    food.goto(random_x, random_y)


def detect_walls_collision(snake: Snake) -> bool:
    """Returns true if a collision is detected, otherwise false."""
    if snake.is_going_up(): return  snake.head_edge_coordinate() > MAX_Y_COORDINATE
    if snake.is_going_down(): return  snake.head_edge_coordinate() < MIN_Y_COORDINATE
    if snake.is_going_left(): return snake.head_edge_coordinate() < MIN_X_COORDINATE
    if snake.is_going_right(): return snake.head_edge_coordinate() > MAX_X_COORDINATE

    return False

def detect_collision(body1: Turtle, body2: Turtle) -> bool:
    """Returns true if a collision is detected, otherwise false."""
    return round(body1.xcor()) == round(body2.xcor()) and round(body1.ycor()) == round(body2.ycor())

def detect_tail_collision(snake: Snake) -> bool:
    """Returns true if a head collides with tail, otherwise false."""
    tail = snake.body[1:]
    for square in tail:
        if detect_collision(snake.head, square):
            return True
    return False

# Variables
score = 0
snake = Snake()
screen = Screen()
pen = Turtle(visible=False)
food = Turtle("square")

# setup screen
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My snake game 🐍🐍🐍")
screen.tracer(0)
screen.listen()
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)

# setup pen
pen.penup()
pen.color("white")
pen.goto(MIN_X_COORDINATE + 10, MIN_Y_COORDINATE + 10)  # Bottom-left with small offset

#setup food
food.color("blue")
food.penup()
move_food_to_random_location(food)

while True:
    if detect_walls_collision(snake) or detect_tail_collision(snake):
        break
    if detect_collision(snake.head, food):
        score += 1
        move_food_to_random_location(food)
        snake.grow_tail()

    snake.move()

    pen.clear()
    pen.write(f"head x: {snake.head.xcor()} y: {snake.head.ycor()} | food x: {food.xcor()} y: {food.ycor()} \tscore: {score}")

    screen.update()
    sleep(DELAY_IN_SECONDS)

screen.title("Game Over")
pen.clear()
pen.write(f"GAME OVER. Score: {score}")
screen.mainloop()