from turtle import Turtle, Screen
from net import Net
from player_board import PlayerBoard
import time
from cpu_board import CpuBoard
"""Screen settings"""
screen = Screen()
screen.listen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
"""Objects"""
my_board = PlayerBoard()
my_board.creating_segments()
cpu_board = CpuBoard()
net = Net()
"""Objects without a classes v"""
ball = Turtle("circle")
ball.color("white")
"""Stering"""
screen.onkey(my_board.move_up,"w")
screen.onkey(my_board.move_down,"s")
"""Logic"""



is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.08)
    cpu_board.up_and_down()
    if cpu_board.segments[0].ycor() > 280:
        cpu_board.segments[0].setheading(270)
    elif cpu_board.segments[0].ycor() < -280:
        cpu_board.segments[0].setheading(90)



















screen.exitonclick()