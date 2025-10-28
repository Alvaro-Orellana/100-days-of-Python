from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
WORDS_TO_LEARN_FILE_PATH = "data/words_to_learn.csv"
FRENCH_WORDS_FILE_PATH = "data/french_words.csv"

words = []
current_card = {}
flip_timer = None

def load_words() -> list[dict[str, str]]:
    try:
        words_to_learn = pandas.read_csv(WORDS_TO_LEARN_FILE_PATH).to_dict(orient="records")
        return words_to_learn
    except FileNotFoundError:
        default_french_words = pandas.read_csv(FRENCH_WORDS_FILE_PATH).to_dict(orient="records")[1:]
        return default_french_words

def next_card(card_is_known=None):
    global flip_timer, current_card

    if not words:
        canvas.itemconfig(language_label, text='No hay mas cartas', fill='black')
        canvas.itemconfig(word_label, text="Las memorizaste todas", fill='black')
        return

    if flip_timer:  # reset timer
        window.after_cancel(flip_timer)
        flip_timer = window.after(3000, flip_card)

    if card_is_known:
        words.remove(current_card)
        pandas.DataFrame(words).to_csv(WORDS_TO_LEARN_FILE_PATH, index=False)

    current_card = random.choice(words)
    update_UI(current_card)

def update_UI(card):
    canvas.itemconfig(language_label, text='French', fill='black')
    canvas.itemconfig(word_label, text=card["french_word"], fill='black')
    canvas.itemconfig(card_background, image=front_image)

def flip_card():
    canvas.itemconfig(card_background, image=back_image)
    canvas.itemconfig(language_label, text='English', fill='white')
    canvas.itemconfig(word_label, text=current_card["english_translation"], fill='white')

window = Tk()
window.title("Flash Card 2")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 268, image=front_image)

language_label = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
word_label = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_image, highlightthickness=0, command=lambda : next_card(card_is_known=True))
wrong_button = Button(image=wrong_image, highlightthickness=0, command=lambda : next_card(card_is_known=False))

canvas.grid(row=0, column=0, columnspan=2)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)



words = load_words()
current_card = random.choice(words)
update_UI(current_card)
flip_timer = window.after(3000, flip_card)
window.mainloop()