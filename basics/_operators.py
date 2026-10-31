# What is an Operator?
# An operator is simply a symbol that tells Python to perform an operation.

# Arithmetic Operators:
# (+), (-), (*), (/), (//), (%), (**)

# Expressions
# An expression is a combination of values, variables, and operators that Python evaluates to produce a result.

# example : (price * quantity + tax)

# calculating average

math = 92
science = 85
english = 95

average = (math + science + english) / 3

print(average)

# calculating future age

age = int(input("Enter your age: "))

future_age = age + 5

print("After five years you will be", future_age)

# calculating total bill

pizza = int(input("enter number of pizzas ordered: "))
price = float(input("enter price per pizza: "))
total_price = pizza * price
print()
print(f"you ordered {pizza} pizzas and price of each is {price}. your total bill is rs.{total_price}")
print(f"enjoy your pizza")

# calculate total salary

name = input("enter employee name:")
Hours_Worked = int(input("enter hours worked:"))
Hourly_Rate = float(input("enter hourly rate"))
Total_Salary = Hours_Worked * Hourly_Rate

print()
print("******Employee Detail******")
print("Name:", name)
print("Hours Worked:", Hours_Worked)
print("Hourly Rate:", Hourly_Rate)
print("Total Salary:", Total_Salary)


# comparison operators

# (==), (!=), (>), (<), (>=), (<=)

# every comparison produces only one of two answers:
#- True
#- False
# These are called Boolean values.

student_name = input("enter your name: ")
marks = int(input("enter makrs obtained: "))

passed = marks >= 40
perfect_score = marks > 90
need_improvement = marks < 40

print()
print("===== STUDENT REPORT =====")
print("Name:", student_name)
print("Marks:", marks)
print("Passed:", passed)
print("Perfect Score:", perfect_score)
print("Needs Improvement:", need_improvement)