from flask import abort

from app.sessions.domain.SessionId import SessionId
from app.sessions.domain.SessionStructure import SessionStructure
from app.sessions.interface.FirestoreRepository import SessionRepository


class DeleteSession(SessionStructure):
    def execute(self, fill_id):
        session_id = SessionId(fill_id)
        if session_id.is_valid() is False:
            abort(400)

        repo = SessionRepository()
        return repo.deleteSession(session_id.value)
