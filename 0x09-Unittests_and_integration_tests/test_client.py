#!/usr/bin/env python3
"""
test_client
"""
import unittest
from client import GithubOrgClient
from unittest.mock import patch, Mock, PropertyMock
from unittest import mock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
    test_client
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

    @mock.patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Testing public_repos method
        """
        mock_get_json.return_value = [{"name": "google"},
                                      {"name": "abc"}]
        with mock.patch.object(GithubOrgClient, "_public_repos_url",
                               new_callable=PropertyMock) as mock_public:
            mock_public.return_value = "http://testurl.com"
            g_client = GithubOrgClient("facebook")
            res = g_client.public_repos()
            self.assertEqual(res, ["google", "abc"])
            mock_get_json.assert_called_once()
            mock_public.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license, expected):
        """Testing for test_has_license
        """
        g_client = GithubOrgClient("facebook")
        res = (g_client.has_license(repo, license))
        self.assertEqual(res, expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ class TestIntegrationGithubOrgClient """
    @classmethod
    def setUpClass(cls):
        """set up class"""
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """tear down class"""
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
