#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []  # Track all item names
        self.last_transaction_amount = 0
        self.last_transaction_items = []  # Track items in last transaction

    def add_item(self, title, price, quantity=1):
        transaction_total = price * quantity
        self.total += transaction_total

        # Track items individually for quantity
        transaction_items = [title] * quantity
        self.items.extend(transaction_items)

        # Store last transaction for voiding
        self.last_transaction_amount = transaction_total
        self.last_transaction_items = transaction_items

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
            return int(self.total)
        else:
            print("There is no discount to apply.")
            return None

    def void_last_transaction(self):
        # Remove last transaction from total
        self.total -= self.last_transaction_amount
        # Remove last transaction items from the items list
        for item in self.last_transaction_items:
            self.items.pop()  # remove last occurrences
        # Reset last transaction tracking
        self.last_transaction_amount = 0
        self.last_transaction_items = []


