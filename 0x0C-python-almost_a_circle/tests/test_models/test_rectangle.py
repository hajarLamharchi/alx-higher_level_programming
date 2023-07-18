""" This module tests the use cases of the class rectangle """
import unittest
from models.rectangle import Rectangle
from models.base import Base


class testRectangle(unittest.TestCase):
    """ Defines test cases of rectangle """
    def setUp(self):
        """ resets the __nb-object attribute before test """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ cleans up any resources"""
        pass

    def test_height_width_value(self):
        """ tests when only the width and height are given """
        r1 = Rectangle(7, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(19, 10)
        self.assertEqual(r2.id, 2)

    def test_with_all_values(self):
        r = Rectangle(28, 11, 0, 0, 3)
        self.assertEqual(r.id, 3)


class testRectangleRaises(unittest.TestCase):
    """ Tests the exception raises """
    def test_width_raises(self):
        """ Tests the width exceptions """
        with self.assertRaises(TypeError):
            Rectangle("a", 5)
            Rectangle(None, 7)
            Rectangle([1, 2, 3], 5)
            Rectangle((1, 2), 7)
            Rectangle({"a", "b"}, 3)
        with self.assertRaises(ValueError):
            Rectangle(-2, 5)
            Rectangle(0, 5)

    def test_height_raises(self):
        """ Tests the height exceptions """
        with self.assertRaises(TypeError):
            Rectangle(5, "a")
            Rectangle(7, None)
            Rectangle(2, [1, 2, 3])
            Rectangle(8, (1, 2))
            Rectangle(1, {"a", "b"})
            Rectangle("b", "a")
            Rectangle([1, 2], [1, 2, 3])
            Rectangle((3, 4), (1, 2))
        with self.assertRaises(ValueError):
            Rectangle(2, -5)
            Rectangle(1, 0)
            Rectangle(0, 0)
            Rectangle(-1, -2)

    def test_x_raises(self):
        """ Tests x exceptions """
        with self.assertRaises(TypeError):
            Rectangle(7, 2, "10", 5)
            Rectangle(7, 2, [1, 2], 5)
            Rectangle(7, 2, (1, 2), 5)
            Rectangle(7, 2, {1, 2}, 5)
            Rectangle(7, 2, None, 5)
            Rectangle("a", 5, "10", 5)
            Rectangle(5, "a", "10", 5)
        with self.assertRaises(ValueError):
            Rectangle(7, 2, -2, 5)
            Rectangle(-2, 5, -1, 3)
            Rectangle(2, -5, -3, 1)

    def test_y_raises(self):
         """ Tests x exceptions """
         with self.assertRaises(TypeError):
             Rectangle(7, 2, "10", 5)
             Rectangle(7, 2, 3, [1, 2])
             Rectangle(7, 2, 3, (1, 2))
             Rectangle(7, 2, 3, {1, 2})
             Rectangle(7, 2, 3, None)
             Rectangle("a", 5, 3, "10")
             Rectangle(5, "a", 3, "10")
             Rectangle(5, "a", "11", "10")
         with self.assertRaises(ValueError):
             Rectangle(7, 2, 2, -5)
             Rectangle(-2, 5, 1, -3)
             Rectangle(2, -5, -3, -1)
             Rectangle(-2, -5, -3, -1)

class testRectangleArea(unittest.TestCase):
    """ Tests the method area"""
    def test_area(self):
        """ tests the area """
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.area(), 2)

        r2 = Rectangle(10, 5, 0, 0, 5)
        self.assertEqual(r2.area(), 50)


class testRectangleUpdate(unittest.TestCase):
    """test the method update"""
    def test_update_id(self):
        """test update id"""
        r = Rectangle(1, 1, 1, 1)
        r.update(10)
        self.assertEqual(r.id, 10)

    def test_update_width(self):
        """test update width"""
        r = Rectangle(1, 1, 1, 1)
        r.update(10, 7)
        self.assertEqual(r.width, 7)

    def test_update_height(self):
        """test update height"""
        r = Rectangle(1, 1, 1, 1)
        r.update(10, 7, 2)
        self.assertEqual(r.height, 2)

    def test_update_x(self):
        """test update x"""
        r = Rectangle(1, 1, 1, 1)
        r.update(10, 7, 2, 9)
        self.assertEqual(r.x, 9)

    def test_update_y(self):
        """test update y"""
        r = Rectangle(1, 1, 1, 1)
        r.update(10, 7, 2, 9, 3)
        self.assertEqual(r.y, 3)



if __name__ == "__main__":
    unittest.main()
