import unittest
from sys import argv

# A list is one of 
# None
# A reference to an array and a int represeting size
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
		return 'List(%r, %r)' % (self.list, self.size)

# no args -> None
# This function returns an empty list
def empty_list():
	return List([],0)

# list int value -> list
# Puts the value at the index specified in your list
def add(alist, index, value):
	if (index < 0 or index > length(alist)):
		raise IndexError
	else:
		newList = List([None]^(length(alist) + 1), 0)