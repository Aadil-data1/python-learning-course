# What is a module?
# A module is simply a Python file containing code that can be reused elsewhere.

import math               # we can also use aliases like: math as m
import datetime
import random 

print(math.sqrt(169))
print(math.pi)

number = random.randint(1,10)
print(number)

today = datetime.date.today()
print(today)

# another important python concept is 
if __name__ ==" __main__ ":          # the idea is simple: A Python file can be: Run directly or Imported into another file.
    print("program started")  # if run directly in the same file the part beneath if... executes, otherwise if imported doesn't execute automatically