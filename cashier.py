"""
cashier.py
Contains everything about purchasing.
"""


class Cashier:
    def process_coins(self):
        """
        Returns the total calculated from coins inserted.
        Accepts large dollar ($1), half dollar ($0.5), quarter ($0.25),
        and nickel ($0.05) coins.
        """
        print("Please insert coins.")
        large_dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))

        total = (large_dollars * 1) + (half_dollars * 0.5) + (quarters * 0.25) + (nickels * 0.05)
        return total

    def transaction_result(self, coins, cost):
        """
        Returns True when the payment is accepted (and prints change owed),
        or False if money is insufficient (and the machine refunds).
        """
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False