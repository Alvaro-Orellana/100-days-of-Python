import  art
import random

LOWER_BOUND = 1
UPPER_BOUND = 100
number_of_attempts = -1
random_number = random.randint(LOWER_BOUND, UPPER_BOUND)

print(art.logo)
print(f"Welcome to the Number Guessing Game! I'm thinking of a number between {LOWER_BOUND} and {UPPER_BOUND}.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    number_of_attempts = 10
else:
    number_of_attempts = 5

while number_of_attempts > 0 :
    print(f"You have {number_of_attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess "))

    if guess > random_number:
        print("Too high.", "Guess again.")
    elif guess < random_number:
        print("Too low.", "Guess again.")
    else:
        print(f"You got it! The answer was {random_number}")
        break
    number_of_attempts -= 1

if number_of_attempts == 0:
    print("You've run out of guesses. Refresh the page to run again.")