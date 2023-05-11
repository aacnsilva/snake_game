from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SHAPE = "square"
COLOR = "white"
MOVE_DISTANCE_INCREASE_BY = 1


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.move_distance = MOVE_DISTANCE

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_tail_segment(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        segment = Turtle(shape=SHAPE)
        segment.penup()
        segment.color(COLOR)
        segment.goto(position)
        self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].pos())
        self.head.forward(self.move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def hit_the_wall(self, x_boundary, y_boundary):
        return self.head.xcor() > x_boundary or self.head.xcor() < -x_boundary or self.head.ycor() > y_boundary \
            or self.head.ycor() < -y_boundary

    def hit_itself(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 5:
                return True
        return False

    def increase_move_distance(self):
        self.move_distance += MOVE_DISTANCE_INCREASE_BY
