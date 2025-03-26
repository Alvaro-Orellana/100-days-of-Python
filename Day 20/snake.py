from turtle import Turtle

class Snake:

    DIRECTIONS = {"right": 0, "up": 90, "left": 180, "down": 270} # turtle's module directions in degrees

    def __init__(self, color: str="white", initial_number_of_cubes=3, square_width=20):
        self.body: list[Turtle] = []
        self.color: str = color
        self.square_width: int = square_width

        # create initial snake
        for i in range(initial_number_of_cubes):
            cube = Turtle("square")
            cube.color(self.color)
            cube.penup()
            cube.backward(self.square_width * i) #puts the cubes horizontally next to each other
            self.body.append(cube)

        self.head: Turtle = self.body[0]

    def move(self):
        """
        First moves tail to the next cube's position, then moves the head.
        Head is the first cube, tail is all the rest.
        """
        # Move tail. Starts at the last cube, shifting each to the next cube's position.
        tail_indices = range(1, len(self.body))
        for index in reversed(tail_indices):
            next_cube = self.body[index - 1]
            self.body[index].goto(x=next_cube.xcor(), y=next_cube.ycor())

        # Move head
        self.head.forward(self.square_width)

    def turn_up(self):
        if not self.is_going_down(): self.turn("up")

    def turn_down(self):
        if not self.is_going_up(): self.turn("down")

    def turn_left(self):
        if not self.is_going_right(): self.turn("left")

    def turn_right(self):
        if not self.is_going_left(): self.turn("right")

    def turn(self, direction: str):
        self.head.setheading(self.DIRECTIONS[direction])

    def head_edge_coordinate(self) -> float:
        # xcor() and ycor() are in the center of a shape.
        # so the square's edge is located on that point plus half the square's size
        square_edge_offset = self.square_width / 2

        if self.is_going_up(): return self.head.ycor() + square_edge_offset
        elif self.is_going_down(): return self.head.ycor() - square_edge_offset
        elif self.is_going_left(): return self.head.xcor() - square_edge_offset
        elif self.is_going_right(): return self.head.xcor() + square_edge_offset
        else: pass # should never reach here. throw an error?

    def is_going_up(self) -> bool: return self.head.heading() == self.DIRECTIONS["up"]
    def is_going_down(self) -> bool: return self.head.heading() == self.DIRECTIONS["down"]
    def is_going_left(self) -> bool: return self.head.heading() == self.DIRECTIONS["left"]
    def is_going_right(self) -> bool: return self.head.heading() == self.DIRECTIONS["right"]

    def grow_tail(self):
        new_square = Turtle("square")
        new_square.color(self.color)
        new_square.penup()
        new_square.goto(self.body[-1].xcor(), self.body[-1].ycor())
        new_square.setheading(self.body[-1].heading())
        new_square.backward(self.square_width)
        self.body.append(new_square)
