from turtle import Screen
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
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

game_is_over = False
while not game_is_over:
    snake.move()
    screen.update()
    time.sleep(0.1)



screen.exitonclick()