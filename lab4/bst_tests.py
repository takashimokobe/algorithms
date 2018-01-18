import unittest
from bst import *


def f(x,y):
    return x < y


class TestCases(unittest.TestCase):
    global bst
    bst = BinarySearchTree(f, BSTNode(12, BSTNode(7, BSTNode(2, None, None),
                                               BSTNode(10, BSTNode(9, None, None), BSTNode(11, None, None))),
                                       BSTNode(23, BSTNode(16, None, BSTNode(20, None, None)), BSTNode(100, None, None))))

    def test_is_empty(self):
        self.assertEqual(is_empty(BinarySearchTree(f, None)), True)

    def test_insert(self):
        self.assertEqual(insert(bst, 32), BinarySearchTree(f, BSTNode(12, BSTNode(7, BSTNode(2, None, None), BSTNode(10, BSTNode(9, None, None), BSTNode(11, None, None))),
                                       BSTNode(23, BSTNode(16, None, BSTNode(20, None, None)), BSTNode(100, BSTNode(32, None, None), None)))))

    def test_lookup_yes(self):
        self.assertEqual(lookup(bst, 11), True)

    def test_lookup_no(self):
        self.assertEqual(lookup(bst, 35), False)

    def test_delete_invalid(self):
        self.assertEqual(delete(bst, 352), bst)

if __name__ == '__main__':
    unittest.main()
