from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
words = pandas.read_csv("data/french_words.csv").to_dict(orient="records")
current_words = random.choice(words)

def get_next_word():
    global image; image = PhotoImage(file="images/card_back.png")
    global current_words; current_words = random.choice(words)

    canvas.itemconfig(language_label, text='French', fill='black')
    canvas.itemconfig(word_label, text=current_words["french_word"], fill='black')

def flip_card():
    global image

    image = PhotoImage(file="images/card_back.png")
    canvas.itemconfig(language_label, text='English', fill='white')
    canvas.itemconfig(word_label, text=current_words["english_translation"], fill='white')


window = Tk()
window.title("Flash Card 2")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 268, image=image)

language_label = canvas.create_text(400, 150, text="", fill="black", font=("ariel", 40, "italic"))
word_label = canvas.create_text(400, 263, text="", fill="black", font=("ariel", 60, "bold"))
#language_label = Label(text="", font=("ariel", 40, "italic"))
#word_label = Label(text="", font=("ariel", 60, "bold"))

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_image, highlightthickness=0, command=get_next_word)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=lambda: window.after(1000, flip_card))

#language_label.place(x=320, y=150)
#word_label.place(x=320, y=263)
canvas.grid(row=0, column=0, columnspan=2)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)



get_next_word()
window.mainloop()