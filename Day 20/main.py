from turtle import Turtle, Screen
import time

CUBE_WIDTH = 20

def draw_initial_snake() -> list[Turtle]:
    snake = []
    for i in range(3):
        cube = Turtle("square")
        cube.color("white")
        cube.penup()
        cube.backward(CUBE_WIDTH * i)
        snake.append(cube)
    return snake

def move_snake(snake):
    for index in range(len(snake)):
        if index == len(snake) - 1:
            # Move head
            snake[index].forward(CUBE_WIDTH)
        else:
            # move Nth cube to Nth+1 cube position
            next_cube_xcor = snake[index + 1].xcor()
            next_cube_ycor = snake[index + 1].ycor()
            snake[index].goto(next_cube_xcor, next_cube_ycor)

def move_up():
    if head.heading() == 0:
        head.left(90)
    if head.heading() == 180:
        head.right(90)

def move_down():
    if head.heading() == 0:
        head.right(90)
    if head.heading() == 180:
        head.left(90)

def move_left():
    if head.heading() == 90:
        head.left(90)
    if head.heading() == 270:
        head.right(90)

def move_right():
    if head.heading() == 90:
        head.right(90)
    if head.heading() == 270:
        head.left(90)

screen = Screen()
snake: list[Turtle] = []

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game 🐍🐍🐍")
screen.listen()


screen.tracer(0)
snake = draw_initial_snake()
screen.update()
head = snake[len(snake) - 1]

screen.onkey(key="Up", fun=move_up)
screen.onkey(key="Down", fun=move_down)
screen.onkey(key="Left", fun=move_left)
screen.onkey(key="Right", fun=move_right)

game_is_over = False
while not game_is_over:
    move_snake(snake)
    screen.update()
    time.sleep(0.1)



screen.exitonclick()