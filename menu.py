class MenuItem:

    def __init__(self,name,water,milk,coffe,cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk" : milk,
            "coffee": coffe
        }

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffe=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffe=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffe=24, cost=3)

        ]

    def get_items(self):

        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        for item in self.menu:
            if order_name == item.name:
                print(item.name)
                return item
        print("sorry that item is not available")


