# class Item:
#     def __init__(self, name: str, quantity):
#         # assertion example
#         assert quantity >= 0, f"Price {quantity} is not greater than or equal to zero!"
#         self.z = 3
#
#
#         # self assignments
#
#         print(f"I am created like that - {name}")
#         self.name = name
#
#     def calculate_total_price(self, x, y):
#         self.z = 3
#         return x * y
#
#
# item1 = Item("laptop", -1)
#
# print(item1.name)

'''Learning about __init__ method in python.'''
import csv

''' Learning about class attributes - attributes that belong to a class and can be accessed by all instances.'''


class Item:
    quantity = 0
    discount = 15
    all = []

    def __init__(self, name):
        self.price = 90
        self.name = name
        Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name= item.get('name')
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True

    def __repr__(self):
        return f"{self.name}"

    def apply_discount(self):
        self.price = self.price / Item.discount
        return self.price


print(Item.is_integer(7.0))
