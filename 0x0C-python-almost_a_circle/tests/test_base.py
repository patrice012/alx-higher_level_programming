#!/usr/bin/python3
"""
Unittesting for module models/base.py
"""
import unittest
from models.base import Base


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
