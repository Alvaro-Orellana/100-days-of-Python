from turtle import Turtle, Screen
from random import random, choice

def draw_square(turtle: Turtle, distance):
    for _ in range(4):
        turtle.forward(distance)
        turtle.right(90)

def random_color():
    r, g, b = random(), random(), random()
    turtle.pencolor((r, g, b))

def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for side in range(number_of_sides):
        turtle.forward(100)
        turtle.right(angle)

def draw_shapes():
    for sides in range(3, 11):
        random_color()
        draw_shape(sides)

def random_walk():
    turtle.speed(3)
    while True:
        random_color()
        random_angle = choice([0,90,180,270])
        turtle.setheading(random_angle)
        turtle.forward(30)

def draw_spirograph(radius: float, angle: int):
    for angle in range(0, 361, angle):
        random_color()
        turtle.circle(radius=radius)
        turtle.setheading(angle)

def draw_many_spirographs(n: int):
    j = 1
    k = 0
    distance = radius*2
    for i in range(n):
        draw_spirograph(radius=radius, angle=7)
        if i % 2 != 0:
            turtle.goto(center[0] + distance*j, center[1] + distance*k)
        else:
            turtle.goto(center[0] + distance*k, center[1] + distance*j)

        j *= -1

screen = Screen()
turtle = Turtle()

turtle.pensize(2)
turtle.speed("fastest")
center = (turtle.xcor(), turtle.ycor())
radius = 150

draw_many_spirographs(5)


#turtle.goto(center[0] + radius*2, center[1])
#draw_spirograph(radius=radius, angle=7)
#turtle.goto(center[0] - radius*2, center[1])
#draw_spirograph(radius=radius, angle=7)
#turtle.goto(center[0], center[1] + radius*2)
#draw_spirograph(radius=radius, angle=7)
#turtle.goto(center[0], center[1] - radius*2)
#draw_spirograph(radius=radius, angle=7)

#draw_shapes()
#random_walk()
#draw_shapes()
#draw_square(turtle, 100)

screen.mainloop()
