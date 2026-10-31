# Understanding Indentation
# example: if age >= 18:
#    print("Eligible")
# the spaces before print() are called indentation.

# ATM example
balance = 1000
withdraw = int(input("Enter withdrawal amount: "))

if withdraw <= balance:
    print("Transaction Approved")

# Movie Ticket Checker.
name = input("enter your name: ")
age = int(input("enter your age: ")) 
if age>=15:
    print("=====MOVIE TICKET=====")
    print("Name: ", name)
    print("Status: Entry Allowed")
    print("Enjoy the movie")
else:
    print("=====TICKET DENIED=====")
    print("Name: ", name)
    print("Status: Entry Denied")
    print("You must be 15 or older to watch this movie.")

# password checker

password = input("Enter password: ")

if password == "python123":
    print("Access Granted")
else:
    print("Access Denied")

# student performance Analyzer

_name = input("enter your name: ")
_marks = int(input("enter your marks :"))
if _marks >= 90:
    grade = "A"
    performance = "Excellent"

elif _marks >= 75:
    grade = "B"
    performance = "Very Good"

elif _marks >= 60:
    grade = "C"
    performance = "Good"

elif _marks >= 40:
    grade = "D"
    performance = "Average"

else:
    grade = "E"
    performance = "Fail"

print("====== Overall Performance ======")
print("Name:", _name)
print("Marks Obtained:", _marks)
print("Performance:", performance)
print("Grade:", grade)

#nested if

age = int(input("enter your age: "))

if age >= 18:
    print("Age requirement met.")

    has_id = input("Do you have an ID? (yes/no): ")

    if has_id == "yes":
        print("Entry Allowed")

#nested if...else
# Bank ATM verification


card_inserted = input("Have you inserted your card? (yes/no): ")

if card_inserted == "yes":

    entered_pin = int(input("enter your PIN: "))
    correct_pin = 1234

    if entered_pin == correct_pin:

        withdrawal = int(input("enter withdrawal amount: "))
        account_balance = 1000

        if withdrawal <= account_balance:
            print("Status: Transaction Successful")
        else:
            print("Status: Insufficient Balance")

    else:
        print("Incorrect PIN")

else:
    print("Please Insert Your Card")