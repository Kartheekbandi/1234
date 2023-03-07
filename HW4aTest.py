import unittest
from HW4a import GithubApi

class TestGitHub(unittest.TestCase):

    def testGithub1(self):
        self.assertNotEqual(GithubApi('hgfigdfuasuofo  wfgsyif'), True)

    def testGithub2(self):
        self.assertNotEqual(GithubApi('valkyron'), False)

    def testGithub3(self):
        self.assertNotEqual(GithubApi('KartheekBandiReddy468473'), True)

    def testGithub4(self):
        self.assertNotEqual(GithubApi('Meghana100301'), False)
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
