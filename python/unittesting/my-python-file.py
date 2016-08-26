#! /usr/bin/env python
import unittest


def main():
    print "hello world"


def is_odd(value):
    return value % 2 == 1


if __name__ == '__main__':
    main()


class IsOddTests(unittest.TestCase):

    def test_even_number_returns_false(self):
        """Assert even numbers result in a false response"""
        test_value = 2
        result = is_odd(test_value)
        self.assertFalse(result)

    def test_odd_number_returns_true(self):
        """Assert odd numbers result in a true response"""
        test_value = 3
        result = is_odd(test_value)
        self.assertTrue(result)

    def test_string_value_raises_type_exception(self):
        test_value = '3'
        with self.assertRaises(TypeError):
            is_odd(test_value)
