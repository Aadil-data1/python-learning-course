# A class is a blueprint, and an object is something created from that blueprint.

class BankAccount:

    def __init__(self, owner, balance):   # this method runs automatically when we create an object
        self.owner = owner              # is an attribute stored inside the particular object
        self.balance = balance

    def deposit(self, amount):                         # creating methods
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        print("you have deposited: ", amount)
        print("your new balance is:", self.balance)
        
        return self.balance 
        
    def withdraw(self, amount) :
        if amount > self.balance:
            print("insufficient balance")
        else:
            self.balance -= amount

            print("you have withdrawn: ", amount)

        
        print("you balance after withdrawl is: ", self.balance)
        return self.balance

    def show_balance(self):
        print("your current balance is : ", self.balance)

    def __str__(self):                                       # describe the object as text
        return (f"Owner: {self.owner} , Balance: ,{self.balance}")

bankaccount1 = BankAccount("Tariq", 2000)  # creating an object and also giving it data
bankaccount1.deposit(4000)           # methods can change the state of object
bankaccount1.show_balance()
bankaccount1.withdraw(5000)
bankaccount1.show_balance()
print(bankaccount1)