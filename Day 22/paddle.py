from turtle import Turtle

class Paddle:

    def __init__(self, pad_length: int=3, square_length: int=20):
        self.body: list[Turtle] = []
        self.square_length = square_length

        for i in range(pad_length):
            segment = Turtle(shape="square")
            segment.penup()
            segment.color("white")
            segment.setheading(90) # point up
            segment.backward(square_length * i)
            self.body.append(segment)

    def move_up(self):
        for segment in self.body:
            segment.forward(self.square_length)

    def move_down(self):
        for segment in self.body:
            segment.backward(self.square_length)

    def move_xcoor(self, x):
        for segment in self.body: segment.setx(x)

    def touches(self, object: Turtle) -> bool:
        for segment in self.body:
            if segment.distance(object) < 5:
                return True
        return False
