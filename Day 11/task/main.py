import art
import random

def print_players_cards():
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {computer_cards}")  # improve, remove parenthesis


answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
if answer == "n":
    exit(1)

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

user_cards.append(random.choice(cards))
user_cards.append(random.choice(cards))
computer_cards.append(random.choice(cards))

print_players_cards()

keep_playing = input("Type 'y' to get another card, type 'n' to pass:")

while keep_playing == "y" and sum(user_cards) <= 21:
    user_cards.append(random.choice(cards))
    print_players_cards()



if sum(user_cards) > 21:
    #Game finished
    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")


