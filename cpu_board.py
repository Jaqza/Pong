from turtle import Turtle
from random import choice


class CpuBoard:

    def __init__(self):
        self.segment = Turtle
        self.position = [(380, 20), (380, 0), (380, -20)]
        self.segments = []
        self.turtle = Turtle
        self.directions = [90, 270]
        self.rand_direct = choice(self.directions)
        self.create_cpu_board()



    def create_cpu_board(self):
        for num_pos in self.position:
            self.turtle = Turtle("square")
            self.turtle.color("white")
            self.turtle.penup()
            self.segments.append(self.turtle)
            self.turtle.goto(num_pos)
            self.turtle.setheading(self.rand_direct)
    def up_and_down(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_cord = self.segments[seg_num - 1].xcor()
            y_cord = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_cord, y_cord)
        self.segments[0].forward(20)
