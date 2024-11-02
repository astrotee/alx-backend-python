#!/usr/bin/env python3
"Parameterize a unit test"
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    @parameterized.expand([
        (({"a": 1}, ("a",)), 1),
        (({"a": {"b": 2}}, ("a",)), {"b": 2}),
        (({"a": {"b": 2}}, ("a", "b")), 2),
    ])
    def test_access_nested_map(self, input, expected):
        self.assertEqual(access_nested_map(*input), expected)
