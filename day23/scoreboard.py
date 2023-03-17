from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-250, 250)
        self.show_score()

    def add_score(self):
        self.level += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f'Level: {self.level}', align='center', font=FONT)

