from flask_restful import abort

from app.users.domain.User import User
from app.users.domain.UserId import UserId
from app.users.domain.UserStructure import UserStructure
from app.users.interface.FirestoreRepository import UserRepository


class ShowUsers(UserStructure):

    def execute(self, fill_id=None):
        repo = UserRepository()
        users = []
        if fill_id is not None:
            user_id = UserId(fill_id)
            if user_id.is_valid() is False:
                abort(400)

            result = repo.listUsersById(user_id.value)
            if result.exists:
                user = User()
                user.from_firestore_document(result)
                users.append(user.__dict__)
        else:
            result = repo.listUsers(self.getName(), self.getEmail())
            for doc in result:
                if doc.exists:
                    user = User()
                    user.from_firestore_document(doc)
                    users.append(user.__dict__)

        return users
