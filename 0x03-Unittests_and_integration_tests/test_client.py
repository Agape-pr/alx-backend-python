#!/usr/bin/env python3
"""Unittests for GithubOrgClient.org method"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient"""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, expected_response, mock_get_json):
        """Test that GithubOrgClient.org returns correct data and calls get_json"""
        mock_get_json.return_value = expected_response

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, expected_response)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
#!/usr/bin/env python3
"""Unit tests for GithubOrgClient"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for the GithubOrgClient class"""

    def test_public_repos_url(self):
        """Test _public_repos_url returns expected URL from mocked org"""

        # Use patch to mock the 'org' property
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            # Define mocked payload
            mock_org.return_value = {"repos_url": "https://api.github.com/orgs/testorg/repos"}

            # Instantiate the client
            client = GithubOrgClient("testorg")

            # Assert that the _public_repos_url gives correct result
            self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/testorg/repos")
