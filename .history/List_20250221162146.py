#List in python
#List is a collection which is ordered and changeable. Allows duplicate members.

#Creating a List
thislist = ["apple", "banana", "cherry","pineapple","orange","grapes"]
print(thislist)
print(thislist[0])
print(thislist[0][2])
print(thislist[1:])
print(thislist[1:4])
print(thislist[-1])
print(type(thislist))
print(len(thislist))
name = 'strawberry'
print(type(name))
print(thislist + [name])
thislist[1] = 'blackcurrant'
print(thislist)
cities = ['cairo','alex','aswan',2,True,'luxor']
print(cities)
vegetables = list(('potato',3,False))
print(vegetables)
print(type(vegetables))

##list methods
#append()	Adds an element at the end of the list
thislist.append('mango')
print(thislist)
#insert()	Adds an element at the specified position
thislist.insert(1,'kiwi')
print(thislist)
#remove()	Removes the first item with the specified value
thislist.remove('kiwi')
print(thislist)
#pop()	Removes the element at the specified position
thislist.pop(2)
print(thislist)
#del()	Removes the element at the specified position
del thislist[2]
print(thislist)
#clear()	Removes all the elements from the list
thislist.clear()
print(thislist)
#copy()	Returns a copy of the list
thislist = ["apple", "banana", "cherry","pineapple","orange","grapes"]
newlist = thislist.copy()   
print(newlist)
#count()	Returns the number of elements with the specified value

print(thislist.count('apple'))
#extend()	Add the elements of a list (or any iterable), to the end of the current list
newlist.extend(thislist)
print(newlist)
#reverse()	Reverses the order of the list
newlist.reverse()
print(newlist)
#sort()	Sorts the list
newlist.sort()
print(newlist)





