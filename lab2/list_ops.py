# * Section 1 (Lists)

# * dd: NumList Data Definition

# a NumList is one of 
# - "mt", or 
# - Pair(first, next)

import unittest

class Pair:
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

    def __eq__(self, other):
        return ((type(other) == Pair)
          and self.first == other.first
          and self.rest == other.rest
        )

    def __repr__(self):
        return ("Pair({!r}, {!r})".format(self.first, self.rest))

# * 1:

# NumList -> A number
# returns the number of values in the list
def length(numList):
    if (numList == "mt"):
    	return 0
    else:
    	return 1 + length(numList.rest)

# * 2:

# NumList -> int
# returns the sum of the values in the linked list
def sum(numList):
	if (numList == "mt"):
		return 0
	else:
		return numList.first + sum(numList.rest)
# * 3:

# LinkedList Value -> integer
# returns the number of values in the linked list that are greater than the value
def count_greater_than(numList, value):
	if (numList == "mt"):
		return 0
	else:
		if numList.first > value:
			return 1 + count_greater_than(numList.rest, value)
		else: 
			return count_greater_than(numList.rest, value)

# * 4:

# LinkedList Value -> integer
# takes in the linked list and a value, and returns the position of the value in the list
def find(numList, value, index = 0):
	if (numList == "mt"):
		return None
	elif numList.first == value:
		return index
	else:
		return find(numList.rest, value, index + 1)


# * 5:

# LinkedList -> LinkedList 
# takes in a Linkedlist, and returns a new linkedList where every value is reduced by one
def sub_one_map(numList):
	if (numList == "mt"):
		return 0
	else:
		return Pair(numList.first - 1, sub_one_map(numList.rest))
		
# * 6:

def insert(numList, num):
	if (numList == 'mt'):
		return Pair(num, 'mt')
	elif num > numList.first:
		return Pair(numList.first, insert(numList.rest,num))
	else:
		return Pair(num, numList)

# * Tests : the test case class for the list functions

class TestCases(unittest.TestCase):

	def test_length(self):
		list = "mt"
		self.assertEqual(length(list), 0)

	def test_length_2(self):
		list2 = Pair(2, Pair(3, Pair(4, Pair(5, "mt"))))
		self.assertEqual(length(list2), 4)

	def test_sum(self):
		list = "mt"
		self.assertEqual(sum(list), 0)

	def test_sum_2(self):
		list2 = Pair(2, Pair(3, Pair(4, Pair(5, "mt"))))
		self.assertEqual(sum(list2), 14)

	def test_count_greater_than(self):
		list = "mt"
		value = 5
		self.assertEqual(count_greater_than(list, value), 0)

	def test_count_greater_than_2(self):
		list = Pair(2, Pair(3, Pair(4, "mt")))
		value = 3
		self.assertEqual(count_greater_than(list, value), 1)

	def test_count_greater_than_3(self):
		list = Pair(10, Pair(2, Pair(6, Pair(100, Pair(7, Pair(19, "mt"))))))
		value = 11
		self.assertEqual(count_greater_than(list, value), 2)

	def test_find(self):
		list = "mt"
		value = 10
		self.assertEqual(find(list, value), None)

	def test_find_2(self):
		list = Pair(2, Pair(4, Pair(3, Pair(8, (Pair(12, "mt"))))))
		value = 4 
		self.assertEqual(find(list, value), 1)

	def test_find_3(self):
		list = Pair(0, Pair(20, Pair(100, Pair(60, Pair(25, "mt")))))
		value = 60
		self.assertEqual(find(list, value), 3)

	def test_sub_one_map(self):
		list = "mt"
		self.assertEqual(sub_one_map(list), 0)

	def test_sub_one_map_2(self):
		list = Pair(2, Pair(3, Pair(4, Pair(5, "mt"))))
		self.assertEqual(sub_one_map(list), Pair(1, Pair(2, Pair(3, Pair(4, 0)))))

	def test_sub_one_map_3(self):
		list = Pair(10, Pair(22, Pair(100, Pair(60, "mt"))))
		self.assertEqual(sub_one_map(list), Pair(9, Pair(21, Pair(99, Pair(59, 0)))))

	def testinsert0(self):
		y = 'mt'
		self.assertEqual(insert(y,2),Pair(2,'mt'))

	def testinsert(self):
		y = Pair(4,Pair(9,'mt'))
		z = Pair(4,Pair(5,Pair(9,'mt')))
		self.assertEqual(insert(y,5),z)

	def testinsert2(self):
		y = Pair(4,Pair(9,'mt'))
		z = Pair(4,Pair(9,Pair(10,'mt')))
		self.assertEqual(insert(y,10),z)

	def testinsert3(self):
		y = Pair(4,Pair(9,'mt'))
		z = Pair(2,(Pair(4,Pair(9,'mt'))))
		self.assertEqual(insert(y,2),z)

if __name__ == '__main__':
	unittest.main()

