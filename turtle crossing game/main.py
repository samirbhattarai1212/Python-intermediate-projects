import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()

screen.listen()
screen.onkey(player.go_up,"Up")
screen.onkey(player.go_down,"Down")

car_manager=CarManager()
scoreboard=Scoreboard()

game_is_on = True
while game_is_on:
    
    time.sleep(0.1)
    screen.update()

    car_manager.make_cars()
    car_manager.move_car()

    #detect collision with cars
    for cars in car_manager.all_cars:
        if cars.distance(player)<20:
            game_is_on=False
            scoreboard.gameover()
    #detect if player crossed finishing line    
    if player.finished_line():
        player.start_new()
        car_manager.level_up()
        scoreboard.increase_score()
        

        

    

screen.exitonclick()