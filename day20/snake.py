from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.creat_snake()
        self.head = self.segments[0]

    def creat_snake(self):
        for i in range(3):
            self.add_segment((-i * 20, 0))

    def add_segment(self, position):
        cube = Turtle(shape='square')
        cube.penup()
        cube.goto(position)
        cube.color("white")
        self.segments.append(cube)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for cut_num in range(len(self.segments) - 1, 0, -1):
            self.segments[cut_num].goto(self.segments[cut_num - 1].pos())

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

