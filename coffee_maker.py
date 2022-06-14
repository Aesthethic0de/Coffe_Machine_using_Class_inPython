class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water" : 300,
            "milk" : 200,
            "coffee" : 100
        }

    def report(self):

        print(f"water is {self.resources['water']}")
        print(f"milk is {self.resources['milk']}")
        print(f"coffee is {self.resources['coffee']}")


    def is_resource_sufficient(self,drink):

        can_make = True

        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"sorry not enough {item} to make")
                can_make = False

            return can_make


    def make_coffee(self,order):

        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]

        print(f" here is your {order.name}")
