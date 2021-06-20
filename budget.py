

class Category:

    def __init__(self, item):
        self.item = item
        self.ledger = list()
        self.balance = 0


    def deposit(self, deposit_amt, deposit_descrpt = False):
        self.deposit_amt = deposit_amt
        self.deposit_descrpt = deposit_descrpt
        self.balance = 0 + deposit_amt
        if self.deposit_descrpt:
            x = {"description": f"{self.deposit_descrpt}", "amount": f"{format(self.deposit_amt,'.2f')}"}
            self.ledger.append(x)
        if not self.deposit_descrpt:
            x = {"description": " ", "amount": f"{format(self.deposit_amt, '.2f')}"}
            self.ledger.append(x)

    def get_balance(self):
        return float(self.balance)

    def check_funds(self, amt):
        self.amt = amt
        if self.amt > self.get_balance():
            return False
        return True

    def withdraw(self, withdraw_amt, withdraw_descrpt = False):
        self.withdraw_amt = withdraw_amt
        self.withdraw_descrpt = withdraw_descrpt
        if self.withdraw_descrpt:
            ledger_item = {"description": f"{self.withdraw_descrpt}", "amount": f"{format((-1) * self.withdraw_amt,'.2f')}"}

        if not self.withdraw_descrpt:
            ledger_item = {"description": " ", "amount": f"{format((-1) * self.withdraw_amt,'.2f')}"}
        if self.check_funds(self.withdraw_amt):
            self.balance = self.deposit_amt - self.withdraw_amt
            self.deposit_amt = self.balance
            self.ledger.append(ledger_item)
            return True
        return False

    def __repr__(self):
        return self.item

    def transfer(self, transfer_amt, item2):
        Category.item = item2
        self.transfer_amt = transfer_amt
        if transfer_amt < self.deposit_amt:
            self.ledger.append({"description": f"Transfer to {item2.item}", "amount": f"{format((-1) * self.transfer_amt, '.2f')}"})
            item2.ledger.append({"description": f"Transfer from {self.item}", "amount": f"{format(self.transfer_amt, '.2f')}"})
            self.balance = self.deposit_amt - self.transfer_amt
            #item2.balance = item2.balance + self.transfer_amt
            return True
        return False

    def __str__(self):
        stars = (self.item.center(30, "*"))
        ledger_items = ""
        for dictionary in self.ledger:
            for key in dictionary.keys():
                numbers = dictionary[key]
            for value in dictionary.values():
                words = dictionary["description"]
                cut_words = (words[0:23])

            ledger_items = ledger_items + f"{cut_words.ljust(len(stars))} {numbers.rjust(len(stars))}  \n"
        total = f"Total: {format(self.get_balance(), '.2f')}"


        return stars + "\n" + str(ledger_items[:]) + total



#code included in the main file by FCC:test code:
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)


print(food)
print(clothing)

