#!/usr/bin/env python3
"Parameterize a unit test"
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    "tests the access_nested_map function"
    @parameterized.expand([
        (({"a": 1}, ("a",)), 1),
        (({"a": {"b": 2}}, ("a",)), {"b": 2}),
        (({"a": {"b": 2}}, ("a", "b")), 2),
    ])
    def test_access_nested_map(self, input, expected):
        "test the return value"
        self.assertEqual(access_nested_map(*input), expected)

    @parameterized.expand([
        (({}, ("a",)), "a"),
        (({"a": 1}, ("a", "b")), "b"),
    ])
    def test_access_nested_map_exception(self, input, key):
        "test if KeyError correctly"
        with self.assertRaises(KeyError, msg=key):
            access_nested_map(*input)
