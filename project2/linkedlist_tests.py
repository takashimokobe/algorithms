import unittest
from linkedlist import *

class TestCases(unittest.TestCase):
    def test_interface(self):
        t_list = empty_list()
        t_list = add(t_list, 0, "Okay")
        get(t_list, 0)
        t_list = set(t_list, 0, "Where")
        remove(t_list, 0)

    def test_empty_list(self):
        self.assertEqual(empty_list(), None)

    def test__add(self):
        mylist = Pair(5, Pair(3, None))
        self.assertEqual(add(mylist, 1, 2), Pair(5, Pair(2, Pair(3, None))))

    def test_add2(self):
        mylist = Pair(4, Pair(20, Pair("hello", Pair("kappa", None))))
        self.assertEqual(add(mylist, 2, "okay"), Pair(4, Pair(20, Pair("okay", Pair("hello", Pair("kappa", None))))))

    def test_index_add(self):
        mylist = Pair("Hello", Pair(2, None))
        self.assertRaises(IndexError, add, mylist, -2, 4)

    def test_length(self):
        mylist = Pair("Hello", Pair(12, Pair("where", Pair(59, None))))
        self.assertEqual(length(mylist), 4)

    def test_0_length(self):
        mtlist = None
        self.assertEqual(length(mtlist), 0)

    def test_get(self):
        mylist = Pair(1, Pair(2, None))
        self.assertEqual(get(mylist, 1), 2)

    def test_index_get(self):
        mylist = Pair(1, Pair(2, Pair(4, Pair("WHAT", Pair(10, None)))))
        self.assertRaises(IndexError, get, mylist, 20)

    def test_er_get(self):
        alist = Pair(1, Pair(2, Pair(20, None)))
        self.assertRaises(IndexError, get, alist, -20)

    def test_set(self):
        mylist = Pair(1, Pair(2, Pair(3, Pair("hello", None))))
        self.assertEqual(set(mylist, 2, 30), Pair(1, Pair(2, Pair(30, Pair("hello", None)))))

    def test_er_set(self):
        alist = Pair(1, Pair(2, Pair(3, None)))
        self.assertRaises(IndexError, set, alist, -20, 4)

    def test_removing(self):
        mylist = Pair(1, Pair(2, Pair(3, None)))
        self.assertEqual(removing(mylist, 1), Pair(1, Pair(3, None)))

    def test_er_removing(self):
        errortest = Pair(1, Pair(3, Pair("hello", None)))
        self.assertRaises(IndexError, removing, errortest, -10)

    def test_remove(self):
        mylist = Pair(1, Pair(20, Pair("65", None)))
        self.assertEqual(remove(mylist, 1), (20, Pair(1, Pair("65", None))))

    def test_er_remove(self):
        erlist = Pair(20, Pair("where", Pair(20, None)))
        self.assertRaises(IndexError, remove, erlist, -10)

if __name__== '__main__':
    unittest.main()