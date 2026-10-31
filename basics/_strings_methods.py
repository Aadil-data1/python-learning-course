# What is a String?
# A string is simply a sequence of characters enclosed in quotation marks.
# string slicing: to get a part of a string

# Username Analyzer
user = input("enter your username: ")

if user == "pythonmaster":
    print("Username:", user)
    print("First character:", user[0])
    print("Last character:", user[-1])  #negative indexing
    print("First three characters:", user[0:3])
    print("Last three characters:", user[-3:])

else:
    print("Invalid username. Please try again.")

# String methods: title(), replace(), strip() etc
word = " Python "

print(word.upper())
print(word.strip())
print(len(word))
print(word.find("on"))

# Username Validator

username = input("Enter username: ")

if username.isalnum() and len(username) >= 5:  #string validation
    print("Username Accepted")
else:
    print("Enter a valid username")