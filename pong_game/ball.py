from turtle import Turtle, Screen
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_pos= 10
        self.y_pos=10
        self.ball_speed=0.1

    def move(self):

        new_x= self.xcor()+self.x_pos
        new_y=self.ycor()+self.y_pos
        self.goto(new_x,new_y)
        

    def bounch_y(self):
        self.y_pos*= -1

    def bounch_x(self):
        self.x_pos*= -1
        self.ball_speed*=0.8

    def reset_position(self):
        self.goto(0,0)
        self.ball_speed=0.1
        self.bounch_x()



    
