#!/usr/bin/python3
"""
Unittest for Rectangle class define in 3-rectangle module
"""
import unittest
file = __import__('3-rectangle')

class TestEmptyClass(unittest.TestCase):
    """Test case for empty class"""

    def setUp(self):
        self.rect = file.Rectangle()
        self.rect.height = 6
        self.rect.width = 4

    def test_instance_class(self):
        """Verify the type of class instance"""
        self.assertTrue(self.rect.__class__ == file.Rectangle)

    def test_docstrings(self):
        """Test for  doc"""
        self.assertTrue(len(self.rect.__doc__) > 0)
        self.assertTrue(len(file.__doc__) > 0)

    def test_hidden_attributes(self):
        """Test for hidden attrs"""
        with self.assertRaises(AttributeError): 
            self.assertEqual(self.rect.__width, "__width")
            self.assertEqual(self.rect.__height, "__height")

    def test_init_instance_method_with_invalid_height(self):
        with self.assertRaises(ValueError):
            r = file.Rectangle(2, -8)
    
    def test_init_instance_method_with_invalid_width(self):
        with self.assertRaises(ValueError):
            r = file.Rectangle(-100, 8)
    
    def test_init_instance_method_with_invalid_height_type(self):
        with self.assertRaises(TypeError):
            r = file.Rectangle(2, '587')
    
    def test_init_instance_method_with_invalid_width_type(self):
        with self.assertRaises(TypeError):
            r = file.Rectangle('88', 88)

    def test_get_and_set_value(self):
        self.assertEqual(self.rect.height, 6)
        self.assertEqual(self.rect.width, 4)

    def test_invalid_width(self):
        """Test case for invalid width input"""
        with self.assertRaises(TypeError):
            self.rect.width = "abc"

    def test_negative_width(self):
        """Test case for negative width input"""
        with self.assertRaises(ValueError):
            self.rect.width = -5

    def test_invalid_height(self):
        """Test case for invalid height input"""
        with self.assertRaises(TypeError):
            self.rect.height = "def"

    def test_negative_height(self):
        """Test case for negative height input"""
        with self.assertRaises(ValueError):
            self.rect.height = -8

    def test_is_public_instance_area_method(self):
        self.assertEqual(self.rect.area.__name__, "area")

    def test_is_public_instance_perimeter(self):
        self.assertEqual(self.rect.perimeter.__name__, "perimeter")

    def test_area_method(self):
        self.assertEqual(self.rect.area(), 24)

    def test_perimeter_instance_method(self):
        self.assertEqual(self.rect.perimeter(), 20)

    def test_perimeter_instance_method_with_zero_value_of_height(self):
        self.rect.height = 0
        self.assertEqual(self.rect.perimeter(), 0)

    def test_perimeter_instance_method_with_zero_value_of_width(self):
        self.rect.width = 0
        self.assertEqual(self.rect.perimeter(), 0)

    def test_string_representation_of_obj__str__(self):
        self.rect.height = 1
        self.rect.width = 2
        output = "##"
        self.assertEqual(str(self.rect), output)
    
    def test_empty_representation_of_obj__str__(self):
        self.rect.height = 1
        self.rect.width = 0
        output = ""
        self.assertEqual(str(self.rect), output)
    
    def test_string_representation_of_obj__repr__(self):
        output = "<3-rectangle.Rectangle object at"
        self.assertIn(output, repr(self.rect))



if __name__ == "__main__":
    unittest.main(verbosity=2)
