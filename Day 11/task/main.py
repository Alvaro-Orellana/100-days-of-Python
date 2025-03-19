import art
import random

def print_players_cards(user_cards: list[int], computer_cards: list[int]):
    print(f"    Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"    Computer's first card: {computer_cards[0]}")

def print_final_score(user_cards: list[int], computer_cards: list[int]):
    user_count = sum(user_cards)
    computer_count = sum(computer_cards)
    print(f"    Your final hand: {user_cards}, final score: {user_count}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_count}")
    if user_count > 21:
        print("You went over. You lose 😭")
    elif computer_count > 21:
        print("Opponent went over. You win 😁")
    elif user_count > computer_count:
        print("You win 😃")
    elif computer_count > user_count:
        print("You lose 😤")
    else:
        print("Draw")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == "y":

    user_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards)]

    print("\n" * 60, art.logo)
    print_players_cards(user_cards, computer_cards)

    # user's turn
    while sum(user_cards) <= 21 and input("Type 'y' to get another card, type 'n' to pass:") == "y":
        user_cards.append(random.choice(cards))

        if sum(user_cards) > 21 and 11 in user_cards:
            index = user_cards.index(11)
            user_cards[index] = 1

        print_players_cards(user_cards, computer_cards)

    if sum(user_cards) <= 21:
        # computer's turn. Draw until score is 17 or more
        while sum(computer_cards) < 17:
            computer_cards.append(random.choice(cards))

    print_final_score(user_cards, computer_cards)



