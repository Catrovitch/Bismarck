import unittest
from entities.user import User


class TestUser(unittest.TestCase):

    def setUp(self):

        pass

    def test_username(self):

        user = User("Gandalf", "oneringtorulethemall123", 0)

        self.assertEqual((user.username, user.password, user.rating),
                         ("Gandalf", "oneringtorulethemall123", 0))
