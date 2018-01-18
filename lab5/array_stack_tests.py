import unittest
from array_stack import *

class TestCases(unittest.TestCase):
    def test00_interface(self):
        test_stack = empty_stack()
        test_stack = push(test_stack, "foo")
        peek(test_stack)
        _, test_stack = pop(test_stack)
        size(test_stack)
        is_empty(test_stack)

    def test_empty(self):
        self.assertEqual(empty_stack(), List([], 0))

    def test_push(self):
        stk1 = empty_stack()
        stk2 = push(stk1, 2)
        self.assertEqual(push(stk2, 3), List([2, 3], 2))

    def test_pop(self):
        stk1 = empty_stack()
        stk2 = push(stk1, 3)
        stk3 = push(stk2, 2)
        self.assertEqual(pop(stk3), (2, List([3], 1)))

    def test_pop_error(self):
        stk1 = empty_stack()
        self.assertRaises(IndexError, pop, stk1)

    def test_peek(self):
        stk1 = empty_stack()
        stk2 = push(stk1, 2)
        stk3 = push(stk1, 79)
        self.assertEqual(peek(stk3), 79)

    def test_peek_error(self):
        stk1 = empty_stack()
        self.assertRaises(IndexError, peek, stk1)

    def test_size(self):
        stk1 = push(empty_stack(), 3)
        self.assertEqual(size(stk1), 1)

    def test_is_empty(self):
        stk1 = empty_stack()
        stk2 = push(stk1, 2)
        self.assertFalse(is_empty(stk2))

if __name__=='__main__':
    unittest.main()
