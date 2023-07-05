#!/usr/bin/python3
""" Unittest for max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Tests the function max_integer """
    def test_max_integer(self):
        """ tests the edge cases of the function max_integer """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([0, 1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([-2, -1, 0, 1, 2]), 2)
        self.assertEqual(max_integer([4, 1, 1, 4]), 4)
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)
        self.assertEqual(max_integer([10]), 10)
        self.assertEqual(max_integer([999999, 1000000, 1999999, 2000000]), 2000000)
        self.assertEqual(max_integer([-9999, -100000, -19999, -20000]), -9999)
        self.assertEqual(max_integer([0, 1, 2, 1, 0]), 2)
