from turtle import Turtle,Screen

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
up = 90
down = 270
right = 0
left = 180

screen=Screen()


class Snake:
    def __init__(self):
        self.segments = []
        self.build_snake()
        self.head = self.segments[0]
        self.head_tail_touch = False

    def build_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def clear(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.build_snake()
        self.head = self.segments[0]
        self.head_tail_touch = False

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_x = self.segments[-1].xcor()
        new_y = self.segments[-1].ycor()
        new_segment.setposition(new_x,new_y)
        self.segments.append(new_segment)

    def up(self):
        if self.head.heading() == down:
            self.head.setheading(down)
        else:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() == up:
            self.head.setheading(up)
        else:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() == right:
            self.head.setheading(right)
        else:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() == left:
            self.head.setheading(left)
        else:
            self.head.setheading(right)

    def check_head_tail_touch(self):
        for sg in self.segments[1:]:
            if self.head.distance(sg) < 10:
                self.head_tail_touch = True



