from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your bet", prompt="Which turtle? Enter a color:")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
tims = []
y_base = -100
for i in range(len(colors)):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=-230, y=y_base+i*50)
    tims.append(tim)

if user_bet:
    is_race_on = True
while is_race_on:
    for tim in tims:
        rand_distance = random.randint(0, 10)
        tim.forward(rand_distance)
        if tim.xcor() > 230:
            is_race_on = False
            if tim.pencolor() == user_bet:
                print(f"You've won! The {tim.pencolor()} is the winner")
            else:
                print(f"You've lost! The {tim.pencolor()} is the winner")




screen.exitonclick()
