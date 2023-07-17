#!/usr/bin/python3
"""
Unittesting for module models/base.py
"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):

    def test_docstrings(self):
        """Test for  doc"""
        self.assertTrue(len(Base.__doc__) > 0)
        self.assertTrue(len(Base.__module__.__doc__) > 0)

    def test_private_attrs(self):
        with self.assertRaises(AttributeError):
            self.assertTrue(Base.__nb_objects)

    def test_init_with_no_id(self):
        base_1  = Base()
        self.assertEqual(base_1.id, 1)
        l = [Base() for i in range(15)]
        self.assertEqual(l[5].id, 7)

    def test_init_with_id(self):
        base_1 = Base(88)
        self.assertEqual(base_1.id, 88)


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

