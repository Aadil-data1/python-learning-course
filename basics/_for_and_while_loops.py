# What Is a Loop?
# A loop is a programming structure that repeats a block of code.
# range(): important python function. 

#Multiplication Table of 8
for i in range(1, 11):
    print(8, "×", i, "=", 8 * i)

# while Loop
# Use it when repetition depends on a condition.

number = 2

while number <= 8:
    print(number)
    number = number + 2

print("Finished")

# user's demand for stars

num_stars = int(input("How many stars? "))


count = 0

while count < num_stars:
    print("*")
    count += 1

#nested loops

for row in range(1, 4):  # repeat for each row
    for column in range(1, 6): #print stars in this row
        print("*", end="")

    print()  #move to next line