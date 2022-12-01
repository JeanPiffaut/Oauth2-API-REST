from app.users.domain.User import User
from app.users.domain.UserEmail import UserEmail
from app.users.domain.UserId import UserId
from app.users.domain.UserName import UserName
from app.users.interface.FirestoreRepository import UserRepository


class ShowUsers:
    _id: UserId = None
    _name: UserName = None
    _email: UserEmail = None

    def setFillId(self, fill_id: str):
        self._id = UserId(fill_id)

    def setFillName(self, fill_name: str):
        self._name = UserName(fill_name)

    def setFillEmail(self, fill_email: str):
        self._email = UserEmail(fill_email)

    def execute(self):
        repo = UserRepository()
        users = []
        if self._id is not None:
            result = repo.listUsersById(fill_id=self._id)
            if result.exists:
                user = User()
                user.from_firestore_document(result)
                users.append(user.to_dict())
        else:
            result = repo.listUsers(fill_name=self._name, fill_email=self._email)
            for doc in result:
                if doc.exists:
                    user = User()
                    user.from_firestore_document(doc)
                    users.append(user.to_dict())

        return users
