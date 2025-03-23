import colorgram
from turtle import Turtle, Screen

#colors = colorgram.extract('image.jpg', 30)
#colors_tuples = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors][3:]
#print(colors_tuples)

starting_coordinate = (-300,-300)
circle_distance = 50

screen = Screen()
turtle = Turtle()
turtle.speed("fastest")
turtle.penup()
turtle.goto(starting_coordinate)
turtle.pendown()

for i in range(1,11):
    for j in range(10):
        turtle.circle(20)
        turtle.penup()
        turtle.goto(turtle.xcor() + circle_distance, turtle.ycor())
        turtle.pendown()

    turtle.penup()
    turtle.goto(starting_coordinate[0], starting_coordinate[1] + circle_distance * i)
    turtle.pendown()


screen.mainloop()