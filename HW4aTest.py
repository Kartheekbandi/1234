import unittest
import urllib
from unittest.mock import patch, Mock
from HW4a import GithubApi


class TestGithubApi(unittest.TestCase):

    @patch('GithubApi.urllib.request.urlopen')
    def test_valid_user(self, mock_urlopen):
        mock_response = Mock()
        mock_response.read.return_value = b'[{"name": "repo1", "description": "description1", "commits_url": "url1"}, {"name": "repo2", "description": "description2", "commits_url": "url2"}]'
        mock_urlopen.return_value = mock_response
        self.assertEqual(GithubApi("Kartheekbandi"), "success")

    @patch('GithubApi.urllib.request.urlopen')
    def test_invalid_user(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.HTTPError("URL", 404, "Not Found", None, None)
        self.assertEqual(GithubApi("invaliduser123"), "GitHub User doesn't exist!!")

    @patch('GithubApi.urllib.request.urlopen')
    def test_no_public_repos(self, mock_urlopen):
        mock_response = Mock()
        mock_response.read.return_value = b'[]'
        mock_urlopen.return_value = mock_response
        self.assertEqual(GithubApi("testuser"), "No Repos")


if __name__ == '__main__':
    unittest.main()
