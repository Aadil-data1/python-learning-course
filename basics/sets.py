# What is a set?
# A set is a collection that does not allow duplicate values.

# Checking membership
languages = {"Python", "Java", "C++"}

if "Python" in languages:
    print("Python is available")

languages.add("Html")
print(languages)

languages.discard("C#")
print(languages)         # element is not present so no error occurs, but is not the case with .remove()  

# Set Operations

website_a = {"Aadi", "Rahul", "Sara", "John"}
website_b = {"Sara", "John", "Emma", "David"}

both = website_a & website_b    # Users registered on both websites
print(both)

all_users = website_a | website_b # Users registered on at least one website
print(all_users)

only_a = website_a - website_b #Users registered on A but not B
print(only_a)

