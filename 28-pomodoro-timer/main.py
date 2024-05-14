from tkinter import * 
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    count_down(5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    canvas.itemconfig(timer_countdown_text, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

#add a canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# split the canvas on a grid 3x4
timer_label = Label(window, text="Timer", font=(FONT_NAME, 35, "bold"),bg=YELLOW, fg=GREEN)
timer_label.grid(row = 0, column = 1) 


# add a green label with text Timer


tomato_img = PhotoImage(file="tomato.png")
img = canvas.create_image(100, 112, image=tomato_img)
canvas.create_image(100, 112, image=tomato_img)
timer_countdown_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

count_down(5)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

start_button = Button(text="Finish")
start_button.grid(row=2, column=3)

tick_marks = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
tick_marks.grid(row=3, column=1)



window.mainloop()