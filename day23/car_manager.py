from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.cars = []
        self.step = STARTING_MOVE_DISTANCE

    def new_car(self):
        car = Turtle()
        car.shape('square')
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.color(random.choice(COLORS))
        car.penup()
        car.goto(300, random.randint(-250, 250))
        self.cars.append(car)

    def speed_up(self):
        self.clear()
        self.step += MOVE_INCREMENT

    def move_car(self):
        for car in self.cars:
            car.goto(car.xcor() - self.step, car.ycor())
            if car.xcor() < -300:
                pass




