from entities.user import User
from repositories.user_repository import UserRepository
from repositories.user_repository import get_database_connection

class UserControl:

    def __init__(self):

        user_repository = get_database_connection()
        self.repository = UserRepository(user_repository)

    def create_user(self, username, password1, password2):

        if self.repository.find_by_username(username) != None:
            return False
        
        if password1 != password2 or None in (password1, password2):
            return False

        else:
            self.user = User(username, password1, 0)
            self.repository.create(self.user)
        return True


    def login(self, username, password):

        user = self.repository.find_by_username(username)

        if user == None:
            return False
        
        if user.password == password:
            self.user = user
            return True

    def update_rating(self, change):

        user = self.repository.find_by_username(self.user.username)

        print(user.username, user.rating)

        if user == None:
            return False
        
        user.rating += change
        
        self.repository.update_rating(user)

    def get_top_ten(self):

        return self.repository.get_top_ten()