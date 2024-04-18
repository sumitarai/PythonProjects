# In Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
# Return an iterator from a tuple, and print each value:
mytupple = ("apple", "banana", "orange")
myiter = iter(mytupple)

print(next(myiter))
print(next(myiter))
print(next(myiter))

print(type(myiter))

# for loop to iterate through an iterable object:
for x in mytupple:
    print(x)


# Stop iteration statement to prevent the iteration from going on forever or prevent any error

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
