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

    def test_public_repos_url(self):
        "test _public_repos_url property"
        with mock.patch('client.GithubOrgClient.org',
                        new_callable=mock.PropertyMock) as mock_property:
            mock_property.return_value = {
                'repos_url': 'https://api.github.com/orgs/google/repos'
            }
            client = GithubOrgClient('google')
            self.assertEqual(client._public_repos_url,
                             'https://api.github.com/orgs/google/repos'
                             )

    @mock.patch('client.get_json')
    def test_public_repos(self, mock_json):
        "test public_repos method"
        mock_json.return_value = [
            {
                'name': 'truth',
                'license': {'key': 'apache-2.0',
                            'name': 'Apache License 2.0',
                            },
            },
            {
                'name': 'ruby-openid-apps-discovery',
                'license': None,
            }
        ]
        with mock.patch('client.GithubOrgClient._public_repos_url',
                        new_callable=mock.PropertyMock) as mock_property:
            mock_property.return_value = (
                'https://api.github.com/orgs/google/'
                'repos'
            )
            client = GithubOrgClient('google')
            client.public_repos()
            self.assertEqual(client.public_repos(),
                             ['truth',
                              'ruby-openid-apps-discovery',
                              ]
                             )
            mock_property.assert_called_once()
        mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        "test has_license method"
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)
