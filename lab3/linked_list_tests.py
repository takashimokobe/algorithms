import unittest
from linked_list import *


class TestCases(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(empty_list(), None)

    def test_add(self):
        mtList = None
        self.assertRaises(IndexError, add, mtList, 2, 4)
        largelist = Pair(0, Pair(1, Pair(3, Pair(2, Pair(4, Pair(8, Pair(10, None)))))))
        self.assertRaises(IndexError, get, largelist, -1, 5)
        smolList = Pair(3, Pair(1, None))
        self.assertRaises(IndexError, get, smolList, 20, 3)
        mylist = Pair(1, Pair(2, None))
        self.assertEqual(add(mylist, 0, 3), Pair(3, Pair(1, Pair(2, None))))

    def test_length(self):
        mtlist = None
        self.assertEqual(length(mtlist), 0)
        mylist = Pair(1, Pair(2, None))
        self.assertEqual(length(mylist), 2)

    def test_get(self):
        mtList = None
        self.assertRaises(IndexError, add, mtList, 2, 4)
        largelist = Pair(0, Pair(1, Pair(3, Pair(2, Pair(4, Pair(8, Pair(10, None)))))))
        self.assertRaises(IndexError, get, largelist, -1)
        smolList = Pair(3, Pair(1, None))
        self.assertRaises(IndexError, get, smolList, 20, 3)
        mylist = Pair(1, Pair(2, None))
        self.assertEqual(get(mylist, 0), 1)

    def test_set(self):
        mtList = None
        self.assertRaises(IndexError, add, mtList, 2, 4)
        largelist = Pair(0, Pair(1, Pair(3, Pair(2, Pair(4, Pair(8, Pair(10, None)))))))
        self.assertRaises(IndexError, get, largelist, -1)
        smolList = Pair(3, Pair(1, None))
        self.assertRaises(IndexError, get, smolList, 20, 3)
        mylist = Pair(1, Pair(2, None))
        self.assertEqual(set(mylist, 1, "hello"), Pair(1, Pair("hello", None)))

    def test_remove(self):
        mtList = None
        self.assertRaises(IndexError, add, mtList, 2, 4)
        largelist = Pair(0, Pair(1, Pair(3, Pair(2, Pair(4, Pair(8, Pair(10, None)))))))
        self.assertRaises(IndexError, get, largelist, -1)
        smolList = Pair(3, Pair(1, None))
        self.assertRaises(IndexError, get, smolList, 20, 3)
        mylist = Pair(1, Pair(2, None))
        self.assertEqual(remove(mylist, 1), Pair(1, None))


if __name__ == '__main__':
    unittest.main()