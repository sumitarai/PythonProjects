# Python is an object oriented programming language with its properties and methods.
# Class is like a object constructor (blueprint) help to create an object.

# To create a class, use the keyword class. Naming convention to write class name in camelcase. Example: MyClass
# Variable written in snake case. Example: my_variable

class MyClass:
    x = 5

# instantiate the class and create an object called my_object and print the value of x:
my_object = MyClass()
print(my_object.x)               # object name and then variable


"""
Lets define a class called Person, add a __init__ method that initializes the member variables name and age.
"""
class Person:
    def __init__(self, p_name, p_age):
        self.name = p_name
        self.age = p_age

# Now initialize the Person objects with corresponding data
p1 = Person("sumi", 50)
p2 = Person("Prakash", 60)

print("Hello! " , p1.name, ". You are " , p1.age , " years old today.")
print(p2.name, p2.age)


class Cars:
    def __init__(self, name, year):
        self.name = name
        self.name = year

    def my_car(self):
        print("This is my car obejct method")

p1 = Cars("Toyota", 2024)
p1.my_car()


