# Inheritance allows one class to reuse the attributes and methods of another class.

class employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"My Name is {self.name}")
        print(f"My Salary is {self.salary}")


class manager(employee):             # child class : class that inherits.

    def __init__(self, name, salary, department):    # Giving the child its own __init__()
        super().__init__(name, salary)   # super() allows the child class to use the parent's version.
        self.department = department

    def show_department(self):
        print(f"My Department is {self.department}")


employee1 = manager("mun", 12000, "computer science")

employee1.show_details()
employee1.show_department()

# another imporant concept about inheritance is method-overriding. A child can also replace a parent's method.
# example

class Animal:

    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):

    def speak(self):
        print("Dog says: Woof!")

dog = Dog()

dog.speak()     