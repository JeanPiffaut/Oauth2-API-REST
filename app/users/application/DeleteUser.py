from app.users.domain.UserId import UserId
from app.users.interface.FirestoreRepository import UserRepository


class DeleteUser:
    _id: UserId = None

    def setId(self, user_id: str):
        self._id = UserId(user_id)

    def execute(self):
        repo = UserRepository()
        return repo.deleteUser(self._id)
