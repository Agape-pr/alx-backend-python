#!/usr/bin/env python3
"""Unittests for GithubOrgClient.org method"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from parameterized import parameterized_class


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



#!/usr/bin/env python3
"""Unit tests for GithubOrgClient"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for the GithubOrgClient class"""

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test public_repos method with mocked dependencies"""

        # Custom repo payload
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = test_payload

        # Patch _public_repos_url contextually
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "https://api.github.com/orgs/testorg/repos"

            client = GithubOrgClient("testorg")
            repos = client.public_repos()

            # Assertions
            self.assertEqual(repos, ["repo1", "repo2", "repo3"])
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/testorg/repos")
            mock_url.assert_called_once()

from parameterized import parameterized

class TestGithubOrgClient(unittest.TestCase):
    ...

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license with different repo license cases"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized_class

from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos



@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
    }
])


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests with mocked external HTTP requests only"""

    @classmethod
    def setUpClass(cls):
        """Mock requests.get and define side_effect behavior"""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        # Create a side_effect function that returns mock response
        def side_effect(url):
            if url == "https://api.github.com/orgs/test_org":
                return Mock(json=lambda: cls.org_payload)
            elif url == cls.org_payload.get("repos_url"):
                return Mock(json=lambda: cls.repos_payload)
            return None

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher after all tests"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos returns expected repo names"""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos returns only Apache2-licensed repos"""
        client = GithubOrgClient("test_org")
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )




import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests with mocked external HTTP requests only"""

    @classmethod
    def setUpClass(cls):
        """Mock requests.get and define side_effect behavior"""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            if url == "https://api.github.com/orgs/test_org":
                return Mock(json=lambda: cls.org_payload)
            elif url == cls.org_payload.get("repos_url"):
                return Mock(json=lambda: cls.repos_payload)
            return Mock()

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(license="apache-2.0"), self.apache2_repos)
