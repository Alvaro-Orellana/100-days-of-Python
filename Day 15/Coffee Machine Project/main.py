MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resources_are_sufficient(coffee_type: str) -> (bool,str):
    ingredients = MENU[coffee_type]["ingredients"]
    if ingredients.get("water", 0) > resources["water"]:
        return (False, "Sorry there is not enough water.")

    if ingredients.get("milk", 0) > resources["milk"]:
        return (False, "Sorry there is not enough milk.")

    if ingredients.get("coffee", 0) > resources["coffee"]:
        return (False, "Sorry there is not enough coffee.")

    return (True, "")

def convert_user_payment_to_dollars(quarters: int, dimes: int, nickles: int, pennies: int, coffee_type: str) -> float:
    # convert coins to dollars
    quarters_in_dollars = quarters / 4
    dimes_in_dollars = dimes / 10
    nickles_in_dollars = nickles / 20
    pennies_in_dollars = pennies / 100

    client_payment_amount = quarters_in_dollars + dimes_in_dollars + nickles_in_dollars + pennies_in_dollars
    return  client_payment_amount

def make_coffee(coffee_type: str):
    ingredients = MENU[coffee_type]["ingredients"]
    resources["water"] -= ingredients.get("water", 0)
    resources["milk"] -= ingredients.get("milk", 0)
    resources["coffee"] -= ingredients.get("coffee", 0)


types_of_coffees = "/".join(MENU.keys())
user_coffee_choice = input(f"What would you like? ({types_of_coffees}): ").lower()

while user_coffee_choice in MENU.keys():

    (enough_resources, message) = resources_are_sufficient(user_coffee_choice)
    if not enough_resources:
        print(message)
        continue

    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    client_payment = convert_user_payment_to_dollars(quarters, dimes, nickles, pennies, user_coffee_choice)
    coffe_cost = MENU[user_coffee_choice]["cost"]

    if client_payment < coffe_cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        make_coffee(user_coffee_choice)
        print(f"Here is ${client_payment - coffe_cost} in change. \nHere is your {user_coffee_choice}☕. Enjoy!")

    user_coffee_choice = input(f"What would you like? ({types_of_coffees}): ").lower()
