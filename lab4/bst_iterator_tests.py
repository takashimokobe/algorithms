import unittest
from bst import *

def f(x,y):
    return x < y

class TestCases(unittest.TestCase):
    global bst
    bst = BinarySearchTree(f, BSTNode(12, BSTNode(7, BSTNode(2, None, None),
                                               BSTNode(10, BSTNode(9, None, None), BSTNode(11, None, None))),
                                       BSTNode(23, BSTNode(16, None, BSTNode(20, None, None)), BSTNode(100, None, None))))

    def test_prefix_iterator(self):
        test_pre = prefix_iterator(bst)
        self.assertEqual(next(test_pre), 12)
        self.assertEqual(next(test_pre), 7)
        self.assertEqual(next(test_pre), 2)
        self.assertEqual(next(test_pre), 10)
        self.assertEqual(next(test_pre), 9)
        self.assertEqual(next(test_pre), 11)
        self.assertEqual(next(test_pre), 23)
        self.assertEqual(next(test_pre), 16)
        self.assertEqual(next(test_pre), 20)
        self.assertEqual(next(test_pre), 100)

    def test_infix_iterator(self):
        test_in = infix_iterator(bst)
        self.assertEqual(next(test_in), 2)
        self.assertEqual(next(test_in), 7)
        self.assertEqual(next(test_in), 9)
        self.assertEqual(next(test_in), 10)
        self.assertEqual(next(test_in), 11)
        self.assertEqual(next(test_in), 12)
        self.assertEqual(next(test_in), 16)
        self.assertEqual(next(test_in), 20)
        self.assertEqual(next(test_in), 23)
        self.assertEqual(next(test_in), 100)

    def test_postfix_iterator(self):
        test_post = postfix_iterator(bst)
        self.assertEqual(next(test_post), 100)
        self.assertEqual(next(test_post), 20)
        self.assertEqual(next(test_post), 16)
        self.assertEqual(next(test_post), 23)
        self.assertEqual(next(test_post), 11)
        self.assertEqual(next(test_post), 9)
        self.assertEqual(next(test_post), 10)
        self.assertEqual(next(test_post), 2)
        self.assertEqual(next(test_post), 7)
        self.assertEqual(next(test_post), 12)

if __name__ == '__main__':
    unittest.main()
