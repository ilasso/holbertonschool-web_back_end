#!/usr/bin/env python3
"""
class to make test cases through unittes
"""
from parameterized import parameterized, parameterized_class
from utils import access_nested_map
import unittest
import sys


class TestAccessNestedMap(unittest.TestCase):
    """
    test accessNestedMap class
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, answer):
        """
        test  access_nestet_map function with 3 cases in
        @parameterized.expand
        """
        self.assertEqual(access_nested_map(nested_map, path), answer)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """catch keyError testcase"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[-1], path[-1])


if __name__ == '__main__':
    unittest.main()
