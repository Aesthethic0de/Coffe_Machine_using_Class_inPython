class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters" : 0.25,
        "dimes" : 0.05,
        "nickles" : 0.05,
        "pennies" : 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"money : {self.CURRENCY}{self.profit}")

    def process_coin(self):
        print("please insert coin")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        self.process_coin()
        if self.money_received >= cost:
            change = round(self.money_received - cost,2)
            print(f"your change is {change}")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("sorry thats not enough money")
            self.money_received = 0
            return False