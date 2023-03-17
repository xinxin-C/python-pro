from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("PONG")
screen.listen()
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

ball = Ball()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:  #撞到上下墙
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320: #右边接到球
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320: #左边接到球
        ball.bounce_x()
    if ball.xcor() < -380: #左边漏球
        ball.reset_position()
        scoreboard.r_point()
    if ball.xcor() > 380: #右边漏球
        ball.reset_position()
        scoreboard.l_point()



screen.exitonclick()