# Python is an object oriented programming language with its properties and methods.
# Class is like a object constructor (blueprint) help to create an object.

# To create a class, use the keyword class. Naming convention to write class name in camelcase. Example: MyClass
# Variable written in snake case. Example: my_variable

class MyClass:
    x = 5

# instantiate the class and create an object called my_object and print the value of x:
my_object = MyClass()            # Create an object of MyClass called my_object
print(my_object.x)               # object name and then variable


"""
Lets define a class called Person, add a __init__ method that initializes the member variables name and age.
"""
class Person:
    def __init__(self, p_name, p_age):
        self.name = p_name
        self.age = p_age

# The __init__() function is called automatically every time the class is being used to create a new object.
# Now initialize the Person objects with corresponding data
p1 = Person("sumi", 50)
p2 = Person("Prakash", 60)

print("Hello! " , p1.name, ". You are " , p1.age , " years old today.")
print(p2.name, p2.age)

# Modify age properties on p1 object like below
p1.age = 44
print(p1.age) 


# Delete age properties on p2 object by using the del keyword:
del p2.age
# print(p2.age) 


class Cars:
    def __init__(self, name, year):
        self.name = name
        self.name = year

    def my_car(self):
        print("This is my car obejct method")

p1 = Cars("Toyota", 2024)
p1.my_car()


# The string representation of an object WITH the __str__() function,
# The __str__() function controls what should be returned when the class object is represented as a string.
class Student:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return f"{self.name, self.gender}"
    
p1 = Student("Sumi", "F")
print(p1)

'''
The Pass statement >> class definitions cannot be empty, but if you for some reason have a class definition with no content, 
then put in the pass statement to avoid getting an error.
'''
class MyPass:
    pass



'''
Python Inheritance allows us to define a class that inherits all the methods and properties from another class.
parent class- base class
Child class- derived class
The child's __init__() function overrides the inheritance of the parent's __init__() function.
By using the super() function, you do not have to use the name of the parent element, 
it will automatically inherit the methods and properties from its parent.

'''

class Student(Person):
  def __init__(self, fname, lname, year):
    #Person.__init__(self, fname, lname)
    super().__init__(fname, lname)
    self.graduationyear = year

  x = Student("Mike", "Olsen", 2019)
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

print("end of the python class")