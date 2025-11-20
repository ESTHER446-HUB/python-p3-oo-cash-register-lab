#!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []

    def add_item(self, title, price):
        self.total += price
        self.items.append({"title": title, "price": price})

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            return f"After the discount, the total comes to {self.total:.0f}."
        else:
            return "There is no discount to apply."
