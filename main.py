from menu import MenuItem, Menu
from coffee_maker import CoffeeMaker
from Money_Machine import MoneyMachine


money_machine = MoneyMachine()
coffemaker = CoffeeMaker()
menu = Menu()


is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"what would you like to have {options}  ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffemaker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffemaker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffemaker.make_coffee(drink)







