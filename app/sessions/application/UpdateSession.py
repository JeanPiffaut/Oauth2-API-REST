from flask import abort

from app.sessions.domain.SessionId import SessionId
from app.sessions.domain.SessionStructure import SessionStructure
from app.sessions.interface.FirestoreRepository import SessionRepository
from app.users.interface.FirestoreRepository import UserRepository


class UpdateSession(SessionStructure):
    def execute(self, fill_id):
        session_id = SessionId(fill_id)
        if session_id.is_valid() is False:
            abort(400)

        repo = SessionRepository()
        return repo.updateSession(session_id.value, self.to_dict())

    def setUserId(self, user_id):
        user_repo = UserRepository()
        result = user_repo.listUsersById(user_id)
        if result.exists is False:
            abort(400)

        self.setUserRef(result.reference)
