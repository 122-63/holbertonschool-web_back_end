#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from nose.tools import assert_equal
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Testing...
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Testing with parameterized
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
