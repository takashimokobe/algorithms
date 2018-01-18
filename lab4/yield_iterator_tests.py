import unittest
from linked_list import Pair
from linked_list import yield_iterator


class TestCases(unittest.TestCase):
    def test_yield_iterator(self):
        lst = Pair(1, Pair(2, Pair(3, None)))
        test_yield = yield_iterator(lst)

        self.assertEqual(next(test_yield), 1)
        self.assertEqual(next(test_yield), 2)
        self.assertEqual(next(test_yield), 3)
        self.assertRaises(StopIteration, next, test_yield)


if __name__ == '__main__':
    unittest.main()
