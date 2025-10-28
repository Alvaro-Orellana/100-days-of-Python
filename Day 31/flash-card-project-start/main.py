from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
words = []
current_card = {}

def load_words():
    global words
    try:
        with open("data/words_to_learn.csv", 'r') as file:
            words = pandas.read_csv(file).to_dict(orient="records")

    except FileNotFoundError:
        words = pandas.read_csv("data/french_words.csv").to_dict(orient="records")[1:]

    print(words)

def button_pressed(button: str | None = None):
    global flip_timer, current_card

    # reset timer
    window.after_cancel(flip_timer)
    flip_timer = window.after(3000, flip_card)

    if not words:
        canvas.itemconfig(language_label, text='No hay mas cartas', fill='black')
        canvas.itemconfig(word_label, text="Las memorizaste todas", fill='black')
        return
    current_card = random.choice(words)

    # update ui
    canvas.itemconfig(language_label, text='French', fill='black')
    canvas.itemconfig(word_label, text=current_card["french_word"], fill='black')
    canvas.itemconfig(card_background, image=front_image)

    # save words
    with open("data/words_to_learn.csv", 'w') as file:
        if button == 'right_button':  # save all words except the current word, the user alredy knows its translation
            words.remove(current_card)
            pandas.DataFrame(words).to_csv(file, index=False)
        elif button == 'wrong_button':  # the user doesn't know the current word, so we save that and all the others
            pandas.DataFrame(words).to_csv(file, index=False)
            words.remove(current_card)


def flip_card():
    canvas.itemconfig(card_background, image=back_image)
    canvas.itemconfig(language_label, text='English', fill='white')
    canvas.itemconfig(word_label, text=current_card["english_translation"], fill='white')

window = Tk()
window.title("Flash Card 2")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 268, image=front_image)

language_label = canvas.create_text(400, 150, text="", fill="black", font=("ariel", 40, "italic"))
word_label = canvas.create_text(400, 263, text="", fill="black", font=("ariel", 60, "bold"))

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_image, highlightthickness=0, command=lambda : button_pressed('right_button'))
wrong_button = Button(image=wrong_image, highlightthickness=0, command=lambda : button_pressed('wrong_button'))

canvas.grid(row=0, column=0, columnspan=2)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

load_words()
button_pressed()
window.mainloop()