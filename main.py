class Item:
    def __init__(self, name: str, quantity):
        # assertion example
        assert quantity >= 0, f"Price {quantity} is not greater than or equal to zero!"
        self.z = 3


        # self assignments

        print(f"I am created like that - {name}")
        self.name = name

    def calculate_total_price(self, x, y):
        self.z = 3
        return x * y


item1 = Item("laptop", -1)

print(item1.name)

'''Learning about __init__ method in python.'''
