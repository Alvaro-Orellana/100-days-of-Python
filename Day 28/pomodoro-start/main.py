import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MINUTES = 25
SHORT_BREAK_MINUTES = 5
LONG_BREAK_MINUTES = 20

# ---------------------------- TIMER RESET ------------------------------- #
def start_pressed():
    pass

def reset_pressed():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer():
    count_down(seconds=WORK_MINUTES * 60)
    count_down(seconds=SHORT_BREAK_MINUTES * 60)
    #window.after(WORK_MINUTES*60, count_down, SHORT_BREAK_MINUTES * 60)

    # update checks
    check_label_text = check_label.cget("text")
    check_label_text += "✓\n"
    check_label.config(text=check_label_text)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds):
    if seconds >= 0:
        canvas.itemconfigure(timer_text, text=format_seconds(seconds)) # update label text
        window.after(1000, count_down, seconds - 1)


def format_seconds(seconds: int) -> str:
    minutes_remaining, seconds_remaining = divmod(seconds, 60)

    minutes_remaining = str(minutes_remaining) if minutes_remaining > 9 else "0" + str(minutes_remaining)
    seconds_remaining = str(seconds_remaining) if seconds_remaining > 9 else "0" + str(seconds_remaining)

    return minutes_remaining + ":" + seconds_remaining
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")

timer_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
start_button = tk.Button(text="Start", command=start_pressed, highlightthickness=0)
reset_button = tk.Button(text="Reset", command=reset_pressed, highlightthickness=0)
check_label = tk.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))

canvas.grid(row=1, column=1)
timer_label.grid(row=0, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
check_label.grid(row=3, column=1)

timer()
window.mainloop()