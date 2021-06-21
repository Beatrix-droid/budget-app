"""This is a budget app. It instantiates objects based on different budget
categories like food, clothng and entertainment. When objects are created,
they are passed in the name of the category. There is also an instance
variable that is a list"""



class Category:

    def __init__(self, item):
        self.item = item
        self.ledger = list()
        self.balance = 0


    def deposit(self, deposit_amt, deposit_descrpt=False):

        """ This function accepts an ammount and a description for an item.
        If no description is given, it defaults to an empty string"""
        self.deposit_amt = deposit_amt
        self.deposit_descrpt = deposit_descrpt
        self.balance = 0 + deposit_amt
        if self.deposit_descrpt:
            x = {"amount": self.deposit_amt, "description": f"{self.deposit_descrpt}"}
            self.ledger.append(x)
        if not self.deposit_descrpt:
            x = {"amount": self.deposit_amt, "description": ''}
            self.ledger.append(x)

    def get_balance(self):
        """ returns the current balance after withdraws, transfers and deposits have
        taken place"""
        return float(self.balance)

    def check_funds(self, amt):
        """ checks funds to see if a withdraw can happen based on the available balance"""
        self.amt = amt
        if self.amt > self.get_balance():
            return False
        return True

    def withdraw(self, withdraw_amt, withdraw_descrpt=False):
        """ similar to the deposit method. Withdraw accepts an ammount and an optional
        descritpion, and if there are enough funds, withdraws the desired amount from
        the available balance"""
        self.withdraw_amt = withdraw_amt
        self.withdraw_descrpt = withdraw_descrpt
        if self.withdraw_descrpt:
            ledger_item = {"amount": (-1) * self.withdraw_amt, "description": \
                f"{self.withdraw_descrpt}"}

        if not self.withdraw_descrpt:
            ledger_item = {"amount": (-1) * self.withdraw_amt, "description" : ''}
        if self.check_funds(self.withdraw_amt):
            self.balance = self.deposit_amt - self.withdraw_amt
            self.deposit_amt = self.balance
            self.ledger.append(ledger_item)
            return True
        return False

    def __repr__(self):
        return self.item

    def transfer(self, transfer_amt, item2):
        """ trasnsfers a desired amount of money from one category to another"""
        Category.item = item2
        self.transfer_amt = transfer_amt
        if transfer_amt < self.deposit_amt:
            self.ledger.append({"description": f"Transfer to {item2.item}", "amount": \
            (-1) * self.transfer_amt})
            item2.ledger.append({"description": f"Transfer from {self.item}", "amount": \
          self.transfer_amt})
            self.balance = self.deposit_amt - self.transfer_amt
            item2.deposit_amt = self.transfer_amt
            item2.balance = item2.deposit_amt + self.transfer_amt
            return True
        return False

    def __str__(self):
        """ prints out the ledger list in a neat formatted way, so that it is easier
        to understand for the end user"""
        stars = (self.item.center(30, "*"))
        ledger_items = ""
        for dictionary in self.ledger:
            for key in dictionary.keys():
                numbers = dictionary["amount"]
            for value in dictionary.values():
                words = dictionary["description"]
                cut_words = (words[0:23])

            ledger_items = ledger_items + f"{cut_words} {format(numbers, '.2f').rjust(len(stars) - len(cut_words) -1, ' ')}  \n"
        total = f"Total: {format(self.get_balance(), '.2f')}"


        return stars + "\n" + str(ledger_items[:]) + total


def create_spend_chart(categories):
  pass

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

print(create_spend_chart([food, clothing, auto]))

# Run unit tests automatically
#############################################################d
#development of the spending chart

def create_spend_chart(list_of_cats):
    pass