
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
        """ transfers a desired amount of money from one category to another"""
        Category.item = item2
        self.transfer_amt = transfer_amt
        if transfer_amt < self.deposit_amt:
            self.ledger.append({"description": f"Transfer to {item2.item}", "amount": (-1) * self.transfer_amt})
            item2.ledger.append({"description": f"Transfer from {self.item}", "amount": self.transfer_amt})
            self.balance = self.deposit_amt - self.transfer_amt
            item2.deposit_amt = self.transfer_amt
            item2.balance = item2.deposit_amt + self.transfer_amt
            return True
        return False

    def __str__(self):
        """ prints out the ledger list in a neat formatted way, so that it is easier
        to understand for the end user"""
        stars = (self.item.center(30, "*"))+"\n"
        ledger_items = ""
        for dictionary in self.ledger:
            for key in dictionary.keys():
                numbers = dictionary["amount"]
            for value in dictionary.values():
                words = dictionary["description"]
                cut_words = (words[0:23])

            ledger_items = ledger_items + f"{cut_words}{format(numbers,'.2f').rjust(len(stars) - len(cut_words) -1, ' ')}\n"
        total = f"Total: {format(self.get_balance(),'.2f')}"
        return stars + str(ledger_items[:])+ total

    def total_category_withdrawals(self):
        category_withdrawals = 0
        for i in self.ledger:
            if i["amount"] < 0:
                category_withdrawals += i["amount"]
        return category_withdrawals

##########################################################################################################################################
    #spemd chart implementation


def create_spend_chart(categories):
    """this function  sums up the withdrawals of all categories (100%) and then provides the
    withdrawals of one category as a percentage of the 'total withdrawal', depicting this in
    a bar chart."""

    #collecting the data of category withdrwals in a list, and computing the sum of total withdrawals
    cat = Category
    category_withdrawals = []
    total_withdrawals = 0
    for cat in categories:
        total_spent_per_cat = cat.total_category_withdrawals()
        category_withdrawals.append(total_spent_per_cat)
    total_withdrawals = sum(category_withdrawals)

    #ensuring that all category titles have the same length
    chart_titles = []
    cat_dic = {}
    for cat in categories:
        cat_dic[str(cat.item)] = len(str(cat.item))
        longest_word = max(cat_dic.values())
    for key, value in cat_dic.items():
        if value == longest_word:
            cat_title = key
            chart_titles.append(cat_title)

        else:
            value = longest_word - value
            extra_spacing = str(value * ' ')
            cat_title = key + extra_spacing
            chart_titles.append(cat_title)

    #implementing the correct formatting for the category titles
    category_chart_names = " "
    for word in chart_titles:
        for i in range(len(word)):
            if len(chart_titles) == 4:
                category_chart_names += " " + (f"    {chart_titles[0][i]}  {chart_titles[1][i]}  {chart_titles[2][i]}  {chart_titles[3][i]}\n ").rjust(12)
            elif len(chart_titles) == 3:
                category_chart_names += " " + (f"    {chart_titles[0][i]}  {chart_titles[1][i]}  {chart_titles[2][i]}\n ").rjust(12)
            elif len(chart_titles) == 2:
                category_chart_names += " " + f"    {chart_titles[0][i]}  {chart_titles[1][i]}\n ".rjust(12)
            elif len(chart_titles) == 1:
                category_chart_names += " " + f"    {chart_titles[0][i]}\n ".rjust(12)
            else:
                return "Sorry you cannot display data for more than four categories at a time"
        break
    category_chart_names = (category_chart_names).rjust(9) + "\n"

    #gathering the percentage data
    percentages = []
    for number in category_withdrawals:
        percentage = round((number / total_withdrawals) * 100)
        percentages.append(percentage)
    #print(percentages)
    #creating bars: matching each bar with its appropriate category
    bars = []
    for percentage in percentages:
       number_of_bars = round((percentage / 10), 0)
       bar = int(number_of_bars) * "o"
       bars.append(bar)
    #print(bars)

    # formatting the bar to ensure that all the bars have the same length
    bar_dic = {}
    equal_length_bars = []
    for bar in bars:
        bar_dic[bar] = len(str(bar))
    for key, value in bar_dic.items():
        if value == 10:
            bar_ = key
            equal_length_bars.append(bar_)
        else:
            value = 10 - value
            extra_spacing = str(value * ' ')
            bar_ = extra_spacing + key
            equal_length_bars.append(bar_)

    #first steps top the creation of the bars
    bark = " "
    j = 110
    for dot in equal_length_bars:
        while j >= -10:
            for i in range(len(dot)):
                if len(equal_length_bars) == 4:
                    j -= 10
                    bark += " " + (f"{j}| {equal_length_bars[0][i]}  {equal_length_bars[1][i]}  {equal_length_bars[2][i]}  {equal_length_bars[3][i]}\n ").rjust(12)
                    if j == 10:
                        break
                elif len(equal_length_bars) == 3:
                    j -= 10
                    bark += (f"{j}|"+ f" {equal_length_bars[0][i]}  {equal_length_bars[1][i]}  {equal_length_bars[2][i]}\n ").rjust(14)
                    if j == 10:
                        break
                elif len(equal_length_bars) == 2:
                    bark += " " + (f"{j}| {equal_length_bars[0][i]}  {equal_length_bars[1][i]}\n").rjust(12)
                    j -= 10
                    if j == 10:
                        break
                elif len(equal_length_bars) == 1:
                    bark += " " + (f"{j}| {equal_length_bars[0][i]}\n ").rjust(10)
                    j -= 10
                    if j == 10:
                        break
            if j == 10:
                break
        break

    bark = bark + f"  0| {len(equal_length_bars)* 'o  '} \n"



    title = " Percentage spent by category\n"

    #putting everything together in the final return statement
    return title + bark + f"     {2*(len(categories) + 2) * '-'}\n" + category_chart_names.rjust(9)
