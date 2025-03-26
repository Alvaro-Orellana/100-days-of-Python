from turtle import Turtle
from turtledemo.penrose import start


class Snake:

    CUBE_WIDTH = 20
    INITIAL_NUMBER_OF_CUBES = 3
    DIRECTIONS = {"right": 0, "up": 90, "left": 180, "down": 270} # turtle's module directions in degrees

    def __init__(self, color: str="white"):
        self.body: list[Turtle] = []
        self.color: str = color

        # create initial snake
        for i in range(self.INITIAL_NUMBER_OF_CUBES):
            cube = Turtle("square")
            cube.color(self.color)
            cube.penup()
            #puts the cubes horizontally next to each other
            cube.backward(self.CUBE_WIDTH * i)
            self.body.append(cube)

        self.head = self.body[0]

    def move(self):
        """first moves tail to the next cube's position and then moves the head"""

        # move tail
        for index in range(len(self.body) - 1, 0, -1):
            # move Nth cube to Nth+1 cube position
            next_xcor = self.body[index - 1].xcor()
            next_ycor = self.body[index - 1].ycor()
            self.body[index].goto(next_xcor, next_ycor)

        # move head
        self.head.forward(self.CUBE_WIDTH)

    def move_up(self):
        if not self.is_going_down():
            self.turn("up")

    def move_down(self):
        if not self.is_going_up():
            self.turn("down")

    def move_left(self):
        if not self.is_going_right():
            self.turn("left")

    def move_right(self):
        if not self.is_going_left():
            self.turn("right")

    def turn(self, direction: str):
        self.head.setheading(self.DIRECTIONS[direction])
        self.head.forward(Snake.CUBE_WIDTH)

    def head_edge_coordinate(self) -> float:
        # xcor() and ycor() are in the center of a shape.
        # so the square's edge is located on that point plus half the square's size
        square_edge_offset = self.CUBE_WIDTH / 2

        if self.is_going_right(): return self.head.xcor() + square_edge_offset
        elif self.is_going_left(): return self.head.xcor() - square_edge_offset
        elif self.is_going_up(): return self.head.ycor() + square_edge_offset
        elif self.is_going_down(): return self.head.ycor() - square_edge_offset
        else: pass # should never reach here. throw an error?

    def is_going_left(self) -> bool: return self.head.heading() == self.DIRECTIONS["left"]
    def is_going_right(self) -> bool: return self.head.heading() == self.DIRECTIONS["right"]
    def is_going_up(self) -> bool: return self.head.heading() == self.DIRECTIONS["up"]
    def is_going_down(self) -> bool: return self.head.heading() == self.DIRECTIONS["down"]

    def grow_tail(self):
        new_square = Turtle("square")
        new_square.color(self.color)
        new_square.penup()
        new_square.goto(self.body[0].xcor(), self.body[0].ycor())
        new_square.setheading(self.body[0].heading())
        new_square.back(self.CUBE_WIDTH)
        self.body.insert(0, new_square)