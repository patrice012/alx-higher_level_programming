#!/usr/bin/python3
"""
Unittesting for module models/rectangle.py
"""
import io
import sys
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestBaseClassDocstrings(unittest.TestCase):

    def test_docstrings(self):
        """Test for  docs"""
        self.assertTrue(len(Rectangle.__doc__) > 0)
        self.assertTrue(len(Rectangle.__module__.__doc__) > 0)


class TestRectangeBaseClass(unittest.TestCase):
    """Test class inheritance behavior"""

    def setUp(self):
        self.rect_1 = Rectangle(10, 20, 5, 8)
        Base.__nb_objects = 0

    def test_inheritance_from_rectangle_cls(self):
        self.assertTrue(issubclass(type(self.rect_1), Base))

    def test_is_base(self):
        self.assertIsInstance(self.rect_1, Base)

    def test_is_rectangle(self):
        self.assertIsInstance(self.rect_1, Rectangle)


class TestRectangleAttrs(unittest.TestCase):
    """Unittests for testing Rectangle class attributs access."""

    def  setUp(self):
        Base.__nb_objects = 0
        self.rect_1 = Rectangle(10, 20, 5, 8)


    def test_private_attrs_width(self):
        with self.assertRaises(AttributeError):
            self.assertTrue(Rectangle.__width)

    def test_private_attrs_height(self):
        with self.assertRaises(AttributeError):
            self.assertTrue(Rectangle.__height)

    def test_private_attrs_x(self):
        with self.assertRaises(AttributeError):
            self.assertTrue(Rectangle.__x)

    def test_private_attrs_y(self):
        with self.assertRaises(AttributeError):
            self.assertTrue(Rectangle.__y)


