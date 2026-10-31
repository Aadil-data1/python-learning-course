# list comprehension
# challenge 1
numbers = [10, 15, 20, 25, 30, 35, 40]
twice = [x*2 for x in numbers]
print(twice)

#challenge 2
numbers = [10, 15, 20, 25, 30, 35, 40]
larger = [x  for x in numbers if x >25]   # creating a list containing numbers greater than 25
print(larger)

# challenge 3
names = ["Aadi", "Rahul", "Ali", "Sara", "John"]
lowercase_names = [n.lower() for n in names if len(n)>3 ] # list containing the names converted to lowercase only if their length is greater than 3.
print(lowercase_names)

# dictionary comprehension

marks = {
    "Math": 85,
    "History": 92,
    "English": 76,
    "Physics": 88
}

higher_marks = {subject : mark
                for subject, mark in marks.items() # Creating a new dictionary containing only subjects where the mark is 80 or above.
                if mark > 80}

print(higher_marks)

result = {subject: "A" if mark >90 else "B"
          for subject, mark in marks.items() # creating a new dictionary that converts marks into grade
          }

print(result)



