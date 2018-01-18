# A Huffman Tree is one of 
# None, or 
# Huffman Node, Leaf

import array_list
import linked_list
from sys import *
from huffman_bits_io import *
import os
import unittest

arr_list = array_list.List([0] * 256, 256)

class Leaf:
	def __init__(self, char, count):
		self.char = char
		self.count = count

	def __eq__(self, other):
		return ((type(other) == Leaf)
			and self.char == other.char
			and self.count == other.count
			)

	def __repr__(self):
		return ("Leaf({!r}, {!r})".format(self.char, self.count))

class HuffmanNode:
	def __init__(self, char, count, left, right):
		self.char = char
		self.count = count
		self.left = left
		self.right = right

	def __eq__(self, other):
		return ((type(other)== HuffmanNode)
			and self.char == other.char
			and self.count == other.count
			and self.left == other.left
			and self.right == other.right
			)

	def __repr__(self):
		return ("HuffmanNode({!r}, {!r}, {!r}, {!r})".format(self.char, self.count, self.left, self.right))

# file -> list 
# opens a text file and counts the frequency or all the characters within the file
def count_occurances(filename):
	list = array_list.empty_list()
	list.list = [None] * 256
	for i in range(0, 256):
		list = array_list.add(list, i, 0)
	with open(filename) as file:
		for line in file:
			for c in line:
				list = array_list.set(list, ord(c), array_list.get(list, ord(c)) + 1)
	return list

# Huffman Tree -> string
# creates a string by traversing the tree in a pre-order traversal and appending the characters of the leaf nodes
# NODE LEFT RIGHT
def traverse(hTree):
	if hTree is None:
		return ""
	if (type(hTree) == Leaf):
		return chr(hTree.char)
	else:
		return traverse(hTree.left) + traverse(hTree.right)

# HuffmanTree, HuffmanTree -> boolean
# returns true if Tree A comes before Tree B
def comes_before(a, b):
	if a.count == b.count:
		return a.char < b.char
	else:
		return a.count < b.count

# list -> HuffmanNode
# builds a Huffman Tree from a given list of occurances
def build_tree(occurances):
	list = linked_list.empty_list()
	index = 0
	for value in occurances.list:
		if value > 0:
			list = linked_list.insert_sorted(list, Leaf(index, value), comes_before)
		index += 1
	while linked_list.length(list) > 1:
		l, list = linked_list.remove(list, 0)
		r, list = linked_list.remove(list, 0)
		minchar = min(l.char, r.char)
		node = HuffmanNode(minchar, l.count + r.count, l, r)
		list = linked_list.insert_sorted(list, node, comes_before)
	return node

# Node, char, string -> List
# traverses the Huffman tree from root to each node, adding 0 when left and 1 when right
def characterCode(node, arr_list, code = ""):
	if node == None:
		return code + "0"
	if type(node) == Leaf:
		arr_list = array_list.set(arr_list, node.char, code)
		return arr_list
	else:
 		arr_list = characterCode(node.right, arr_list, code + "1")
	return arr_list

# input output ->
# Huffman Encodes the tree
def huffman_encode(input, output):
	frequency = count_occurances(input)
	tree = build_tree(frequency)
	code = characterCode(tree, arr_list)
	hb_writer = HuffmanBitsWriter(output)
	string = ""
	counter = 0

	if frequency is None:
		hb_writer.write_byte(0)
		hb_writer.close()
		return ""

	for value in frequency.list:
		if value is not 0:
			counter = counter + 1
	hb_writer.write_byte(counter)

	for i in range(len(frequency.list)):
		if frequency.list[i] is not 0:
			hb_writer.write_byte(i)
			hb_writer.write_byte(frequency.list[i])

	f = open(input, 'r')
	for line in f:
		for x in line:
			string = string + str(code.list[ord(x)])
	hb_writer.write_code(string)
	hb_writer.close()

	return traverse(tree)

# Opens the input file using HuffmanBitsReader and read the header information (# of codes, list of occurances)
# Builds a HuffmanTree from the number of codes and the list of occurences
# Decopes the compressed data, reading bit by bit from the file and writing to the output
def huffman_decode(input, output):
	hb_reader = HuffmanBitsReader(input)
	num_codes = hb_reader.read_byte()
	num_chars = 0
	string = ""
	arr_list = array_list.List([0] * 256, 256)

	if (num_codes is 0):
		open(output, 'wb').close()
		hb_reader.close()
	else: 
		for i in range(num_codes):
			value = hb_reader.read_byte()
			num_occurences = hb_reader.read_int()
			num_chars += num_occurences
			arr_list = array_list.set(arr_list, value, num_occurences)
		tree = build_tree(arr_list)
		code = characterCode(tree, arr_list)
		file = open(output, 'w')

		for i in range(num_chars):
			x, hb_reader = check_leaf(tree, hb_reader)
			string = string + x

		hb_reader.close()
		file.write(str(string))
		file.close()

class TestCases(unittest.TestCase):
    def test_repr(self):
        leaf = Leaf(1, 2)
        leaf2 = Leaf(1, 3)
        node = HuffmanNode(2, 2, leaf, leaf2)
        self.assertEqual(leaf.__repr__(), "Leaf(1, 2)")
        self.assertEqual(leaf2.__repr__(), "Leaf(1, 3)")
        self.assertEqual(node.__repr__(), "HuffmanNode(2, 2, Leaf(1, 2), Leaf(1, 3))")

    def test_eq(self):
        tree = HuffmanNode("z", 10, None, None)
        tree2 = HuffmanNode("z", 10, None, None)
        self.assertEqual(tree, tree2)

    def test_comes_before(self):
        leaf = Leaf(1, 4)
        leaf2 = Leaf(3, 4)
        self.assertTrue(comes_before(leaf, leaf2))
        leaf3 = Leaf(3, 5)
        leaf4 = Leaf(1, 1)
        self.assertFalse(comes_before(leaf3, leaf4))
        charLeaf = Leaf("a", "b")
        charLeaf2 = Leaf("c", "d")
        self.assertTrue(comes_before(charLeaf, charLeaf2))

    def test_count_occurances(self):
        self.assertEqual(count_occurances("char.txt"), array_list.List([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 256))

    def test_build_tree(self):
        countlist = count_occurances("char.txt")
        self.assertEqual(build_tree(countlist), HuffmanNode(32, 13, HuffmanNode(32, 6, Leaf(32, 3), Leaf(98, 3)), HuffmanNode(97, 7, HuffmanNode(99, 3, Leaf(100, 1), Leaf(99, 2)), Leaf(97, 4))))

    def test_traverse(self):
        countlist = count_occurances("char.txt")
        tree = build_tree(countlist)
        self.assertEqual(traverse(tree), " bdca")

    def test_characterCode(self):
        countlist = count_occurances("char.txt")
        tree = build_tree(countlist)
        codes = characterCode(tree, arr_list)
        self.assertEqual(codes, array_list.List([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '11', '01', '101', '100', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 256))

    def test_huffman_encode(self):
        string = huffman_encode("char.txt", "output.bin")
        self.assertEqual(string, " bdca")

    def test_huffman_decode(self):
        string = huffman_decode("output.bin", "decoded_output.txt")
        self.assertEqual(string, None)

if __name__ == '__main__':
    unittest.main()