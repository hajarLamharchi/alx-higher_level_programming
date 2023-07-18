""" Defines the class testBase """
import unittest
from models.base import Base


class testBase(unittest.TestCase):
    """ Defines the test cases for the class Base """
    def setUp(self):
        """ resets the __nb-object attribute before test """
    Base._Base__nb_objects = 0
    
    def tearDown(self):
        """ cleans up any resources"""
        pass
    
    def test_base_with_value(self):
        """ Tests the case with value """
        b = Base(7)
        self.assertEqual(b.id, 7)

    def test_base_with_no_value(self):
        """ Tests the case with no value """
        a = Base()
        b = Base()
        self.assertEqual(a.id, 1)
        self.assertEqual(b.id, 2)

if __name__ == "__main__":
    unittest.main()
