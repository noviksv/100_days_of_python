from tkinter import * 
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None

def play_sound():
    import winsound
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    tick_marks.config(text="")
    canvas.itemconfig(timer_countdown_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 != 0:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(timer_countdown_text, text=f"{count_min}:{count_sec:02}")
    if count > 0:
        global timer
        timer = window.after(100, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✔"
            tick_marks.config(text=marks)
        play_sound()



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

#add a canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# split the canvas on a grid 3x4
timer_label = Label(window, text="Timer", font=(FONT_NAME, 35, "bold"),bg=YELLOW, fg=GREEN)
timer_label.grid(row = 0, column = 1) 

tick_marks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
tick_marks.grid(row=3, column=1)

# add a green label with text Timer


tomato_img = PhotoImage(file="tomato.png")
img = canvas.create_image(100, 112, image=tomato_img)
canvas.create_image(100, 112, image=tomato_img)
timer_countdown_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)


start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Finish", command=reset_timer)
reset_button.grid(row=2, column=3)




window.mainloop()