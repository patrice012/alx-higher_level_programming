#!/usr/bin/python3
"""
Unittest for Rectangle class define in 0-rectangle module
"""
import unittest
file = __import__('0-rectangle')

class TestEmptyClass(unittest.TestCase):
    """Test case for empty class"""

    def setUp(self):
        """Create variable for all tests"""
        self.rect = file.Rectangle()

    def test_instance_class(self):
        """Verify the type of class instance"""
        self.assertTrue(self.rect.__class__ == file.Rectangle)

    def test_class_name_using_instance_attrs(self):
        self.assertEqual(self.rect.__class__.__name__, 'Rectangle')

    def test_docstrings(self):
        self.assertTrue(len(self.rect.__doc__) > 0)
        self.assertTrue(len(file.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
