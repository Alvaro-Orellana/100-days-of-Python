from turtle import Turtle, Screen

def main():
    turtle = Turtle()
    screen = Screen()

    screen.listen()

    screen.onkey(key="w", fun=lambda: turtle.forward(10))
    screen.onkey(key="s", fun=lambda: turtle.backward(10))
    screen.onkey(key="a", fun=lambda: turtle.left(10))
    screen.onkey(key="d", fun=lambda: turtle.right(10))
    screen.onkey(key="c", fun=turtle.clear)

    print("Press w to go forward")
    print("s to go backward")
    print("a to go left")
    print("d to go right")
    print("and c to clear the screen")

    screen.mainloop()

if __name__ == '__main__':
    main()