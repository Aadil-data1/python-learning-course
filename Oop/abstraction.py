# “Abstraction is the process of hiding implementation details and exposing only essential features.”

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):

    def pay(self, amount):
        print("Paid by Credit Card")        

class UPI(Payment):                        # The abstraction establishes: Every payment type must provide pay()

    def pay(self, amount):
        print("Paid via UPI")

class PayPal(Payment):

    def pay(self, amount):
        print("Paid via PayPal")



payments = [CreditCard(), UPI(), PayPal()]   

for payment in payments:
    payment.pay(1000)