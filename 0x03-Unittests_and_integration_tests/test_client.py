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
