from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from rule import Rule

import time

screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("#FFDD7B")
screen.title("Ping Pong Game")
screen.tracer(0)

r_paddle = Paddle((250, 0))
l_paddle = Paddle((-250, 0))

ball = Ball()
scoreboard = Scoreboard()
all_rules = Rule()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True

while game_on:
    time.sleep(0.02)
    screen.update()
    ball.move()

    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.bounce_y()

    if ball.xcor() > 230 and ball.distance(r_paddle) < 50 or ball.xcor() < -230 and ball.distance(l_paddle) < 50 :
        ball.bounce_x()

    if ball.xcor() > 280:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -280:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
