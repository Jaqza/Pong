from turtle import Turtle


class PlayerBoard:
    def __init__(self):
        self.board = []
        self.segment = Turtle
        self.position = [(-380, 0), (-380, 20), (-380, -20)]
    def creating_segments(self):
        """creating a board from a list of positions , for cpu board too"""
        for place in self.position:
            self.segment = Turtle("square")
            self.segment.speed("normal")
            self.segment.penup()
            self.segment.color("blue")
            self.segment.goto(place)
            self.board.append(self.segment)

    def move_up(self):
        for self.segment in self.board:
            self.segment.left(90)
            self.segment.forward(20)
            self.segment.right(90)

    def move_down(self):
        for self.segment in self.board:
            self.segment.right(90)
            self.segment.forward(20)
            self.segment.left(90)



