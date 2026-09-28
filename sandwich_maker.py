"""
sandwich_maker.py
Contains everything about making sandwiches.
"""


class SandwichMaker:
    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """
        Returns True when the order can be made, False if ingredients are
        insufficient. ingredients comes from the recipe dict for the chosen
        sandwich size, e.g. {"bread": 2, "ham": 4, "cheese": 4}.
        """
        for item, amount in ingredients.items():
            if self.machine_resources.get(item, 0) < amount:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """
        Deducts the required ingredients from the resources.
        Void function, no return.
        """
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")