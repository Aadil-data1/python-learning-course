# lambda — a tiny function. A lambda lets us write a small function in one line:
square = lambda number: number**2
print(square(4))

# map() — apply a function to every item

numbers = [10, 15, 20, 25, 30, 35, 40]
doubled = map(lambda n : n*2 , numbers)
large_numbers = list(filter(lambda n: n > 50, doubled)) # use filter to keep numbers greater than 50
print(large_numbers)