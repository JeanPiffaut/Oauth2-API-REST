from app.users.domain.User import User
from app.users.domain.UserStructure import UserStructure
from app.users.interface.FirestoreRepository import UserRepository


class CreateUser(UserStructure):

    def execute(self):
        repo = UserRepository()
        return repo.createUser(self.__dict__)
