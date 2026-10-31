# Return gives a result back to a program. Also, it Immediately Ends the Function
#  Example
def multiply(a, b):
    return a*b

product = multiply(7,9)
print(product)

# Local Variable:
# A local variable exists inside the function where it was created.

# Global Variable:
# created outside the function.

name = "Aadi"   # Global

def greet():
    print(name)

def greet():    
    name = "Aadi"     # Local
    print(name)


 # Student Result System

def calculate_grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 40:
        return "D"

    else:
        return "F"


grade = calculate_grade(84)

print("Grade:", grade)