#!/usr/bin/env python3
"""
test_client
"""
import unittest
from client import GithubOrgClient
from unittest.mock import patch, Mock, PropertyMock, call
from unittest import mock
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
import requests


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


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ class TestIntegrationGithubOrgClient """

    @classmethod
    def setUpClass(cls):
        """set up class"""
        org = TEST_PAYLOAD[0][0]
        repos = TEST_PAYLOAD[0][1]
        org_mock = Mock()
        org_mock.json = Mock(return_value=org)
        cls.org_mock = org_mock
        repos_mock = Mock()
        repos_mock.json = Mock(return_value=repos)
        cls.repos_mock = repos_mock

        cls.get_patcher = patch('requests.get')
        cls.get = cls.get_patcher.start()

        options = {cls.org_payload["repos_url"]: repos_mock}
        cls.get.side_effect = lambda y: options.get(y, org_mock)

    @classmethod
    def tearDownClass(cls):
        """tear down class"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ public repos test """
        y = GithubOrgClient("x")
        self.assertEqual(y.org, self.org_payload)
        self.assertEqual(y.repos_payload, self.repos_payload)
        self.assertEqual(y.public_repos(), self.expected_repos)
        self.assertEqual(y.public_repos("NONEXISTENT"), [])
        self.get.assert_has_calls([call("https://api.github.com/orgs/x"),
                                   call(self.org_payload["repos_url"])])

    def test_public_repos_with_license(self):
        """ public repos test """
        y = GithubOrgClient("x")
        self.assertEqual(y.org, self.org_payload)
        self.assertEqual(y.repos_payload, self.repos_payload)
        self.assertEqual(y.public_repos(), self.expected_repos)
        self.assertEqual(y.public_repos("NONEXISTENT"), [])
        self.assertEqual(y.public_repos("apache-2.0"), self.apache2_repos)
        self.get.assert_has_calls([call("https://api.github.com/orgs/x"),
                                   call(self.org_payload["repos_url"])])


# if __name__ == '__main__':
#    unittest.main()
