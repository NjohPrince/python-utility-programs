import math
from tkinter import *

# --------------------------- CONSTANTS ---------------------------#

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# --------------------------- TIMER RESET ---------------------------#
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")


# --------------------------- TIMER MECHANISM ---------------------------#
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# --------------------------- COUNTDOWN MECHANISM ---------------------------#
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)


# --------------------------- CONSTANTS ---------------------------#

# --------------------------- UI SETUP ---------------------------#
window = Tk()
window.title("Pomodoro")
window.config(bg=YELLOW, padx=100, pady=50)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=183, height=209, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(91.5, 104.5, image=tomato_image)
timer_text = canvas.create_text(91.5, 104.5, text="00:00", fill="White", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", bg="White", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg="White", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(text="", bg=YELLOW, fg=GREEN)
check_marks.grid(row=3, column=1)

window.mainloop()
