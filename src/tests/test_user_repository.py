
import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.sauron = User('Sauron', 'ring123', 0)
        self.frodo = User('Frodo', 'ring123', 0)

    def test_create(self):
        user_repository.create(self.sauron)
        users = user_repository.get_all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.sauron.username)

    def test_find_all(self):
        user_repository.create(self.sauron)
        user_repository.create(self.frodo)
        users = user_repository.get_all_users()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.sauron.username)
        self.assertEqual(users[1].username, self.frodo.username)

    def test_find_by_username(self):
        user_repository.create(self.sauron)

        user = user_repository.get_by_username(self.sauron.username)

        self.assertEqual(user.username, self.sauron.username)