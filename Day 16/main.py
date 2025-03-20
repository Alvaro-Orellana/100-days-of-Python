from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    choice = input(f"What would you like? {menu.get_items()} ")

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    if choice == "off":
        break

    drink = menu.find_drink(choice)
    if drink is None:
        continue

    enough_resources = coffee_maker.is_resource_sufficient(drink)
    payment_successful = money_machine.make_payment(drink.cost)

    if enough_resources and payment_successful:
        coffee_maker.make_coffee(drink)



