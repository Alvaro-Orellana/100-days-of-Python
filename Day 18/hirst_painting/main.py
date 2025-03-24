import colorgram
import random
from turtle import Turtle, Screen

colors = colorgram.extract('image.jpg', 30)
rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors][5:]

(x_origin, y_origin) = (-300, -300)
interdot_distance = 50

screen = Screen()
screen.colormode(255)

turtle = Turtle()
turtle.speed("fastest")
turtle.penup()
turtle.hideturtle()
turtle.goto((x_origin, y_origin))

for i in range(1,11):
    for j in range(10):
        turtle.dot(20, random.choice(rgb_colors))
        turtle.goto(turtle.xcor() + interdot_distance, turtle.ycor())

    turtle.goto(x_origin, y_origin + interdot_distance * i)

screen.mainloop()