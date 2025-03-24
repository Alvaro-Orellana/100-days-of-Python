from turtle import Turtle

class Snake:

    CUBE_WIDTH = 20
    INITIAL_NUMBER_OF_CUBES = 3
    # turtle's module directions in degrees
    directions = { "east": 0, "north": 90, "west": 180, "south": 270 }

    def __init__(self, color: str="white"):
        self.snake: list[Turtle] = []

        # create initial snake
        for i in range(self.INITIAL_NUMBER_OF_CUBES):
            cube = Turtle("square")
            cube.color(color)
            cube.penup()
            #puts the cubes horizontally next to each other
            cube.backward(self.CUBE_WIDTH * i)
            self.snake.append(cube)

        self.head = self.snake[len(self.snake) - 1]

    def move(self):
        """first moves tail to the next cube's position and then moves the head"""

        tail_length = len(self.snake) - 1
        # move tail
        for index in range(tail_length):
            # move Nth cube to Nth+1 cube position
            next_xcor = self.snake[index + 1].xcor()
            next_ycor = self.snake[index + 1].ycor()
            self.snake[index].goto(next_xcor, next_ycor)

        # move head
        self.head.forward(self.CUBE_WIDTH)

    def move_up(self):
        heading = self.head.heading()
        if heading == self.directions["east"] or heading == self.directions["west"]:
            self.turn("north")

    def move_down(self):
        heading = self.head.heading()
        if heading == self.directions["east"] or heading == self.directions["west"]:
            self.turn("south")

    def move_left(self):
        heading = self.head.heading()
        if heading == self.directions["north"] or heading == self.directions["south"]:
            self.turn("west")

    def move_right(self):
        heading = self.head.heading()
        if heading == self.directions["north"] or heading == self.directions["south"]:
            self.turn("east")

    def turn(self, direction: str):
        self.head.setheading(self.directions[direction])