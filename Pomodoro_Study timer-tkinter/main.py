from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#06FF00"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARK = '✔'
WORK_SECS = 25 * 60
SHORT_BREAK_SECS = 5 * 60
LONG_BREAK_SECS = 20 * 60
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global REPS
    windows.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer', font=(FONT_NAME, 50, 'bold'), fg='green')
    checkmark_label.config(text='')
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_countdown():
    global REPS
    REPS += 1

    if REPS % 8 == 0:
        timer_label.config(text='LONG BREAK TIME 🍜', fg=RED)
        countdown(LONG_BREAK_SECS)
    elif REPS % 2 == 0:
        timer_label.config(text='SHORT BREAK TIME ☕', fg=PINK)
        countdown(SHORT_BREAK_SECS)
    else:
        timer_label.config(text='WORK TIME 🦾🦾', font=(FONT_NAME, 25, 'bold'), fg='green')
        countdown(WORK_SECS)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    checkmark_label.config(text=CHECKMARK * (REPS // 2))

    timer_count = divmod(count, 60)  # gives a tuple of Quotient and remainder
    timer_minutes = timer_count[0]
    timer_seconds = timer_count[1]

    if timer_minutes <= 9:
        timer_minutes = '0'+str(timer_minutes)
    if timer_seconds <= 9:
        timer_seconds = '0'+str(timer_seconds)

    canvas.itemconfig(timer_text, text=f'{timer_minutes}:{timer_seconds}')

    if count > -1:  # actually 0 but 00:00 is not written so -1 is used.
        global timer
        timer = windows.after(1000, countdown, count - 1)
    else:
        start_countdown()


# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title('Pomodoro Timer')
windows.minsize(width=500, height=400)
windows.config(bg=YELLOW, padx=100, pady=90)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 132, text='00:00', font=(FONT_NAME, 35, 'bold'), fill='white')
canvas.grid(row=1, column=1)

timer_label = Label(text='Timer', font=(FONT_NAME, 50, 'bold'), bg=YELLOW, fg='green')
timer_label.grid(row=0, column=1)

checkmark_label = Label(text='', font=(FONT_NAME, 20, 'bold'), bg=YELLOW, fg=GREEN)
checkmark_label.grid(row=3, column=1)

start_button = Button(text='START', command=start_countdown)
start_button.grid(row=2, column=0)

reset_button = Button(text="RESET", command=reset)
reset_button.grid(row=2, column=2)


windows.mainloop()
