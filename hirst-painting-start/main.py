###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append((color.rgb[0], color.rgb[1], color.rgb[2]))
#
# print(rgb_colors)
from turtle import Turtle, Screen
import random

tony = Turtle()
tony.speed('fastest')
screen = Screen()
screen.setworldcoordinates(-90, -90, 900, 900)
screen.colormode(255)
color_list = [(240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
radii = 20
distance = 50
walk = radii * 2 + distance
for i in range(10):
    for j in range(10):
        color = random.choice(color_list)
        tony.dot(20, color)
        tony.penup()
        tony.hideturtle()
        tony.setx(tony.xcor() + walk)
    tony.setx(0)
    tony.sety(tony.ycor() + walk)

screen.exitonclick()

