#!/usr/bin/python3
"""
Unittesting for module models/rectangle.py
"""
import io
import sys
import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class TestDocstrings(unittest.TestCase):
    """Test code documentation"""

    def test_module_docstrings(self):
        self.assertTrue(len(Square.__module__.__doc__) > 0)

    def test_square_class_docstrings(self):
        self.assertTrue(len(Square.__doc__) > 0)

    def test_square_class_methods_docstrings(self):
        self.assertTrue(len(Square.__init__.__doc__) > 0)
        self.assertTrue(len(Square.__str__.__doc__) > 0)


class TestSquareBaseClass(unittest.TestCase):
    """Test class inheritance behavior"""

    def setUp(self):
        self.sq = Square(5)

    def test_inheritance_from_base_cls(self):
        self.assertTrue(issubclass(type(self.sq), Base))

    def test_inheritance_from_rectangle_cls(self):
        self.assertTrue(issubclass(type(self.sq), Rectangle))

    def test_is_base(self):
        self.assertIsInstance(self.sq, Base)

    def test_is_rectangle(self):
        self.assertIsInstance(self.sq, Square)



class TestSquareInstantiantion(unittest.TestCase):
    """Test obj creation behavior"""

    def setUp(self):
        Square._Base__nb_objects = 0

    def test_init_with_no_id(self):
        sq = Square(size=1)
        self.assertEqual(sq.id, 1)

    def test_init_with_id(self):
        sq = Square(id=99, size=1)
        self.assertEqual(sq.id, 99)

    def test_init_with_no_args(self):
        with self.assertRaises(TypeError):
            sq = Square()

    def test_one_arg(self):
        sq_1 = Square(10)
        sq_2 = Square(11)
        self.assertEqual(sq_1.id, sq_2.id - 1)

    def test_two_args(self):
        sq_1 = Square(10, 2)
        sq_2 = Square(2, 10)
        self.assertEqual(sq_1.id, sq_2.id - 1)

    def test_three_args(self):
        sq_1 = Square(10, 2, 2)
        sq_2 = Square(2, 2, 10)
        self.assertEqual(sq_1.id, sq_2.id - 1)

    def test_four_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)


class TestSquareAttrsAccess(unittest.TestCase):
    
    # def test_size_getter(self):
    #     self.assertEqual(5, Square(5, 2, 3, 9).size)

    # def test_size_setter(self):
    #     sq = Square(4, 1, 9, 2)
    #     sq.size = 8
    #     self.assertEqual(8, sq.size)

    # def test_width_getter(self):
    #     sq = Square(4, 1, 9, 2)
    #     sq.size = 8
    #     self.assertEqual(8, sq.width)

    # def test_height_getter(self):
    #     sq = Square(4, 1, 9, 2)
    #     sq.size = 8
    #     self.assertEqual(8, sq.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)



class TestInheritAttrsAndMethod(unittest.TestCase):
    """Test for methods and attrs"""
    @staticmethod
    def capture_stdout(square, method):
        """Captures and returns text printed to stdout.
        Args:
            square (Square): The Square to print to stdout.
            method (str): The method to run on square.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(square)
        else:
            square.display()
        sys.stdout = sys.__stdout__
        return capture

    def setUp(self):
        self.sq = Square(5)

    def test_area(self):
        self.assertEqual(self.sq.area(), 25)

    def test_display_width_height(self):
        rect_1 = Square(2)
        capture = TestInheritAttrsAndMethod.capture_stdout(rect_1, "display")
        self.assertEqual("##\n##\n", capture.getvalue())

