# Encapsulation means keeping an object's internal data protected and controlling how other code can interact with it.

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount   # name mangling , internal/private
            print("Deposit successful")
        else:
            print("Invalid deposit")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid withdrawal")
        else:
            self.__balance -= amount
            print("Withdrawal successful")

    def show_balance(self):
        print("Balance:", self.__balance)

account = BankAccount("john", 4000)
account.deposit(0)         # object controls its own data and enforces its own rules
account.deposit(2000)
account.show_balance