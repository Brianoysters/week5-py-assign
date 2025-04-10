# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

# Subclasses with different move() methods
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Using polymorphism
def travel(vehicle):
    vehicle.move()

# Creating vehicle objects
v1 = Car()
v2 = Plane()
v3 = Boat()

# Call the same method in a polymorphic way
travel(v1)
travel(v2)
travel(v3)
