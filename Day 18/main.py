from turtle import Turtle, Screen
from random import random

def draw_square(turtle: Turtle, distance):
    for _ in range(4):
        turtle.forward(distance)
        turtle.right(90)

def random_color():
    r = random()
    g = random()
    b = random()
    turtle.pencolor((r, g, b))

screen = Screen()
turtle = Turtle()
turtle.pensize(3)

for sides in range(3,11):
    angle = 360 / sides
    random_color()
    for side in range(sides):
        turtle.forward(100)
        turtle.right(angle)

#draw_square(turtle, 100)

screen.mainloop()
