'''
The word "polymorphism" means "many forms".
It refers to methods/functions/operators with the same name that can be executed on many objects or classes.
'''

class Car:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def move(self):
        print(self.name, "Drives!")

class Plane:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def move(self):
        print(self.name, "Fly!")

print("Class Polymorphism")
# instantiate class and create an objects vehicle1 & vehicle2
vehicles1 = Car ("Toyota", "Seiana")
#vehicles1.move()
vehicles2 = Plane("Boeing", "MAX372")
#vehicles2.move()

for x in (vehicles1, vehicles2):
    x.move()



'''
Inheritance Class polymorphism
Parent class called Vehicle, and make Car, Boat child classes of Vehicle, 
the child classes inherits the Vehicle methods, but can override them
'''

class Vehicle:
    def __init__(self, name, brnad):
        self.name = name
        self.brand = brnad

    def move(self):
        print("Move")

    
class Cars(Vehicle):
    def move(self):
        print(self.name, " Drive!")


class Boats(Vehicle):
    def move(self):
        print(self.name, " Sail!")

print("Inheritance Class polymorphism")
x = Cars("Toyota", "Priyus")
y = Boats("Yamaha", "ZX240")

for vehicle_move in (x, y):
    vehicle_move.move()