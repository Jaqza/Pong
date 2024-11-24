import turtle as t
import time
from random import randint
screen = t.Screen()

screen.setup(800,600)
screen.listen()
screen.bgcolor("black")


rand_angle = randint(0, 360)
ball = t.Turtle("circle")
ball.color("white")
ball.setheading(rand_angle)
print(ball.heading())
is_game_on = True
while is_game_on:
    ball.forward(20)
    time.sleep(0.16)
    if ball.ycor() == 380 or ball.ycor() == -380:
        ball.setheading(360 - 2 * ball.heading())












screen.exitonclick()