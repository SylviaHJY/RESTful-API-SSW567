import unittest
from unittest.mock import patch

from RESTful import getUserCommits;

class TestGetUserCommits(unittest.TestCase):
    @patch('requests.get')
    def test_user_not_found(self, mock_get):
        mock_get.return_value.status_code = 404
        self.assertEqual(getUserCommits("invalidUserId"), [])

    @patch('requests.get')
    def test_get_user_commits(self, mock_get):
     mock_get.side_effect = [
        unittest.mock.Mock(status_code=200, json=lambda: [{"name": "csp", "url": "https://api.github.com/repos/richkempinski/csp"}]),
        unittest.mock.Mock(status_code=200, json=lambda: [1, 2])  # Two commits
    ]
    self.assertEqual(getUserCommits("richkempinski")[0], "Repo: csp Number of commits: 2\n")


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
