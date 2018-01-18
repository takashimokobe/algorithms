# a arrayList is one of 
# a reference to an empty list, with size 0
# reference to a list, and an int representing size
class List:
	def __init__(self, list, size):
		self.list = list
		self.size = size

	def __eq__(self, other):
		return (type(other)== List
			and self.list == other.list
			and self.size == other.size
			)

	def __repr__(self):
		return "List(%r, %r)" % (self.list, self.size)

# no arguments -> List([], 0)
# returns an empty list, with size 0
def empty_list():
	return List([], 0)

# list, int, value -> list
# puts the value specified at the index in your list, and returns a list. 
def add(alist, index, value):
	if (index < 0 or index > length(alist)):
		raise IndexError
	else:
		newList = List([None] * (length(alist) + 1), 0)
		if index == 0:
			newList.list[0] = value
			newList.size += 1
			for i in range(1, length(alist) + 1):
				newList.list[i] = alist.list[i-1]
				newList.size += 1
		else:
			for i in range(index):
				newList.list[i] = alist.list[i]
				newList.size += 1
			newList.list[index] = value
			newList.size += 1

		return newList

# list -> int 
# returns the number of items in the list 
def length(alist):
	return alist.size

# list int -> value
# returns the value at a given index in the list
def get(alist, index):
	if (index < 0 or index > length(alist)):
		raise IndexError
	else:
		return alist.list[index]

# list int value -> list
# sets the value at the given index, and returns the newList
def set(alist, index, value):
	if (index < 0 or index > length(alist)):
		raise IndexError
	else:
		newList = List([None] * length(alist), 0)

		for i in range(alist.size):
			if i == index:
				newList.list[i] = value
			else:
				newList.list[i] = alist.list[i]
			newList.size += 1
		return newList

# list int ->tuple
# removes the value at index given, and returns a tuple of deleted element and the newList
def remove(alist, index):
	if (index < 0 or index > length(alist)):
		raise IndexError
	else:
		newList = List([None] * (length(alist)-1), 0)
		if (index == length(alist)-1):
			for i in range(length(alist)-1):
				newList.list[i] = alist.list[i]
				newList.size += 1
		else:
			for i in range(length(alist)-1):
				if (i < index):
					newList.list[i] = alist.list[i]
				else:
					newList.list[i] = alist.list[i+1]
				newList.size += 1
		return (alist.list[index], newList)

# list function -> null
# allows us to access each element in our array list
def foreach(alist, function):
	for index in range(length(alist)):
		function(get(alist, index))

# list, lessthan -> alist
# sorts your list in descending order
def sort(alist, lessthan):
	for index in range(length(alist)):
		value = get(alist, index)
		position = index
		while lessthan == True:
			x = get(alist, position)
			y = get(alist, position - 1)
			x = y
			position = position - 1
		x = value
	return alist