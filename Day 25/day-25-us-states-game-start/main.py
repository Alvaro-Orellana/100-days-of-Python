import turtle as t
import pandas

# setup screen and pen
screen = t.Screen()
screen.title("US States Guessing Game")
screen.bgpic("blank_states_img.gif")
pen = t.Turtle(visible=False)
pen.penup()

# load states data
states_table = pandas.read_csv("50_states.csv")
remaining_states_names = states_table.state.to_list()

while remaining_states_names:
    correct_guesses = 50 - len(remaining_states_names)
    guess = t.textinput(f"{correct_guesses}/50 States Correct", "What's another state name?").title()

    if guess in remaining_states_names:
        remaining_states_names.remove(guess)
        state_row = states_table[states_table.state == guess]
        pen.goto(state_row.x.item(), state_row.y.item())
        pen.write(guess, align="center")

    if guess == "Exit": break

pandas.DataFrame(remaining_states_names, columns=["States"]).to_csv("states_to_learn.csv")
