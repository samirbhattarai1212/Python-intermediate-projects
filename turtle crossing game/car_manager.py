from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 8


class CarManager():

    def __init__(self):
        self.all_cars=[]
        self.car_speed= STARTING_MOVE_DISTANCE

    def make_cars(self):
        if random.randint(1,6)==1:
        
            self.new_car= Turtle("square")
            self.new_car.shapesize(stretch_wid=1,stretch_len=2)
            self.new_car.penup()
            self.new_car.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            self.new_car.goto(x=300,y=random_y)
            self.all_cars.append(self.new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed+= MOVE_INCREMENT



        
    

    
