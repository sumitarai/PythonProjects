# A function is a block of code which only runs when it is called.

# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.


# In Python a function is defined using the def keyword:
def my_function():
    print("Hello from a function")

my_function()   # To call a function, use the function name followed by parenthesis


def my_function(fname):
  print(fname + " Rai")

my_function("Emil")   # Arguments are value specified after the function name, inside the parentheses.
my_function("Tobias")



# Default Parameter value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()



# function return a value using the return statement
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function("Sumi"))


# Pass statement >> function definitions cannot be empty, 
# if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
  pass


# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)

cars[0] = "Toyota"
print(cars)


