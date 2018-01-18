import unittest
from linked_stack import *


class TestStack(unittest.TestCase):

    def test00_interface(self):
        test_stack = empty_stack()
        test_stack = push(test_stack, "foo")
        peek(test_stack)
        _, test_stack = pop(test_stack)
        size(test_stack)
        is_empty(test_stack)

    def test_empty(self):
        self.assertEqual(empty_stack(), None)

    def test_push(self):
        self.assertEqual(push(empty_stack(), 5), Pair(5, None))

    def test_pop(self):
        stack1 = empty_stack()
        update_stack = push(stack1, 5)
        update_stack2 = push(update_stack, 1)
        self.assertEqual(pop(update_stack2), (1, Pair(5, None)))

    def test_pop_error(self):
        stack1 = empty_stack()
        self.assertRaises(IndexError, pop, stack1)

    def test_peek(self):
        stack1 = empty_stack()
        update_stack = push(stack1, 5)
        update_stack2 = push(update_stack, 1)
        self.assertEqual(peek(update_stack2), 1)

    def test_peek_error(self):
        stk1 = empty_stack()
        self.assertRaises(IndexError, peek, stk1)

    def test_size(self):
        stack1 = empty_stack()
        stack2 = push(stack1, 4)
        stack3 = push(stack2, 3)
        self.assertEqual(size(stack3), 2)

    def test_is_empty(self):
        self.assertEqual(is_empty(empty_stack()), True)


if __name__ == "__main__":
    unittest.main()
