from flask import abort

from app.users.domain.UserId import UserId
from app.users.domain.UserStructure import UserStructure
from app.users.interface.FirestoreRepository import UserRepository
from app.sessions.interface.FirestoreRepository import SessionRepository


class DeleteUser(UserStructure):
    def execute(self, fill_id):
        user_id = UserId(fill_id)
        if user_id.is_valid() is False:
            abort(400)

        session_repository = SessionRepository()
        result = session_repository.delete_by_user_id(user_id.value)

        if result:
            repo = UserRepository()
            return repo.deleteUser(user_id.value)
        else:
            abort(400)
