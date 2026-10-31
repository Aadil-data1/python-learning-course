# What Is a Parameter?
# A parameter is a variable that belongs to a function.
# example
def greet(name):   #name = parameter(the variable waiting to receive information)
    print("Hello", name)

greet("john")   #john = argument(the actual information)

# calculate grade of a students

def report(name, marks):

    print("Name:", name)
    print("Marks:", marks)

    if marks >= 90:
       print("Grade: A")
       print("Excellent")

    elif marks >= 75:
       print("Grade: B")
       print("Very Good")

    elif marks >= 60:
       print("Grade: C")
       print("Good")

    else:
       print("Grade: D")
       print("Needs Improvement")

    print("-----------------")

report("shakir", 72)
report("sunny", 80)

# Default Parameters:
# A default parameter is a value Python uses when you don't provide one yourself.
# Example

def student(name, marks, subject="Python"):   # Required parameters first, default parameters afterward.
   print(name)
   print(marks)
   print(subject)


def calculate_total(price, quantity=1):
   return price * quantity

#total = calculate_total(100)
#print(total)

_total = calculate_total(price=100, quantity= 5)  #using keyword argument
print(_total)

# mini exercise/project

student = {                         # creating dictionary
    "name": "umar",         
    "marks": [85, 72, 91, 64, 78]   # stores marks in a list
}
def calculate(student):
   name = student["name"]

   total = 0

   for mark in student["marks"]:
      total += mark

   average = total / len(student["marks"])
   maximum_marks = max(student["marks"])
   minimum_marks = min(student["marks"])

   if total>= 250:
      result = "pass"

   else:
      result = "fail"

   return name, total, average, maximum_marks, minimum_marks, result

name, total, average, maximum_marks, minimum_marks, result = calculate(student)   # unpacking

print(print(
    "Name:", name,
    "\nTotal:", total,
    "\nAverage:", average,
    "\nMaximum Marks:", maximum_marks,
    "\nMinimum Marks:", minimum_marks,
    "\nResult:", result
))







