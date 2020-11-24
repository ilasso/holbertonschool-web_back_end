#!/usr/bin/env python3
import unittest
from client import GithubOrgClient
from unittest.mock import patch, Mock, PropertyMock
from unittest import mock
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

    def test_public_repos_url(self):
        """Testing public_repos_url
        """
        with mock.patch.object(GithubOrgClient,
                               "org",
                               new_callable=PropertyMock) as mock_org:
            test_json = {"url": "facebook", "repos_url": "http://testurl.com"}
            mock_org.return_value = test_json
            g_client = GithubOrgClient(test_json.get("url"))
            res = g_client._public_repos_url
            mock_org.assert_called_once()
            self.assertEqual(res, test_json.get("repos_url"))
