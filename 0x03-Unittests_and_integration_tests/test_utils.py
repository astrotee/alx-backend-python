#!/usr/bin/env python3
"Parameterize a unit test"
from unittest import TestCase, mock
from parameterized import parameterized
from utils import access_nested_map, get_json


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


class TestGetJson(TestCase):
    "tests for the get_json function"
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        "test the return value and that it call get and json correctly"
        with mock.patch('requests.get') as mock_get:
            mock_reponse = mock_get.return_value
            mock_reponse.json.return_value = payload
            self.assertEqual(get_json(url), payload)
            mock_get.assert_called_once_with(url)
