from turtle import Turtle, Screen
import pandas

turtle=Turtle()
screen=Screen()

screen.setup(1050,700)

screen.title("Nepal Districts")


image= "Districts_of_Nepal_2020_(blank).gif"
screen.addshape(image)
turtle.shape(image)

guessed_states=[]
data= pandas.read_csv("nepaldistrict.csv")
cities_list=data.state.to_list()
while len(guessed_states) <78:
    answer= screen.textinput(title=f"{len(guessed_states)}/78 ", prompt="what's another district name? ").title()
    
    if answer== "Exit":
        missing_states=[]
        for states in cities_list:
            if states not in guessed_states:
                missing_states.append(states)
            new_data=pandas.DataFrame(missing_states)
            new_data.to_csv("missing_states")


        break
    if answer in cities_list:
        timmy= Turtle()
        timmy.hideturtle()
        timmy.penup()
        timmy.color("black")
        state_data= data[data.state==answer] #gives row of current state
        timmy.goto(int(state_data.x), int(state_data.y))
        timmy.write(answer)
        guessed_states.append(answer)




screen.mainloop()
