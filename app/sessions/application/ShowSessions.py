from flask import abort

from app.sessions.domain.Session import Session
from app.sessions.domain.SessionId import SessionId
from app.sessions.domain.SessionStructure import SessionStructure
from app.sessions.interface.FirestoreRepository import SessionRepository
from decouple import config


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
                params = session.to_dict()
                params['creation_date'] = params['creation_date'].strftime(config('DATE_TIME_FORMAT'))
                params['last_activity'] = params['last_activity'].strftime(config('DATE_TIME_FORMAT'))
                sessions.append(params)
        else:
            result = repo.listSessions(self.getUserId(), self.getToken(), self.getCreationDate(),
                                       self.getLastActivity(), self.getLifeTime())
            for doc in result:
                if doc.exists:
                    session = Session()
                    session.from_firestore_document(doc)
                    params = session.to_dict()
                    params['creation_date'] = params['creation_date'].strftime(config('DATE_TIME_FORMAT'))
                    params['last_activity'] = params['last_activity'].strftime(config('DATE_TIME_FORMAT'))
                    sessions.append(params)

        return sessions
