from turtle import Turtle
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
            super().__init__(shape, undobuffersize, visible)
            self.hideturtle()
            self.penup()
            self.goto(-250,260)
            self.level=0
            self.color("black")
            self.write(f"Level: {self.level}",align="left",font= FONT)

    def increase_score(self):
          self.clear()
          self.level+=1
          self.write(f"Level {self.level}",align="left",font= FONT)
    
    def gameover(self):
          self.goto(0,0)
          self.write("Game over!",align="left",font= FONT)
          


