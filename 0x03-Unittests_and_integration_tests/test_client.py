#!/usr/bin/env python3
"Tests for the client module"
from typing import Dict
from unittest import TestCase, mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    "tests the GithubOrgClient class"
    @parameterized.expand([
        ('google', {'login': 'google'}),
        ('abc', {'login': 'abc'})
    ])
    @mock.patch('client.get_json')
    def test_org(self, org: str, response: Dict, mock_json: mock.MagicMock):
        "test the return value of org method"
        mock_json.return_value = response
        client = GithubOrgClient(org)
        self.assertEqual(client.org, response)
        self.assertEqual(client.org, response)
        mock_json.assert_called_once_with(f"https://api.github.com/orgs/{org}")