class TestRectangleAttributsAccess(unittest.TestCase):
    """Unittests for testing the Rectangle class getters and setters."""

    def  setUp(self):
        self.rect_1 = Rectangle(10, 20, 5, 8)
        Base.__nb_objects = 0

    def test_width_getter(self):
        self.assertEqual(self.rect_1.width, 10)

    def test_height_getter(self):
        self.assertEqual(self.rect_1.height, 20)

    def test_x_getter(self):
        self.assertEqual(self.rect_1.x, 5)

    def test_y_getter(self):
        self.assertEqual(self.rect_1.y, 8)

    #Test all setters...........
    def test_width_setter(self):
        self.rect_1.width = 14
        self.assertEqual(self.rect_1.width, 14)

    def test_height_setter(self):
        self.rect_1.height = 55
        self.assertEqual(self.rect_1.height, 55)

    def test_x_setter(self):
        self.rect_1.x = 14
        self.assertEqual(self.rect_1.x, 14)

    def test_y_setter(self):
        self.rect_1.y = 10
        self.assertEqual(self.rect_1.y, 10)

    # test assertRaises exception
    def test_invalid_width_value(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            self.rect_1.width = 5.55

    def test_invalid_width_type(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            self.rect_1.width = 'test'

    def test_invalid_width_value_2(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            self.rect_1.width = -5
            self.rect_1.width = 0

    def test_invalid_height_type(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            self.rect_1.height = ['test', 55]
            self.rect_1.height = {'h':44}

    def test_invalid_height_value(self):
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            self.rect_1.height = 0
            self.rect_1.height = -11

    def test_invalid_x_type(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            self.rect_1.x = 'hello'
            self.rect_1.x = 1, 8

    def test_invalid_x_value(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            self.rect_1.x = -1

    def test_invalid_y_type(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            self.rect_1.y = 5.44
            self.rect_1.y = {'h':0}

    def test_invalid_y_value(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            self.rect_1.y = -11


class TestRectangleInstantiation(unittest.TestCase):
    """Unittests for testing the Rectangle class instantiation."""

    def setUp(self):
        Base.__nb_objects = 0

    def test_init_with_no_id(self):
        Base.__nb_objects = 0
        rect_1  = Rectangle(12, 55)
        self.assertEqual(rect_1.id, 63)

    def test_init_with_id_calling_super(self):
        # Base.__nb_objects = 0
        rect_1 = Rectangle(18, 99, id=14)
        self.assertEqual(rect_1.id, 14)

    def test_object_instantiation_width_invalid_value(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            rect_2 = Rectangle(-2, 5)

    def test_object_instantiation_height_invalid_value(self):
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            rect_2 = Rectangle(2, -5)

    def test_object_instantiation_x_invalid_value(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            rect_2 = Rectangle(2, 5, x=-5)

    def test_object_instantiation_y_invalid_value(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            rect_2 = Rectangle(2, 5, y=-5)

    def test_object_instantiation_width_invalid_type(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            rect_2 = Rectangle('55', 5)
            rect_2 = Rectangle(55.4, 5)

    def test_object_instantiation_height_invalid_type(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            rect_2 = Rectangle(2, '88')
            rect_2 = Rectangle(2, [])

    def test_object_instantiation_x_invalid_type(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            rect_2 = Rectangle(2, 5, x='5')
            rect_2 = Rectangle(2, 5, x=885.1)

    def test_object_instantiation_y_invalid_type(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            rect_2 = Rectangle(2, 5, y='9')
            rect_2 = Rectangle(2, 5, y={})



class TestRectangle_area(unittest.TestCase):
    """Unittests for testing the area method of the Rectangle class."""

    def setUp(self):
        Base.__nb_objects = 0

    def test_area_method(self):
        rect_1 = Rectangle(2, 4)
        self.assertEqual(rect_1.area(), 8)

    def test_area_small(self):
        rect_1 = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, rect_1.area())

    def test_area_large(self):
        rect_1 = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, rect_1.area())

    def test_area_changed_attributes(self):
        rect_1 = Rectangle(2, 10, 1, 1, 1)
        rect_1.width = 7
        rect_1.height = 14
        self.assertEqual(98, rect_1.area())

    def test_area_one_arg(self):
        rect_1 = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            rect_1.area(1)


class TestStrMethod:

    def test___str__output(self):
        rect_2 = Rectangle(10, 20, x=2, y=3, id=1)
        output = '[Rectangle] (1) 2/3 - 10/20'
        self.assertEqual(str(rect_2), output)


class TestRectangle_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Rectangle class."""

    def setUp(self):
        Base.__nb_objects = 0

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.
        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    # Test __str__ method
    def test_str_method_print_width_height(self):
        rect_1 = Rectangle(4, 6)
        capture = TestRectangle_stdout.capture_stdout(rect_1, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(rect_1.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        rect_1 = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(rect_1.id)
        self.assertEqual(correct, rect_1.__str__())

    def test_str_method_width_height_x_y(self):
        rect_1 = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(rect_1.id)
        self.assertEqual(correct, str(rect_1))

    def test_str_method_width_height_x_y_id(self):
        rect_1 = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(rect_1))

    def test_str_method_changed_attributes(self):
        rect_1 = Rectangle(7, 7, 0, 0, [4])
        rect_1.width = 15
        rect_1.height = 1
        rect_1.x = 8
        rect_1.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(rect_1))

    def test_str_method_one_arg(self):
        rect_1 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rect_1.__str__(1)

    # Test display method
    def test_display_width_height(self):
        rect_1 = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(rect_1, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        rect_1 = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangle_stdout.capture_stdout(rect_1, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_y(self):
        rect_1 = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangle_stdout.capture_stdout(rect_1, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        rect_1 = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangle_stdout.capture_stdout(rect_1, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        rect_2 = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            rect_2.display(1)


class TestRectangle_update_args(unittest.TestCase):
    """Unittests for testing update args method of the Rectangle class."""

    def tearDown(self):
        Base.__nb_objects = 0

    # Test args
    def test_update_args_zero(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        rect_1.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(rect_1))

    def test_update_args_one(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        rect_1.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(rect_1))

    def test_update_args_two(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        rect_1.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(rect_1))

    def test_update_args_three(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        rect_1.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(rect_1))

    def test_update_args_four(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        rect_1.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(rect_1))

    def test_update_args_five(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        rect_1.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(rect_1))

    def test_update_args_more_than_five(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        rect_1.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(rect_1))

    def test_update_args_None_id(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        rect_1.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(rect_1.id)
        self.assertEqual(correct, str(rect_1))

    def test_update_args_None_id_and_more(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        rect_1.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/10 - 4/5".format(rect_1.id)
        self.assertEqual(correct, str(rect_1))

    def test_update_args_twice(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        rect_1.update(89, 2, 3, 4, 5, 6)
        rect_1.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(rect_1))

    def test_update_args_invalid_width_type(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect_1.update(89, "invalid")

    def test_update_args_width_zero(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect_1.update(89, 0)

    def test_update_args_width_negative(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect_1.update(89, -5)

    def test_update_args_invalid_height_type(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect_1.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect_1.update(89, 1, 0)

    def test_update_args_height_negative(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect_1.update(89, 1, -5)

    def test_update_args_invalid_x_type(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect_1.update(89, 2, 3, "invalid")

    def test_update_args_x_negative(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect_1.update(89, 1, 2, -6)

    def test_update_args_invalid_y(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect_1.update(89, 2, 3, 4, "invalid")

    def test_update_args_y_negative(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect_1.update(89, 1, 2, 3, -6)

    def test_update_args_width_before_height(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect_1.update(89, "invalid", "invalid")

    def test_update_args_width_before_x(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect_1.update(89, "invalid", 1, "invalid")

    def test_update_args_width_before_y(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect_1.update(89, "invalid", 1, 2, "invalid")

    def test_update_args_height_before_x(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect_1.update(89, 1, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect_1.update(89, 1, "invalid", 1, "invalid")

    def test_update_args_x_before_y(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect_1.update(89, 1, 2, "invalid", "invalid")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Rectangle class."""

    def tearDown(self):
        Base.__nb_objects = 0

    def test_update_kwargs_one(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        rect_1.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(rect_1))

    def test_update_kwargs_two(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        rect_1.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(rect_1))

    def test_update_kwargs_three(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        rect_1.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(rect_1))

    def test_update_kwargs_four(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        rect_1.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(rect_1))

    def test_update_kwargs_five(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        rect_1.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(rect_1))

    def test_update_kwargs_None_id(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        rect_1.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(rect_1.id)
        self.assertEqual(correct, str(rect_1))

    def test_update_kwargs_None_id_and_more(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        rect_1.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(rect_1.id)
        self.assertEqual(correct, str(rect_1))

    def test_update_kwargs_twice(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        rect_1.update(id=89, x=1, height=2)
        rect_1.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(rect_1))

    def test_update_kwargs_invalid_width_type(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect_1.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect_1.update(width=0)

    def test_update_kwargs_width_negative(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect_1.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect_1.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect_1.update(height=0)

    def test_update_kwargs_height_negative(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect_1.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect_1.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect_1.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect_1.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect_1.update(y=-5)

    def test_update_args_and_kwargs(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        rect_1.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(rect_1))

    def test_update_kwargs_wrong_keys(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        rect_1.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(rect_1))

    def test_update_kwargs_some_wrong_keys(self):
        rect_1 = Rectangle(10, 10, 10, 10, 10)
        rect_1.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(rect_1))




class TestDictMethod(unittest.TestCase):
    """Test instance method"""
    def test_to_dictionary_method(self):
        Rectangle._Base__nb_objects = 0
        rect = Rectangle(10, 2, 1, 9)
        output = {'x': 1, 'y': 9, 'id': 38, 'height': 2, 'width': 10}
        self.assertEqual(rect.to_dictionary(), output)
