from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)


    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.backward(MOVE_DISTANCE)

    def start_new(self):
        self.goto(STARTING_POSITION)

    def finished_line(self):
        if self.ycor()>280:
            return True
        else:
            return False
    
