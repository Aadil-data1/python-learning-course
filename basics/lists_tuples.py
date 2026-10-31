# What Is a List?
# A list is a collection of multiple values stored under one variable

# what is a Tuple?
#  A Tuple is immutable sequence of elements. Once a tuple is created, its individual values cannot be changed.

# Using a loop to print each student's name and corresponding marks.

students = ["Taha", "Sana", "Sunny", "Bunny"] # students names in a list
marks = [73, 92, 45, 81]

print("sunny" in students)  # Searching a List
print(len(students))

for i in range(len(students)):
    print(students[i], "-", marks[i]) # use index to print each student and marks

# List also use negative indexing
print(students[-1])

# can slice the list
print(students[0:2])

# can also change the item in list
# Example: students[1] = "sara"

# we can also use .append(), .remove(), .pop(), .extend(), .sort(), .reverse(), .count() to modify a list 

# insert an element into a list
students.insert(1, "kamal") # at index 1


# calculating students result

students1 = [
    ["Taha", 73],
    ["Sana", 92],    # using nested list
    ["Sunny", 45],  
    ["Bunny", 81]
]

for student in students1:
    if student[1]>50:
        print(student[0], "---", student[1],"---", "passed")  

    else:
        print(student[0], "---", student[1],"---", "failed")


# Tuple Unpacking
# example

point = (10, 20)

x, y = point
print(x)
print(y)

    



