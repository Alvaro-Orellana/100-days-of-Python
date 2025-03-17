import art

print(art.logo)

bidders = {}
add_more_bidders = True
highest_bidder = ""
highest_bidding_amount = 0

while add_more_bidders:
    # TODO-1: Ask the user for input
    user_name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    # TODO-2: Save data into dictionary {name: price}
    bidders[user_name] = bid
    # TODO-3: Whether if new bids need to be added
    add_more_bidders = input("Are there any other bidders? Type 'yes or 'no'.") == "yes"
    # TODO-4: Compare bids in dictionary
    if add_more_bidders == "yes":
        print("\n"*60)

for user_name, bid in bidders.items():
    if bid > highest_bidding_amount:
        highest_bidder = user_name
        highest_bidding_amount = bid
print(f"The winner is {highest_bidder} with a bid of ${highest_bidding_amount}")


