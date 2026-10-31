# An iterator is like a pointer that remembers where you currently are.
numbers = [10, 20, 30]
iterator = iter(numbers)
print(next(iterator))  # gives the next item one at a time, while remebering where it is

# Generator: A generator is a special kind of function that produces values one at a time.
# example

def EvenNumbers():
    for i in range(1, 1000):
        if i % 2 ==0:
            yield i 

even_number = EvenNumbers()
print(next(even_number))
print(next(even_number))

for even_number in EvenNumbers():
   print(even_number)