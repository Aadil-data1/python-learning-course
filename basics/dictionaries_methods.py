# creating dictionary

student = {
    "name": "Taha",      #keys : values
    "marks": 82,
    "age": 17
}

print(student["name"])  #accessing dictionary

student["marks"] = 90 # modifying a dictionary
student["city"] = "Delhi" # adding a new key 
del student["city"] # removing a key 

print(student.keys())
print(student.values())    # dictionary methods
print(student.items())

for key, value in student.items():     # looping through dictionary
    print(key, ":", value)

# nested dictionaries
 
students = {
    "student1": {
        "name": "Aadi",
        "marks": 90
    },                               # dictionary within dictionary
    "student2": {
        "name": "Rahul",
        "marks": 85
    }
}

print(students["student1"]["name"])


# program to find the highest vlaue

marks = {
    "Math": 85,
    "English": 78,
    "Python": 95,
    "Physics": 72
}

highest_subject = None
highest_mark = -1

for subject, mark in marks.items():
    if mark > highest_mark:
        highest_mark = mark
        highest_subject = subject

print(highest_subject)
print(highest_mark)

# dictionary comprehension

numbers = [1, 2, 3, 4, 5]
squares = {}

for number in numbers:
    squares[number] = number ** 2

squares = {number: number ** 2 for number in numbers}

# can also use dictionary comprehension with conditions
