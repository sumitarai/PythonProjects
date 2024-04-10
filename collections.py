# There are four collection data types in the Python programming language:
'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

'''

thislist = ["apple", "banana", "cherry", 1]
print(thislist[-2])


thistuple = ("apple", "banana", "apple")
print(thistupple)

thisset = {"apple", "cat", "cat"}  
x= list(thisset)
print(x[1])

thisdict = {"firstname":"Mimi", "lastname":"Rai", "Year":2004}
print(thisdict["lastname"])




thislist = list(("apple", "banana", "cherry"))
print(type(thislist))

thislist2 = thislist

thislist1 = ["apple", "banana", "cherry"]
print(type(thislist1))
print(thislist is thislist2)


# tupple is immutable. Cannot change but you can assign tuple to list and then change the value
thistuple = ("apple", "banana", "cherry")
thislist = list(thistuple)
print(thislist)
thislist[1] = 'mango'
print(thislist)
print(type(thislist))

thistuple = tuple(thislist)
print(thistuple)
print(type(thistuple))


# Access List Item >> This will return the items from position 2 to 5.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#Remember that the first item is position 0, #and note that the item in position 5 is NOT included

#To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)