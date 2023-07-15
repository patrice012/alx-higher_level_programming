#!/usr/bin/python3
"""
Unittesting for module models/rectangle.py
"""
import unittest
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):

    def setUp(self):
        self.rect_1 = Rectangle(10, 20, 5, 8)
        # This is used to get the initial value state
        Rectangle._Base__nb_objects = 0


    def test_docstrings(self):
        """Test for  doc"""
        self.assertTrue(len(Rectangle.__doc__) > 0)
        self.assertTrue(len(Rectangle.__module__.__doc__) > 0)

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

    def test_init_with_no_id(self):
        rect_1  = Rectangle(12, 55)
        self.assertEqual(rect_1.id, 1)

    def test_init_with_id_calling_super(self):
        rect_1 = Rectangle(18, 99, id=14)
        self.assertEqual(rect_1.id, 14)


    # test all getters........

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
    def test_invalid_width_type(self):
        with self.assertRaises(TypeError):
            self.rect_1.width = 'test'
            self.rect_1.width = 5.55

    def test_invalid_width_value(self):
        with self.assertRaises(ValueError):
            self.rect_1.width = -5
            self.rect_1.width = 0

    def test_invalid_height_type(self):
        with self.assertRaises(TypeError):
            self.rect_1.height = ['test', 55]
            self.rect_1.height = {'h':44}

    def test_invalid_height_value(self):
        with self.assertRaises(ValueError):
            self.rect_1.height = 0
            self.rect_1.height = -11

    def test_invalid_x_type(self):
        with self.assertRaises(TypeError):
            self.rect_1.x = 'hello'
            self.rect_1.x = 1, 8

    def test_invalid_x_value(self):
        with self.assertRaises(ValueError):
            self.rect_1.x = -1

    def test_invalid_y_type(self):
        with self.assertRaises(TypeError):
            self.rect_1.y = 5.44
            self.rect_1.y = {'h':0}

    def test_invalid_y_value(self):
        with self.assertRaises(ValueError):
            self.rect_1.y = -11

    #Test init logic.........
    def test_object_instantiation_width_invalid_value(self):
        with self.assertRaises(ValueError):
            rect_2 = Rectangle(-2, 5)

    def test_object_instantiation_height_invalid_value(self):
        with self.assertRaises(ValueError):
            rect_2 = Rectangle(2, -5)

    def test_object_instantiation_x_invalid_value(self):
        with self.assertRaises(ValueError):
            rect_2 = Rectangle(2, 5, x=-5)

    def test_object_instantiation_y_invalid_value(self):
        with self.assertRaises(ValueError):
            rect_2 = Rectangle(-2, 5, y=-5)

    def test_object_instantiation_width_invalid_type(self):
        with self.assertRaises(TypeError):
            rect_2 = Rectangle('55', 5)
            rect_2 = Rectangle(55.4, 5)

    def test_object_instantiation_height_invalid_type(self):
        with self.assertRaises(TypeError):
            rect_2 = Rectangle(2, '88')
            rect_2 = Rectangle(2, [])

    def test_object_instantiation_x_invalid_type(self):
        with self.assertRaises(TypeError):
            rect_2 = Rectangle(2, 5, x='5')
            rect_2 = Rectangle(2, 5, x=885.1)

    def test_object_instantiation_y_invalid_type(self):
        with self.assertRaises(ValueError):
            rect_2 = Rectangle(-2, 5, y='9')
            rect_2 = Rectangle(-2, 5, y={})

    #test error msg............


    def test_area_method(self):
        self.rect_1.width = 2
        self.rect_1.height = 4
        self.assertEqual(self.rect_1.area(), 8)

    def test_display_method(self):
        pass
