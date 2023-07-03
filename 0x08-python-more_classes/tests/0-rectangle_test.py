#!/usr/bin/python3
"""
Unittest for Rectangle class define in 0-rectangle module
"""
import unittest
Rectangle = __import__('0-rectangle').Rectangle

class TestEmptyClass(unittest.TestCase):
    """Test case for empty class"""

    def setUp(self):
        """Create variable for all tests"""
        self.rect = Rectangle()

    def test_instance_class(self):
        """Verify the type of class instance"""
        self.assertTrue(self.rect.__class__ == Rectangle)

if __name__ == "__main__":
    unittest.main()
