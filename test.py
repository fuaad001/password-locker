import unittest
from user import User
from credentials import Credentials

class TestLocker(unittest.TestCase):
    """
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("fuaad001", "qwerty123**")

        self.new_account = Credentials("GitHub", "fuaad001", "qwerty123**")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''

        User.user_list = []
        Credentials.credentials_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name, "fuaad001")
        self.assertEqual(self.new_user.password, "qwerty123**")
        self.assertEqual(self.new_account.account_name, "GitHub")
        self.assertEqual(self.new_account.account_user_name, "fuaad001")
        self.assertEqual(self.new_account.account_password, "qwerty123**")

    def test_create_user(self):
        '''
        test_create_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.create_user()
        self.assertEqual(len(User.user_list),1)

    def test_add_credentials(self):
        '''
        test_add_credentials test case to test if the credentials object is saved into
         the credentials list
        '''
        self.new_account.add_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
