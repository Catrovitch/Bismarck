import os

class User:

    def __init__(self, username, password):

        self.username = username
        self.password = password
    
    def create_repositary(self):

        directory = f"{self.username}"

        parent_dir = "../repositories/users"

        path = os.path.join(parent_dir, directory)


