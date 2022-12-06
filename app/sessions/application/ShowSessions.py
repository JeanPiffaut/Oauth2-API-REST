from flask import abort

from app.sessions.domain.Session import Session
from app.sessions.domain.SessionId import SessionId
from app.sessions.domain.SessionStructure import SessionStructure
from app.sessions.interface.FirestoreRepository import SessionRepository


class ShowSessions(SessionStructure):
    def execute(self, fill_id=None):
        repo = SessionRepository()
        sessions = []

        if fill_id is not None:
            session_id = SessionId(fill_id)
            if session_id.is_valid() is False:
                abort(400)

            result = repo.listSessionsById(session_id.value)
            if result.exists:
                session = Session()
                session.from_firestore_document(result)
                sessions.append(session.to_dict())
        else:
            result = repo.listSessions(self.getUserId(), self.getToken(), self.getCreationDate(),
                                       self.getLastActivity(), self.getLifeTime())
            for doc in result:
                if doc.exists:
                    session = Session()
                    session.from_firestore_document(doc)
                    sessions.append(session.to_dict())

        return sessions
