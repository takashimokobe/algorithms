import unittest
from postfix import *

class TestCases(unittest.TestCase):
    def test00_interface(self):
        postfix_calc("1 1 +")

    def test_postfix(self):
        op1 = "1 2 3 + * 4 *"
        self.assertAlmostEqual(postfix_calc(op1), 20)

    def test_postfix_sub_div(self):
        op2 = "1 5 / 2 -"
        self.assertEqual(postfix_calc(op2), -1.8)

if __name__=='__main__':
    unittest.main()
