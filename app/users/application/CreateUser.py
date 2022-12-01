from app.users.domain.User import User
from app.users.domain.UserEmail import UserEmail
from app.users.domain.UserName import UserName
from app.users.interface.FirestoreRepository import UserRepository


class CreateUser:
    _name: UserName = None
    _email: UserEmail = None

    def setName(self, user_name: str):
        self._name = UserName(user_name)

    def setEmail(self, user_email: str):
        self._email = UserEmail(user_email)

    def execute(self):
        user = User()
        user.setName(self._name)
        user.setEmail(self._email)

        repo = UserRepository()
        return repo.createUser(user)
