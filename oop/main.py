class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        if amount == 0:
            print("Enter an amount greater than 0")
        elif self.balance >= amount:
            self.balance -= amount
        else:
            print("low balance")
        
        return self.balance

    def show_balance(self):
        return f"{self.owner}`s balance is ${self.balance}"

bankAccount1 = BankAccount("emmanuel", 10)
print(bankAccount1.balance)
bankAccount1.deposit(5000)
bankAccount1.withdraw(2000)
print(bankAccount1.show_balance())