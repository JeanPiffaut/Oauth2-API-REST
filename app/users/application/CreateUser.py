from app.users.domain.UserStructure import UserStructure
from app.users.interface.FirestoreRepository import UserRepository


class CreateUser(UserStructure):

    def execute(self):
        repo = UserRepository()
        return repo.createUser(self.to_dict())
