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

money = 0
COFFEE_MACHINE_COMMANDS = ["off", "report"]
allowed_inputs = list(MENU.keys()) + COFFEE_MACHINE_COMMANDS
client_input = ""


def ask_client_for_coffee() -> str:
    types_of_coffees = "/".join(MENU.keys())
    global client_input
    client_input = input(f"What would you like? ({types_of_coffees}): ").lower().strip()
    return client_input

def are_resources_sufficient(coffee_type: str) -> (bool, str):
    ingredients_required = MENU[coffee_type]["ingredients"]
    if  resources["water"] < ingredients_required.get("water", 0):
        return (False, "Sorry there is not enough water.")

    if resources["milk"] < ingredients_required.get("milk", 0) :
        return (False, "Sorry there is not enough milk.")

    if resources["coffee"] < ingredients_required.get("coffee", 0):
        return (False, "Sorry there is not enough coffee.")

    return (True, "")

def convert_user_payment_to_dollars(quarters: int, dimes: int, nickles: int, pennies: int, coffee_type: str) -> float:
    quarters_in_dollars = quarters * 0.25
    dimes_in_dollars = dimes * 0.1
    nickles_in_dollars = nickles * 0.05
    pennies_in_dollars = pennies * 0.01

    client_payment_amount = quarters_in_dollars + dimes_in_dollars + nickles_in_dollars + pennies_in_dollars
    return  round(client_payment_amount, 2)

def update_resources(coffee_type: str):
    ingredients = MENU[coffee_type]["ingredients"]
    resources["water"] -= ingredients.get("water", 0)
    resources["milk"] -= ingredients.get("milk", 0)
    resources["coffee"] -= ingredients.get("coffee", 0)

    coffe_cost_cost = MENU[coffee_type]["cost"]
    global  money
    money += coffe_cost_cost

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

while ask_client_for_coffee() in allowed_inputs:

    if client_input in COFFEE_MACHINE_COMMANDS:
        if client_input == "off":
            break
        if client_input == "report":
            print_report()
            continue

    (enough_resources, message) = are_resources_sufficient(client_input)
    if not enough_resources:
        print(message)
        continue

    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    client_payment = convert_user_payment_to_dollars(quarters, dimes, nickles, pennies, client_input)
    coffe_cost = MENU[client_input]["cost"]

    if client_payment < coffe_cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        update_resources(client_input)
        change = round(client_payment - coffe_cost, 2)
        print(f"Here is ${change} in change. \nHere is your {client_input} ☕ . Enjoy!")
