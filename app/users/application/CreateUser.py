from app.users.domain.User import User
from app.users.domain.UserStructure import UserStructure
from app.users.interface.FirestoreRepository import UserRepository


class CreateUser(UserStructure):

    def execute(self):
        if self.name.is_valid() is False:
            return False

        if self.email.is_valid() is False:
            return False

        repo = UserRepository()
        return repo.createUser(self.to_dict())
