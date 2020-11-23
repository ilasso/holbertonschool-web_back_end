#!/usr/bin/env python3
"""
class to make test cases through unittes
"""
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json, memoize
import unittest
import sys
from unittest.mock import patch, Mock
import requests
import json


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


class TestGetJson(unittest.TestCase):
    """mock get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """ test the output of the func
        check: https://www.youtube.com/watch?v=opsctSvcvs4
        """
        response = Mock()
        response.json.return_value = test_payload
        patcher = patch('requests.get', return_value=response)
        patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        patcher.stop()
        # using with doesn't necesary start/stop
        """with patch('requests.get', return_value=response):
            self.assertEqual(get_json(test_url),test_payload)"""


class TestMemoize(unittest.TestCase):
    """testing with memoization """
    def test_memoize(self):
        """ testing memoize decorator"""
        class TestClass:
            """ Test Class
                Methods:
                    a_method, a_property
            """

            def a_method(self):
                """ a_method"""
                return 42

            @memoize
            def a_property(self):
                """ a_property"""
                return self.a_method()

        with patch.object(TestClass, "a_method",
                          return_value=42) as mock_method:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mock_method.assert_called_once


if __name__ == '__main__':
    unittest.main()
