# For Unit Tests (used earlier)
TEST_PAYLOAD = [
    {'name': 'Google'},
    {'name': 'Facebook'}
]

# For Integration Tests (task 9)
org_payload = {
    "login": "test_org",
    "repos_url": "https://api.github.com/orgs/test_org/repos",
}

repos_payload = [
    {
        "id": 1,
        "name": "repo1",
        "license": {"key": "apache-2.0"}
    },
    {
        "id": 2,
        "name": "repo2",
        "license": {"key": "mit"}
    },
]

expected_repos = ["repo1", "repo2"]

apache2_repos = ["repo1"]
