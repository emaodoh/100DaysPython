class BankServices:
    def __init__(self, balance):
        self.balance = balance

    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
            return True

        else:
            print("amount can not be 0 or less than 0")
            return False

    def withdraw(self, amount):
        if amount < 0 :
            print("amount can not be less than 0")
            return False

        if amount <= self.balance:
            self.balance -= amount
            return True

        else:
            print("Insufficiant fund")
            return False

    def show_balance(self):
        return f"Balance: {self.balance}"
        