from app.users.domain.User import User
from app.users.domain.UserEmail import UserEmail
from app.users.domain.UserId import UserId
from app.users.domain.UserName import UserName
from app.users.interface.FirestoreRepository import UserRepository


class ShowUsers:
    _name: UserName = None
    _email: UserEmail = None

    def setFillName(self, fill_name: str):
        self._name = UserName(fill_name)

    def setFillEmail(self, fill_email: str):
        self._email = UserEmail(fill_email)

    def show(self):
        repo = UserRepository()
        result = repo.listUsers(fill_name=self._name, fill_email=self._email)

        users = []

        for doc in result:
            user = User()
            user.setId(UserId(doc.id))
            user.setName(UserName(doc.get('name')))
            user.setEmail(UserEmail(doc.get('email')))
            users.append(user.to_dict())

        return users
