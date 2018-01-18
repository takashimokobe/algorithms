import unittest
from sys import argv

# A List is one of 
# None
# A reference to an arrary and a int representing size
class List: 
	def __init__(self, list, size):
		self.list = list
		self.size = size

	def __eq__(self, other):
		return (type(other) == List
			and self.list == other.list
            and self.size == other.size
			)

	def __repr__(self):
		return "List (%r, %r)" % (self.list, self.size)

# no arguments -> None
# this function returns an empty list. 
def empty_list():
	return List([], 0)

# list int value -> list
# puts the value at the index specified in your list
def add(alist, index, value):
	if (index < 0 or index > length(alist)):
		raise IndexError
	else:
		newList = List([None] * (length(alist) + 1), 0)
		if index != 0:
			for i in range(index):
				newList.list[i] = alist.list[i]
				newList.size += 1
			newList.list[index] = value
			newList.size += 1

			for i in range(index, length(alist)):
				newList.list[i + 1] = alist.list[i]
				newList.size += 1
		else:
			newList.list[0] = value
			newList.size += 1

			for i in range(1, length(alist) + 1):
				newList.list[i] = alist.list[i - 1] 
				newList.size += 1
		return newList

# list -> int
# returns the number of elements in the list
def length(alist):
	if (alist == None):
		return 0
	else:
		return alist.size

# list int -> value
# returns the value at the index position in the list
def get(alist, index):
	if (index < 0 or index > length(alist)):
		raise IndexError
	else:
		return alist.list[index]

# list int value -> list
# replaces the element of the index postion specified with the given value
def set(alist, index, value):
	if (index < 0 or index > length(alist)):
		raise IndexError
	else:
		newList = List([None] * length(alist), 0)
		for i in range(list.size):
			if i == index:
				newList.list[i] = value
			else:
				newList.list[i] = alist.list[i]
			newList.size += 1
		return newList

# list int - > list
# removes the value at the position index and returns a tuple of deleted element and rest of the list
def remove(alist, index):
	if (index < 0 or index > length(list)):
		raise IndexError
	else:
		if (index == length(alist) - 1):
			newList = List([None] * (length(alist) - 1), 0)

			for i in range(length(alist) - 1):
				newList.list[i] = list.list[i]
				newList.size += 1
		else:
			newList = List([None] * length(alist - 1), 0)

			for i in range(length(alist) - 1):
				if i < index:
					newList.list[i] = alist.list[i]
				else:
					newList.list[i] = alist.list[i + 1]
				newList.size += 1
		return (alist.list[index], newList)
			


