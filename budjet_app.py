
#import textwrap

class Category:

    def __init__(self, item, ledger = False):
        self.item = item
        self.ledger = list()
        self.balance = 0


    def deposit(self, deposit_amt, deposit_descrpt = False):
        self.deposit_amt = deposit_amt
        self.deposit_descrpt = deposit_descrpt
        self.balance = 0 + deposit_amt
        if self.deposit_descrpt:
            x = "description : {}, amount {}".format(self.deposit_descrpt, self.deposit_amt)
            self.ledger.append(x)
        if not self.deposit_descrpt:
            x = "description : \" \", amount {}".format(self.deposit_amt)
            self.ledger.append(x)

    def get_balance(self):
        return self.balance

    def check_funds(self, amt):
        self.amt = amt
        if self.amt > self.get_balance():
            return False
        return True

    def withdraw(self, withdraw_amt, withdraw_descrpt = False):
        self.withdraw_amt = withdraw_amt
        self.withdraw_descrpt = withdraw_descrpt
        if self.withdraw_descrpt:
            ledger_item = "description : {}, amount {}".format(self.withdraw_descrpt, (-1) * self.withdraw_amt)
        if not self.withdraw_descrpt:
            ledger_item = "description : \" \", amount {}".format((-1) * self.withdraw_amt)
        if self.check_funds(self.withdraw_amt):
            self.balance = self.deposit_amt - self.withdraw_amt
            self.deposit_amt = self.balance
            self.ledger.append(ledger_item)
            return True
        return False

    def __repr__(self):
        return self.item

    def transfer(self, transfer_amt, item2):
        Category.item2 = item2
        self.transfer_amt = transfer_amt
        if transfer_amt < self.deposit_amt:
            self.ledger.append("{} Transfer to {}".format(Category.item2.ledger, (-1) * self.transfer_amt))
            item2.ledger.append("{} Transfer from {}".format(self.item, self.transfer_amt))
            return True
        return False

    def __str__(self):
            stars = "{}  {}  {} \n ".format((int(30 - len(self.item)/2) * "*"), self.item, int(30 - len(self.item)/2) * "*")
            ledger_items = ""
            for numbers in self.ledger:
                numbers = numbers.replace(", amount", "")
                numbers = numbers.replace("description :", "")
                ledger_items = ledger_items + str(numbers) + "\n"
                ledger_items = f"{ledger_items:<25}"
            return stars + ledger_items[:]


            #second_display = stars + "\n" + textwrap.fill((display), len(numbers))




food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(food.get_balance())
