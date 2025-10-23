import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"

def check():
    print("Checking")


window = tk.Tk()
window.title("Flash Card 2")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = tk.PhotoImage(file="images/card_front.png")
canvas.create_image(400, 268, image=image)

language_label = tk.Label(text="French", font=("ariel", 40, "italic"))
word_label = tk.Label(text="trouve", font=("ariel", 60, "bold"))

right_image = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, command=check)
wrong_image = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, command=check)

canvas.grid(row=0, column=0, columnspan=2)
language_label.place(x=320,y=150)
word_label.place(x=320,y=263)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)




window.mainloop()