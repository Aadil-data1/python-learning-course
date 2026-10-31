# Variable: A variable is like a labeled box that stores information so you can use it later

#Variable names may contain:
# - Letters
# - Numbers
# - Underscores (_)

# A variable cannot begin with a number.

name = "faiz"
age = 25
country = "India"

print(name)
print(age)
print(country)


print("=======My profile========")
name = "Faiz"
favorite_subject = "Mathematics"
dream_career = "Ai Engineer"
favorite_language = "python"

print("Name: ", name)
print("Favorite Subject: ",  favorite_subject)
print("Dream Career: " , dream_career)
print("Favorite Programming Language: " , favorite_language)


# Data types
# A data type tells Python what kind of value is being stored.

# The Four Basic Data Types: String (str), Integer (int), Float (float), Boolean (bool)

# Seeing Data Types: type()

# example

name = "john"

print(type(name))

height = 5.8

print(type(height))

#mini exercise

name = "suresh"
age = 18
height = 5.3
student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(student, type(student))

#BMI information calculator

_name = input("enter your name: ")
_age = int(input("enter your age: "))
_height = float(input("enter your height (in mts): "))
_weight = float(input("enter your weight (in kg): "))

print()
print("========BMI Profile========")
print("Name: ", _name)
print("Age: ", _age)
print("Height: ", _height)
print("Weight: ", _weight)
print("your information has been recorded successfully")
print()
_bmi = _weight / (_height**2)
print("BMI: ", _bmi)
