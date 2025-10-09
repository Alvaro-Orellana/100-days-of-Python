import turtle as t
import time
from car import Car
from scoreboard import Scoreboard

FINISH_LINE = 280
CAR_SPEED = 20

def move_up():
    turtle.forward(20)

def move_down():
    turtle.back(20)

def advance_cars():
    for car in cars:
        car.forward(CAR_SPEED)

def clear_cars():
    for car in cars:
        car.hideturtle()
    cars.clear()

def turtle_collides_with_cars():
    for car in cars:
        if car.distance(turtle) < 27:
            return True
    return False

def next_level():
    global score; score += 1
    global CAR_SPEED; CAR_SPEED += 5
    clear_cars()
    turtle.sety(-300 + 20)
    scoreboard.update_score(score)

screen = t.Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.onkey(key="Up", fun=move_up)
screen.onkey(key="Down", fun=move_down)
screen.listen()

turtle = t.Turtle(shape="turtle")
turtle.penup()
turtle.setheading(90)
turtle.sety(-300 + 20)

scoreboard = Scoreboard()
score = 0
loop_number = 1
cars: list[Car] = []
won_game = False

while True:
    if loop_number % 6 == 0:
        cars.append(Car())
    if loop_number % 400 == 0:
        clear_cars()
    if turtle_collides_with_cars():
        scoreboard.display_game_over()
        break#game_over()
    if turtle.ycor() >= FINISH_LINE: # turtle got to the finish line
        next_level()

    advance_cars()
    screen.update()
    time.sleep(0.1)
    loop_number += 1

screen.exitonclick()