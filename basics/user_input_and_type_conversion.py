# making prog interactive by input() function

name = input("Enter your name: ")   # Wait for the user to type something and press Enter.

print("Hello,", name)

# another example

city = input("Which city do you live in? ")

print("You live in", city)

# conversion from text to int

name2 = input("enter your name ")
age = int(input("enter your age "))
country = input("enter your country ")

print("Name: ", name2)
print("Age: ", age)
print("Country: ", country)

print(f"your Name is {name2}, your Age is {age} and you live in {country}")

height = float(input("Enter your height: ")) # convert to float


#mini challenge

# Program to collect student information and display a summary

# Entering student information using input()
name = input("enter your name: ")
student_class = input("enter your class: ")
university = input("enter your university: ")
dream_career = input("enter your dream career: ")

# Printing the header

print()
print("==============================")
print("     STUDENT INFORMATION" )
print("==============================")
print()

# Displaying the inputs

print("enter your name:", name)
print("enter your class:", student_class)
print("enter your university:", university)
print("enter your dream career:", dream_career)

# Printing the summary section

print()
print("========== SUMMARY ==========")
print()
print(f"Welcome, {name}!")
print()
print(f"You are studying in {student_class} at {university}.")
print()
print(f"Your dream career is {dream_career}.")
print()
print("Best wishes for your Python journey!")


# calculating total price

price = float(input("Enter price of one book: "))

quantity = int(input("Enter number of books: "))

total_cost = price*quantity

print("Total Cost =", total_cost)