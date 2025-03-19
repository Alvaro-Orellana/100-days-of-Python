import  art
import game_data
import random

game_is_over = False
score = 0
a = random.choice(game_data.data)

while not game_is_over:
    b = random.choice(game_data.data)

    print("\n"*30)
    print(art.logo)
    if score != 0:
        print(f"You're right! Current score: {score}.")

    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
    print(art.vs)
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.")

    answer = input("Who has more followers? Type 'A' or 'B':").lower()

    a_count, b_count = a["follower_count"], b["follower_count"]
    if (answer == 'a' and a_count > b_count) or (answer == 'b' and b_count > a_count):
        score += 1
        a = b
    else:
        game_is_over = True
        print("\n"*30)
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}.")