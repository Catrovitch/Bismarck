import unittest
from entities.user import User


class TestUser(unittest.TestCase):

    def setUp(self):

        pass

    def test_username(self):

        user = User("Gandalf", "oneringtorulethemall123")

        self.assertEqual((user.username, user.password),
                         ("Gandalf", "oneringtorulethemall123"))
