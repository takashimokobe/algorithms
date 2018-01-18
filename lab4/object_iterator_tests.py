import unittest
from linked_list import *

class TestCases(unittest.TestCase):
    global lst
    lst = Pair(1, Pair(2, Pair(3, None)))

    def test_object_iterator(self):
        self.assertEqual(object_iterator(lst), Iterator(lst))

    def test_has_next_true(self):
        self.assertEqual(has_next(Iterator(lst)), True)

    def test_has_next_false(self):
        self.assertEqual(has_next(Iterator(None)), False)

    def test_next_empty(self):
        self.assertRaises(StopIteration, next, Iterator(None))

    def test_next_valid(self):
        self.assertEqual(next(Iterator(lst)), 1)

if __name__ == "__main__":
    unittest.main()
