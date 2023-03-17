from turtle import Turtle, Screen
import random
tim = Turtle()

tim.shape('turtle')

tim.color('red')
tim.speed('fastest')


def draw(size_of_gap):
    for _ in range(360//size_of_gap):
        tim.pencolor(random.random(), random.random(), random.random())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw(5)

screen = Screen()
screen.exitonclick()