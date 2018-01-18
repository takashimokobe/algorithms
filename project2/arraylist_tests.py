import unittest
from arraylist import *

class TestCases(unittest.TestCase):
    def test_interface(self):
        t_list = empty_list()
        t_list = add(t_list, 0, "Kappa")
        get(t_list, 0)
        t_list = set(t_list, 0, "Okay")
        remove(t_list, 0)

    def test_repr(self):
        mylist = List([1, 2, 3, 4], 4)
        self.assertEqual(repr(mylist), "List([1, 2, 3, 4], 4)")

    def test_empty(self):
        self.assertEqual(empty_list(), List([], 0))

    def test_add(self):
        mylist = List([1, 2, 3, 4], 4)
        self.assertEqual(add(mylist, 0, "hello"), List(["hello", 1, 2, 3, 4], 5))

    def test_add2(self):
        lst = List(["Okay", "Sure"], 2)
        self.assertEqual(add(lst, 2, "where"), List(["Okay", "Sure", "where"], 3))

    def test_raise_add(self):
        erlist = List([1, 2, 3], 3)
        self.assertRaises(IndexError, add, erlist, -2, 4)

    def test_length(self):
        mylist = List(["kappa", 23, "WHERE", 30], 4)
        self.assertEqual(length(mylist), 4)

    def test_length2(self):
        mylist = List([], 0)
        self.assertEqual(length(mylist), 0)

    def test_get(self):
        mylist = List(["What", "is", "going", "one"], 4)
        self.assertEqual(get(mylist, 2), "going")

    def test_er_get(self):
        mylist = List ([1, 4222, "okay"], 3)
        self.assertRaises(IndexError, get, mylist, 200)

    def test_set(self):
        mylist = List([1, 2, 3, "HUHH"], 4)
        self.assertEqual(set(mylist, 3, "OKAY"), List([1, 2, 3, "OKAY"], 4))

    def test_er_set(self):
        mylist = List ([1, 2, 3, 4, 5], 5)
        self.assertRaises(IndexError, set, mylist, -2, 5)

    def test_remove(self):
        mylist = List (["Okay", "where", "is", "the", "pizza"], 5)
        self.assertEqual(remove(mylist, 2), ("is", List(["Okay", "where", "the", "pizza"], 4)))

    def test_removelast(self):
        mylist = List([1, 2, 3, 4, 5, 5, 5], 7)
        self.assertEqual(remove(mylist, 6), (5, List([1, 2, 3, 4, 5, 5], 6)))

    def test_removefirst(self):
        mylist = List([1, 2, 3, 4], 4)
        self.assertEqual(remove(mylist, 0), (1, List([2, 3, 4], 3)))

    def test_er_remove(self):
        mylist = List([1, 2, 3, 4], 4)
        self.assertRaises(IndexError, remove, mylist, 10)


if __name__ == '__main__':
    unittest.main()