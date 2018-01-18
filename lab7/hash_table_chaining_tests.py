from hash_table_chaining import *
import unittest

hashtable = HashTable()
hashtable.size = 2
hashtable.list = [[], [], [], [], [], [[5, 'apples']], [[6, 'carrot']], []]

hashtable2 = HashTable()
hashtable2.size = 1
hashtable2.list = [[], [], [], [], [], [], [[6, 'carrot']], []]

hashtable3 = HashTable()
hashtable3.size = 2
hashtable3.collisions = 1
hashtable3.list = [[], [], [], [], [], [[5, 'apples']], [[6, 'apples']], []]

hashtable4 = HashTable(1)
hashtable4.size = 2
hashtable4.val = 2
hashtable4.collisions = 0
hashtable4.list = [[[6, 'carrot']], [[5, 'apples']]]

hashtable5 = HashTable(1)
hashtable5.size = 4
hashtable5.val = 4
hashtable5.collisions = 1
hashtable5.list = [[[4, '2'], [100, '3']], [[5, '1']], [[6, 'fuck']], []]

class TestCases(unittest.TestCase):

	def test_repr(self):
		self.assertEqual(repr(hashtable), "HashTable([[], [], [], [], [], [[5, 'apples']], [[6, 'carrot']], []])")

	def test_empty(self):
		self.assertEqual(empty_hash_table(), HashTable())

	def test_insert(self):
		table = HashTable()
		table = insert(table, 5, 'apples')
		table = insert(table, 6, "carrot")
		self.assertEqual(table,hashtable)

	def test_insert_replace(self):
		table = HashTable()
		table = insert(table, 5, 'apples')
		table = insert(table, 6, "carrot")
		table = insert(table, 6,'apples')
		self.assertEqual(table, hashtable3)

	def test_insert_load_factor(self):
		table = HashTable(1)
		table = insert(table, 5, 'apples')
		table = insert(table, 6, "carrot")
		self.assertEqual(table,hashtable4)


	def test_insert_69(self):
		table = HashTable(1)
		table = insert(table,6,'fuck')
		table = insert(table,5,'1')
		table = insert(table,4,'2')
		table = insert(table,100,'3')
		self.assertEqual(table,hashtable5)


	def test_get(self):
		self.assertEqual(get(hashtable,5), 'apples')

	def test_get_2(self):
		with self.assertRaises(LookupError):
			get(hashtable,69)

	def test_insert_get(self):
		table = HashTable()
		insert(table,4,'cat')
		self.assertEqual(get(table,4), 'cat')


	def test_remove(self):
		table2 = HashTable()
		table2 = insert(table2, 5, 'apples')
		table2 = insert(table2, 6, "carrot")
		self.assertEqual(remove(table2,5), hashtable2)

	def test_raise_remove(self):
		with self.assertRaises(LookupError):
			remove(hashtable,4)

	def test_size(self):
		self.assertEqual(size(hashtable),2)

	def test_loadfactor(self):
		self.assertEqual(load_factor(hashtable), 2/8)

	def test_collisons(self):
		table = HashTable()
		table = insert(table, 5, 'apples')
		table = insert(table, 5, "carrot")

		self.assertEqual(collisions(table),1)


if __name__ == "__main__":
    unittest.main()