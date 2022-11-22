from entities.user import User
from stored_data import data

class UserRepository:
    def __init__(self,data):
        self._data = data

    def create_user(self, user):
        
        return self._data[user.username]=user.name
