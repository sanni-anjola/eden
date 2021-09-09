import unittest
from models.User import User


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def __init__(self) -> None:
        self.user = User()

    def test_user_has_login_id(self):
        self.assertEqual(self.user.login_id, "chidi111")




if __name__ == '__main__':
    unittest.main()
