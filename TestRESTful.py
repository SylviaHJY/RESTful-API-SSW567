import unittest;

from RESTful import getUserCommits;

class TestGetUserCommits(unittest.TestCase):     
     def test_user_not_found(self):
        self.assertEqual(getUserCommits("invalidUserId"),[])
        
     def test_get_user_commits(self):
        self.assertEqual(getUserCommits("richkempinski")[0],"Repo: csp Number of commits: 2\n")
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
