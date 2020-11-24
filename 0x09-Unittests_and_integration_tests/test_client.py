#!/usr/bin/env python3
import unittest
from client import GithubOrgClient
from unittest.mock import patch, Mock
from parameterized import parameterized
"""
"""
class TestGithubOrgClient(unittest.TestCase):
    """
    """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json):
        """ Test method returns correct output """
        gc = GithubOrgClient(org_name)
        gc.org()
        mock_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
            )
