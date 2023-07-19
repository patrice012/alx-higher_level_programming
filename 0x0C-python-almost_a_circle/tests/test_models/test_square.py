#!/usr/bin/python3
"""
Unittesting for module models/Square.py
"""
import io
import sys
import unittest
from models.square import Square
from models.base import Base


class TestDocstrings(unittest.TestCase):
    """Test code documentation"""

    def test_module_docstrings(self):
        self.assertTrue(len(Square.__module__.__doc__) > 0)

    def test_square_class_docstrings(self):
        self.assertTrue(len(Square.__doc__) > 0)

    def test_square_class_methods___init__docstrings(self):
        self.assertTrue(len(Square.__init__.__doc__) > 0)

    def test_square_class_methods___str__docstrings(self):
        self.assertTrue(len(Square.__str__.__doc__) > 0)

    def test_square_class_methods__update__docstrings(self):
        self.assertTrue(len(Square.update.__doc__) > 0)

    def test_square_class_methods__to_dictionary__docstrings(self):
        self.assertTrue(len(Square.to_dictionary.__doc__) > 0)

    def test_square_class_methods__size__docstrings(self):
        self.assertTrue(len(Square.size.__doc__) > 0)


class TestSquareBaseClass(unittest.TestCase):
    """Test class inheritance behavior"""

    def setUp(self):
        self.sq = Square(5)

    def test_inherit_from_base_cls(self):
        self.assertTrue(issubclass(type(self.sq), Base))

    def test_inherit_from_rectangle_cls(self):
        self.assertTrue(issubclass(type(self.sq), Square))

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
        self.assertTrue(sq.id > 0)

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
    
    def test_size_getter(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        sq = Square(4, 1, 9, 2)
        sq.size = 8
        self.assertEqual(8, sq.size)

    def test_width_getter(self):
        sq = Square(4, 1, 9, 2)
        sq.size = 8
        self.assertEqual(8, sq.width)

    def test_height_getter(self):
        sq = Square(4, 1, 9, 2)
        sq.size = 8
        self.assertEqual(8, sq.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)


class TestAttrsExecptions(unittest.TestCase):

    def setUp(self):
        self.sq = Square(1)

    def test_invalid_size_value(self):
        with self.assertRaises(TypeError, msg='width must be an integer'):
            self.sq.size = 5.55
            self.sq.size = 'hello'

    def test_invalid_size_type(self):
        with self.assertRaises(ValueError, msg='width must be > 0'):
            self.sq.size = -5

    def test_invalid_x_value(self):
        with self.assertRaises(TypeError, msg='x must be an integer'):
            self.sq.x = 5.55
            self.sq.x = 'hello'

    def test_invalid_x_type(self):
        with self.assertRaises(ValueError, msg='x must be >= 0'):
            self.sq.x = -5

    def test_invalid_y_value(self):
        with self.assertRaises(TypeError, msg='y must be an integer'):
            self.sq.y = 5.55
            self.sq.y = 'hello'

    def test_invalid_y_type(self):
        with self.assertRaises(ValueError, msg='y must be >= 0'):
            self.sq.y = -5


class TestInheritAttrsAndMethod(unittest.TestCase):
    """Test for methods and attrs"""
    @staticmethod
    def capture_stdout(Square, method):
        """Captures and returns text printed to stdout.
        Args:
            Square (Square): The Square to print to stdout.
            method (str): The method to run on Square.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(Square)
        else:
            Square.display()
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


class TestDictMethod(unittest.TestCase):
    """Test instance method"""
    def test_to_dictionary_method(self):
        Square._Base__nb_objects = 0
        sq = Square(10, 2, 1)
        output = {'id': sq.id, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(sq.to_dictionary(), output)

    def test_to_dictionary_no_object_changes(self):
        sq_1 = Square(10, 2, 1, 2)
        sq_2 = Square(1, 2, 10)
        sq_1.update(**sq_1.to_dictionary())
        self.assertNotEqual(sq_1, sq_2)

    def test_to_dictionary_arg(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            sq.to_dictionary(1)


class TestSquareUpdate(unittest.TestCase):

    def test_update_kwargs_three(self):
        rect_1 = Square(10, 5, 8)
        rect_1.id = 89
        self.assertEqual("[Square] (89) 5/8 - 10", str(rect_1))

    def test_update_kwargs_four(self):
        rect_1 = Square(8)
        rect_1.update(id=2, x=1, y=3, size=4)
        self.assertEqual("[Square] (2) 1/3 - 4", str(rect_1))

    def test_update_kwargs_two(self):
        Square._Base__nb_objects = 0
        rect_1 = Square(2)
        rect_1.update(y=5, x=8)
        self.assertEqual("[Square] ({}) 8/5 - 2".format(rect_1.id), str(rect_1))

    def test_update_args_width_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.width)

    def test_update_args_height_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.height)

    def test_update_args_zero(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_args_one(self):
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))

    def test_update_args_two(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_args_three(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))


if __name__ == "__main__":
    unittest.main()
