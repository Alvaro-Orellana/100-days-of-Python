from turtle import Turtle

class Snake:

    DIRECTIONS = {"right": 0, "up": 90, "left": 180, "down": 270} # turtle's module directions in degrees

    def __init__(self, color: str="white", segment_width=20, number_of_segments=3):
        self.color: str = color
        self.segment_width: int = segment_width
        self.number_of_segments: int = number_of_segments
        self.body: list[Turtle] = []
        self.head: Turtle = None
        self.create_initial_body()

    def create_initial_body(self):
        # Create head
        self.head = Turtle("square")
        self.head.color(self.color)
        self.head.penup()
        self.body.append(self.head)

        # Create tail
        for i in range(self.number_of_segments):
            new_segment = self.create_segment()
            self.body.append(new_segment)

    def create_segment(self):
        """Use for growing the tail only, not the head. Because it assumes there exists at least one segment before """
        if self.head is None: return

        last_segment = self.body[-1]
        new_segment = Turtle("square")
        new_segment.color(self.color)
        new_segment.penup()
        new_segment.setheading(last_segment.heading())
        new_segment.goto(last_segment.position())
        new_segment.backward(self.segment_width)
        return new_segment

    def move(self):
        """
        First moves tail, shifting each segment to the next segment's position, then moves the head.
        Head is the first cube, tail is all the rest.
        """
        # Move tail.
        tail_indices = range(1, len(self.body))
        for index in reversed(tail_indices):
            next_segment = self.body[index - 1]
            self.body[index].goto(next_segment.position())

        # Move head
        self.head.forward(self.segment_width)

    def grow_tail(self):
       """Adds only one segment to the end of the snake."""
       new_segment = self.create_segment()
       self.body.append(new_segment)

    def reset(self):
        for segment in self.body:
            segment.goto(10000,10000)
        self.body.clear()
        self.create_initial_body()

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
        square_edge_offset = self.segment_width / 2

        if self.is_going_up(): return self.head.ycor() + square_edge_offset
        elif self.is_going_down(): return self.head.ycor() - square_edge_offset
        elif self.is_going_left(): return self.head.xcor() - square_edge_offset
        elif self.is_going_right(): return self.head.xcor() + square_edge_offset
        else: pass # should never reach here. throw an error?

    def is_going_up(self) -> bool: return self.head.heading() == self.DIRECTIONS["up"]
    def is_going_down(self) -> bool: return self.head.heading() == self.DIRECTIONS["down"]
    def is_going_left(self) -> bool: return self.head.heading() == self.DIRECTIONS["left"]
    def is_going_right(self) -> bool: return self.head.heading() == self.DIRECTIONS["right"]


