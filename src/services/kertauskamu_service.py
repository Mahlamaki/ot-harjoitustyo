from entitied.kertauskamu import User
from repostiories.user_repository import user_repository

class KertauskamuService:

    def __init__(self):
        self.user = None

    def create_user(self,username,name):
        user = self.user_repository.create(User(username,name))
