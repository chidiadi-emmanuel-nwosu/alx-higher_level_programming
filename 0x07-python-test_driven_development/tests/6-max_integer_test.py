#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class for test different edge cases for
       max_integer function
    """

    def test_correct_input(self):
        """Test the function for correct list inputs"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 1, 2]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-10, -8, 0]), 0)

    def test_empty(self):
        """Test the function for empty list"""
        self.assertEqual(max_integer([]), None)

    def test_None(self):
        """Test the function when nothing is passed"""
        self.assertEqual(max_integer(), None)

    def test_string(self):
        """Test the function for string input list"""
        with self.assertRaises(TypeError):
            max_integer(["1", 2, 3, "4"])

    def test_int(self):
        """Test the function when non-list type is passed"""
        with self.assertRaises(TypeError):
            max_integer(1234)
