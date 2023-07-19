#!/usr/bin/python3
"""
Unittesting for module models/base.py
"""
import os
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):

    def test_module_docstrings(self):
        """Test for  docs"""
        self.assertTrue(len(Base.__doc__) > 0)

    def test_base_docstrings(self):
        self.assertTrue(len(Base.__module__.__doc__) > 0)

    def test_base_class_methods__init__docstrings(self):
        self.assertTrue(len(Base.__init__.__doc__) > 0)

    def test_base_class_methods_from_json_string_docstrings(self):
        self.assertTrue(len(Base.from_json_string.__doc__) > 0)

    def test_base_class_methods__to_json_string__docstrings(self):
        self.assertTrue(len(Base.to_json_string.__doc__) > 0)
    
    def test_base_class_methods__save_to_file__docstrings(self):
        self.assertTrue(len(Base.save_to_file.__doc__) > 0)

    def test_base_class_methods_create_docstrings(self):
        self.assertTrue(len(Base.create.__doc__) > 0)

    def test_base_class_methods_load_from_file_docstrings(self):
        self.assertTrue(len(Base.load_from_file.__doc__) > 0)

    def test_base_class_methods_save_to_file_csv_docstrings(self):
        self.assertTrue(len(Base.save_to_file_csv.__doc__) > 0)

    def test_base_class_methods_load_from_file_csv_docstrings(self):
        self.assertTrue(len(Base.load_from_file_csv.__doc__) > 0)

    def test_base_method_draw_docstrings(self):
        self.assertTrue(len(Base.draw.__doc__) > 0)


class TestClassId(unittest.TestCase):

    def setUp(self):
        Base.__nb_objects = 0

    def test_private_attrs(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_init_with_no_id(self):
        base_1  = Base()
        self.assertTrue(base_1.id > 0)
        l = [Base() for i in range(15)]
        self.assertEqual(l[5].id, l[6].id - 1)

    def test_init_with_id(self):
        base_1 = Base(88)
        self.assertEqual(base_1.id, 88)

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)


class TestIdAttribute(unittest.TestCase):
    """Test id setting values"""

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestJsonFormatOuput(unittest.TestCase):
    '''Test for to_json_string() function'''

    def test_valid_input(self):
        _input = [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]
        _output = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(Base.to_json_string(_input), _output)

    def test_current_obj(self):
        _input = Rectangle(10, 7, 2, 8).to_dictionary()
        _output = json.dumps([_input])
        self.assertEqual(Base.to_json_string([_input]), _output)

    def test_invalid_input(self):
        _input = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        _output = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertNotEqual(Base.to_json_string(_input), _output)


    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))



class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_to_json_string_rectangle_type(self):
        rect = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([rect.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        rect = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([rect.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        rect_1 = Rectangle(2, 3, 5, 19, 2)
        rect_2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [rect_1.to_dictionary(), rect_2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        sq = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([sq.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        sq = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([sq.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        sq_1 = Square(10, 2, 3, 4)
        sq_2 = Square(4, 5, 21, 2)
        list_dicts = [sq_1.to_dictionary(), sq_2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        rect = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        rect_1 = Rectangle(10, 7, 2, 8, 5)
        rect_2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rect_1, rect_2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        sq = Square(10, 7, 2, 8)
        Square.save_to_file([sq])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        sq_1 = Square(10, 7, 2, 8)
        sq_2 = Square(8, 1, 2, 3)
        Square.save_to_file([sq_1, sq_2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        sq = Square(10, 7, 2, 8)
        Base.save_to_file([sq])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        sq = Square(9, 2, 39, 2)
        Square.save_to_file([sq])
        sq = Square(10, 7, 2, 8)
        Square.save_to_file([sq])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
                {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
                {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
                ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
                {"id": 89, "size": 10, "height": 4},
                {"id": 7, "size": 1, "height": 7}
                ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_rectangle_original(self):
        rect_1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = rect_1.to_dictionary()
        rect_2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rect_1))

    def test_create_rectangle_new(self):
        rect_1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = rect_1.to_dictionary()
        rect_2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rect_2))

    def test_create_rectangle_is(self):
        rect_1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = rect_1.to_dictionary()
        rect_2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(rect_1, rect_2)

    def test_create_rectangle_equals(self):
        rect_1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = rect_1.to_dictionary()
        rect_2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(rect_1, rect_2)

    def test_create_square_original(self):
        sq_1 = Square(3, 5, 1, 7)
        s1_dictionary = sq_1.to_dictionary()
        sq_2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sq_1))

    def test_create_square_new(self):
        sq_1 = Square(3, 5, 1, 7)
        s1_dictionary = sq_1.to_dictionary()
        sq_2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sq_2))

    def test_create_square_is(self):
        sq_1 = Square(3, 5, 1, 7)
        s1_dictionary = sq_1.to_dictionary()
        sq_2 = Square.create(**s1_dictionary)
        self.assertIsNot(sq_1, sq_2)

    def test_create_square_equals(self):
        sq_1 = Square(3, 5, 1, 7)
        s1_dictionary = sq_1.to_dictionary()
        sq_2 = Square.create(**s1_dictionary)
        self.assertNotEqual(sq_1, sq_2)



class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file_method of Base class."""

    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        rect_1 = Rectangle(10, 7, 2, 8, 1)
        rect_2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect_1, rect_2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rect_1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        rect_1 = Rectangle(10, 7, 2, 8, 1)
        rect_2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect_1, rect_2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rect_2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        rect_1 = Rectangle(10, 7, 2, 8, 1)
        rect_2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect_1, rect_2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        sq_1 = Square(5, 1, 3, 3)
        sq_2 = Square(9, 5, 2, 3)
        Square.save_to_file([sq_1, sq_2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(sq_1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        sq_1 = Square(5, 1, 3, 3)
        sq_2 = Square(9, 5, 2, 3)
        Square.save_to_file([sq_1, sq_2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(sq_2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        sq_1 = Square(5, 1, 3, 3)
        sq_2 = Square(9, 5, 2, 3)
        Square.save_to_file([sq_1, sq_2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
