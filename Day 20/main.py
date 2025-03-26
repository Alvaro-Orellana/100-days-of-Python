import turtle
from turtle import Screen, Turtle
from snake import Snake
from time import sleep
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
MAX_X_COORDINATE, MIN_X_COORDINATE = SCREEN_WIDTH // 2, -SCREEN_WIDTH // 2
MAX_Y_COORDINATE, MIN_Y_COORDINATE = SCREEN_HEIGHT // 2, -SCREEN_HEIGHT // 2

def move_food_to_random_location(food: Turtle):
    random_x = random.randrange(start=MIN_X_COORDINATE + snake.CUBE_WIDTH,
                                stop=MAX_X_COORDINATE + 1 - snake.CUBE_WIDTH,
                                step=snake.CUBE_WIDTH)

    random_y = random.randrange(start=MIN_Y_COORDINATE + snake.CUBE_WIDTH,
                                stop=MAX_Y_COORDINATE + 1 - snake.CUBE_WIDTH,
                                step=snake.CUBE_WIDTH)
    food.goto(random_x, random_y)


def detect_walls_collision(snake: Snake) -> bool:
    """Returns true if a collision is detected, otherwise false."""
    if snake.is_going_right(): return snake.head_edge_coordinate() > MAX_X_COORDINATE
    if snake.is_going_left(): return snake.head_edge_coordinate() < MIN_X_COORDINATE
    if snake.is_going_up(): return  snake.head_edge_coordinate() > MAX_Y_COORDINATE
    if snake.is_going_down(): return  snake.head_edge_coordinate() < MIN_Y_COORDINATE

    return False

def detect_collision(body1: Turtle, body2: Turtle) -> bool:
    """Returns true if a collision is detected, otherwise false."""
    return round(body1.xcor()) == round(body2.xcor()) and round(body1.ycor()) == round(body2.ycor())

def detect_tail_collision(snake: Snake) -> bool:
    """Returns true if a collision is detected, otherwise false."""
    for index in range(len(snake.body) - 1):
        if detect_collision(snake.head, snake.body[index]):
            return True
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

score = 0

food = Turtle("square")
food.color("blue")
food.penup()
move_food_to_random_location(food)

pen = Turtle()
pen.hideturtle()
pen.penup()
pen.goto(-SCREEN_WIDTH // 2 + 10, -SCREEN_HEIGHT // 2 + 10)  # Bottom-left with small offset
pen.color("white")

loops = 0
while True:
    if detect_walls_collision(snake):
        break

    if detect_collision(snake.head, food):
        score += 1
        move_food_to_random_location(food)
        snake.grow_tail()

    #if detect_tail_collision(snake):
    #    for square in range(len(snake.body)):
    #        snake.body[square].color("red")
    #    break

    snake.move()

    pen.clear()
    message = f"head x: {snake.head.xcor()} y: {snake.head.ycor()} | food x: {food.xcor()} y: {food.ycor()} \tscore: {score}"
    pen.write(message, font=("Arial", 12, "normal"))

    screen.update()
    sleep(0.1)

    loops += 1

screen.title("Game Over")

screen.mainloop()