# Different objects can use the same method name, but behave differently.

class Vehicle:

    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):

    def move(self):
        print("Car is driving")


class Boat(Vehicle):

    def move(self):
        print("Boat is sailing")

car = Car() 
boat = Boat()

vehicles = [car, boat]

for vehicle in vehicles:
    vehicle.move()        # same method, different behaviour