import unittest
from array_list import *

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)

    def testrepr(self):

        arrayList = List([5, 10, 10, 1], 4)
        self.assertEqual(repr(arrayList), "List([5, 10, 10, 1], 4)")

    def testempty(self):
        self.assertEqual(empty_list(), List([], 0))

    def testadd1(self):
        lst = List([1,5,3], 3)
        self.assertEqual(add(lst, 0, 5), List([5, 1, 5, 3], 4))

    def test_add2(self):
        lst = List(['king','kong'], 2)
        self.assertEqual(add(lst, 2, 'godzilla'), List(['king', 'kong', 'godzilla'], 3))

    def testaddraise(self):
        with self.assertRaises(IndexError):
            lst = List([4, 2], 2)
            add(lst,3,3)
            

    def testlength(self):
        lst = List([111,111,1111], 3)
        self.assertEqual(length(lst), 3)

    def testget(self):
        lst = List(['cpe','103','505'], 3)
        self.assertEqual(get(lst, 0), "cpe")

    def testgeterror(self):
        lst = List([1,2,3,4,5,6], 6)
        self.assertRaises(IndexError, get, lst, 9)

    def testset(self):
        lst = List([5,10,30], 3)
        self.assertEqual(set(lst, 1, 7), List([5,7,30], 3))

    def testseterror(self):
        lst = List([1,2,3], 3)
        self.assertRaises(IndexError, set, lst, 4, 5)

    def testremove(self):
        lst= List([5,5,5,5], 4)
        self.assertEqual(remove(lst, 1), (5, List([5,5,5], 3)))

    def testremoveend(self):
        lst = List([5,10,100], 3)
        self.assertEqual(remove(lst, 2), (100, List([5,10], 2)))

    def testremoveraise(self):
        with self.assertRaises(IndexError):
            lst = List([1,1,1,1],4)
            remove(lst,10)

if __name__ == '__main__':
    unittest.main()
