"""
main.py
Acts as the starting point of execution for the program.
"""

import data
import sandwich_maker
import cashier

# Create data variables from the dictionaries in data.py
resources = data.resources
recipes = data.recipes

# Create instances of our classes
machine = sandwich_maker.SandwichMaker(resources)
register = cashier.Cashier()

is_on = True

while is_on:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ")

    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f"Bread: {resources['bread']} slice(s)")
        print(f"Ham: {resources['ham']} slice(s)")
        print(f"Cheese: {resources['cheese']} pound(s)")

    elif choice in recipes:
        order = recipes[choice]
        ingredients = order["ingredients"]

        if machine.check_resources(ingredients):
            coins = register.process_coins()
            if register.transaction_result(coins, order["cost"]):
                machine.make_sandwich(choice, ingredients)

    else:
        print("Sorry, I didn't understand that choice.")