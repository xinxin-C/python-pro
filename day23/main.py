import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, FONT

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.go_up, 'Up')

counter =0
game_is_on = True
while game_is_on:
    counter += 1
    if counter == 6:
        car_manager.new_car()
        counter = 0
    car_manager.move_car()
    time.sleep(0.1)
    screen.update()
    if player.ycor() > 280:
        scoreboard.add_score()
        player.reset_player()
        car_manager.speed_up()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.goto(0, 0)
            scoreboard.write('Game Over!', align='center', font=FONT)


screen.exitonclick()