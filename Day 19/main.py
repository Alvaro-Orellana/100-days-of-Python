from turtle import Screen, Turtle
import random

WIDTH = 800
HEIGHT = 600
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "violet"]
NUMBER_OF_TURTLES = len(rainbow_colors)
turtles = []
race_is_finished = False
winner = None
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)

for i in range(NUMBER_OF_TURTLES):
    turtle = Turtle("turtle")
    turtle.color(rainbow_colors[i])
    turtle.penup()
    turtle.goto(x=(-WIDTH / 2) + 40, y=(-HEIGHT / 2) + 70 * (i+1))
    turtles.append(turtle)

user_bet = screen.textinput("Choose a turtle", "enter a color to place your bet")

while not race_is_finished:
    for turtle in turtles:
        if turtle.xcor() >= (WIDTH / 2) - 20 :
            race_is_finished = True
            winner = turtle

        turtle.forward(random.randint(1, 10))

screen.title(f"the winner is {winner}")
screen.mainloop()