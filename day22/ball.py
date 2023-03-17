from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("white")
        self.penup()
        self.y_move = 10
        self.x_move = 10

    def move(self):
        self.setx(self.xcor() + self.x_move)
        self.sety(self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move = -self.y_move

    def bounce_x(self):
        self.x_move = -self.x_move
        self.y_move *= 1.1 #每次接到球都让球速度加快，更刺激！
        self.x_move *= 1.1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x() #把球发给另一个人
        self.y_move = 10
        self.x_move = 10




