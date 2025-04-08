from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer_=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_():
    canvas.after_cancel(timer_)
    canvas.itemconfig(timer_text, text="00:00")
    check_sign.config(text="")
    timer.config(text="Timer")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1

    if reps%8==0:
        count_down(LONG_BREAK_MIN*60)
        timer.config(text="Long Break",fg=RED)
    elif reps%2==0:
        count_down(SHORT_BREAK_MIN*60)
        timer.config(text="Short Break", fg=PINK)
    else:
        count_down(WORK_MIN*60)
        timer.config(text="Work", fg=GREEN)


    

def count_down(count):

    count_min= math.floor(count/60)
    count_sec= count%60
    if count_sec<10:
        count_sec= f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
       global timer_
       timer_=window.after(1000, count_down, count-1 )

    else:
        start_timer()
        marks=""
        for _ in range(math.floor(reps/2)):
            marks+= "✔️"
        check_sign.config(text=marks)
        
# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.title("Timewatch")
window.config(padx=100, pady=50, bg=YELLOW)


timer= Label(text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME,40, "bold"))
timer.grid(column= 1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_image= PhotoImage(file="tomato.png")
canvas.create_image( 100,112,image=tomato_image)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)



start=Button(text="Start",bg=YELLOW, highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset= Button(text="Reset",bg=YELLOW, highlightthickness=0, command= reset_)
reset.grid(column=2, row=2)

check_sign = Label(font=(FONT_NAME,10,"bold"), fg=GREEN, bg=YELLOW)
check_sign.grid(column=1,row=3)



window.mainloop()


