from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



screen= Screen()
screen.tracer(0)
paddle= Turtle()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")

l_paddle= Paddle((-350,0))
r_paddle=Paddle((350,0))
ball= Ball()

scoreboard= Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
       ball.bounch_y()

    if ball.distance(l_paddle)<50 and ball.xcor()<-325 or ball.distance(r_paddle) <50 and ball.xcor()>325:
        ball.bounch_x()
    
    if ball.xcor()> 380:
        ball.reset_position()
        scoreboard.l_add()
        
    if ball.xcor()< -380:
        ball.reset_position()
        scoreboard.r_add()
        
        
    

    

screen.exitonclick()