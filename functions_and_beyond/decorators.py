# Decorators: Changing a Function Without Changing Its Code
# A decorator takes a function, adds something around it, and gives you back a modified function.

#def greet(name):
 #   print(f"Hello : {name}")

def add_message(func):
    def wrapper(*args, **kwargs):        # *args handles extra positional arguments. stored as tuple
      print("Starting function...")      # **kwargs handles extra keyword arguments. Stored as dictionary
      result = func(*args, **kwargs)
      print("Ending function....")
      return result
    return wrapper

@add_message                  # decorating below function greet
def greet(name):
    print(f"Hello: {name}")

greet("Jack")

