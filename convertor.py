
def celsius_to_farenheit(celsius):
    ferenheit = (celsius * 9/5) + 32
    return ferenheit

#Example
celsius_value = 100
converted_ferenheit = celsius_to_farenheit(celsius_value)
print(f"{celsius_value:.1f} celsius is equal to {converted_ferenheit:.1f} ferenheit")



def add(x,y):
    print('adding:', x ,'and', y)
    return x+y                  # return returns a value of function and it is end of the function. 
   

result = add(10,10)
print(result)




a = 30
txt = "My friend is {} years old."
print(txt.format(a))

a = 10
b = 20
c = 30
txt = "I want {} Apples, {} Oranges, and {} Strawberries"
print(txt.format(a, b, c))

txt = "Python is an \"Awesome\" language"    #The \ escape character allows you to use double quotes in a strings
print(txt)


txt = "This will insert one \\ (backslash)."  # \\ use to show one backslash
print(txt)

txt = "Hello\nWorld!"  # \n use for new line
print(txt) 


