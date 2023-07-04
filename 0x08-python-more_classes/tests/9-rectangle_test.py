#!/usr/bin/python3
"""
Unittest for Rectangle class define in 9-rectangle module
"""
import unittest
file = __import__('9-rectangle')

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

    def test_string_representation_of_obj_using__str__(self):
        self.rect.height = 1
        self.rect.width = 2
        self.rect.print_symbol = "#"
        output = "##"
        self.assertEqual(str(self.rect), output)
    
    def test_empty_representation_of_obj_using__str__(self):
        self.rect.height = 1
        self.rect.width = 0
        output = ""
        self.assertEqual(str(self.rect), output)
    
    def test_string_representation_of_obj_using__repr__(self):
        output = "Rectangle(4, 6)"
        self.assertIn(output, repr(self.rect))
    
    def test_empty_string_representation_of_obj_using__repr__(self):
        output = "Rectangle(0, 0)"
        self.rect = file.Rectangle()
        self.assertIn(output, repr(self.rect))

    def test_check_new_obj_type(self):
        Rectangle= __import__('4-rectangle').Rectangle
        new_rect = eval(repr(self.rect))
        print(new_rect)
        self.assertTrue(type(new_rect) is not type(self.rect))

    def test_new_obj_diff_old_rect_using_eval_repr(self):
        Rectangle = __import__('4-rectangle').Rectangle
        new_rect = eval(repr(self.rect))
        self.assertFalse(new_rect is self.rect)
        self.assertFalse(hex(id(new_rect)) == hex(id(self.rect)))

    def test_custom_obj_deletion_using_del__(self):
        output = "Bye rectangle..."
        self.rect_2 = file.Rectangle()
        rest = self.rect_2.__del__()
        self.assertIsNone(rest)

    def test_incremention_after_new_instance_instantiation(self):
        objs = list()
        for i in range(0, 100):
            objs.append(file.Rectangle())
        self.assertEqual(file.Rectangle.number_of_instances, 100)
    
    def test_decremention_after_new_instance_deletion(self):
        objs = []
        for i in range(0, 30):
            objs.append(file.Rectangle())
        for i in range(0, (len(objs) - 20)):
            del objs[i]
        self.assertEqual(file.Rectangle.number_of_instances, 20)
        self.assertEqual(objs[0].number_of_instances, 20)

    def test_string_as_print_symbol_class_level(self):
        file.Rectangle.print_symbol = "&"
        rect_1 = file.Rectangle(8, 4)
        output = '&&&&&&&&\n&&&&&&&&\n&&&&&&&&\n&&&&&&&&'
        self.assertEqual(str(rect_1), output)
    
    def test_string_as_print_symbol_obj_level(self):
        rect_1 = file.Rectangle(8, 4)
        rect_1.print_symbol = symb  = "+"
        _format = f'{str(symb) * rect_1.width}'
        output = _format + '\n' + _format +'\n' +  _format + '\n' + _format
        self.assertEqual(str(rect_1), output)
    
    def test_immutable_object_as_print_symbol(self):
        rect_1 = file.Rectangle(3, 2)
        rect_1.print_symbol = symb = 0.07
        _format = f'{str(symb) * rect_1.width}'
        output = _format + '\n' + _format
        self.assertEqual(str(rect_1), output)

        rect_1.print_symbol = symb = "hello ALX"
        _format = f'{str(symb) * rect_1.width}'
        output = _format + '\n' + _format
        self.assertEqual(str(rect_1), output)
        
        rect_1.print_symbol = symb = True
        _format = f'{str(symb) * rect_1.width}'
        output = _format + '\n' + _format
        self.assertEqual(str(rect_1), output)
    
    def test_mutable_object_as_print_symbol(self):
        rect_1 = file.Rectangle(3, 2)
        rect_1.print_symbol = symb = ["007", "ALX", 5]
        _format = f'{str(symb) * rect_1.width}'
        output = _format + '\n' + _format
        self.assertEqual(str(rect_1), output)

        rect_1.print_symbol = symb = {"test": "enough", "I_am":{"1":"tired", "2":"happy"}, "for": 2023}
        _format = f'{str(symb) * rect_1.width}'
        output = _format + '\n' + _format
        self.assertEqual(str(rect_1), output)
        
        rect_1.print_symbol = symb = 1, 5, "Test agaim"
        _format = f'{str(symb) * rect_1.width}'
        output = _format + '\n' + _format
        self.assertEqual(str(rect_1), output)

    def test_rect_area_comparison(self):
        li = list()
        Rectangle  = file.Rectangle
        comp = Rectangle.bigger_or_equal
        val = [2, 5, 6, 3 ,7, 6, 6, 7]
        j = 0
        for i in range(0, int(len(val) / 2)):
            li.append(Rectangle(val[j], val[j+1]))
            j += 2
        self.assertEqual(comp(li[0], li[1]), li[1])
        self.assertEqual(comp(li[2], li[1]), li[2])
        self.assertEqual(comp(li[2], li[3]), li[2])
        self.assertEqual(comp(li[3], li[3]), li[3])

    def test_not_Rectangle_obj(self):
        comp = file.Rectangle.bigger_or_equal
        rect_1 = 1
        rect_2 = 0.88
        rect_3 = 1, 8
        rect_4 = {"height":4, "width":6}
        rect_5 = [10, 80]
        with self.assertRaises(TypeError):
            self.assertEqual(comp(rect_1, rect_2), rect_1)
        with self.assertRaises(TypeError):
            self.assertEqual(comp(rect_2, rect_3), rect_3)
        with self.assertRaises(TypeError):
            self.assertEqual(comp(rect_4, rect_4), rect_4)
        with self.assertRaises(TypeError):
            self.assertEqual(comp(rect_5, rect_5), rect_5)
        with self.assertRaises(TypeError):
            self.assertEqual(comp(rect_4, rect_5), rect_5)

    def test_square_obj_value(self):
        sq = file.Rectangle(5, 5)
        sq.print_symbol = symb = "$"
        self.assertEqual(sq.area(), 25)
        self.assertEqual(sq.perimeter(), 20)
        out = "Rectangle(5, 5)"
        self.assertEqual(repr(sq), out)
        _format = f'{str(symb) * sq.width}'
        output = _format + '\n' + _format +'\n' +  _format + '\n' + _format + '\n' + _format
        self.assertEqual(str(sq), output)
        

if __name__ == "__main__":
    unittest.main(verbosity=2)
