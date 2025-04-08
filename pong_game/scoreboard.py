from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, ):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.upgrade()

    def upgrade(self):
        self.clear()
        self.goto(-100,180)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))        
        self.goto(100,180)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_add(self):
        self.l_score+=1
        self.upgrade()
    def r_add(self):
        self.r_score+=1
        self.upgrade()



