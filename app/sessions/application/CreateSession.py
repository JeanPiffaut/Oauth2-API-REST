import hashlib
from datetime import datetime, timedelta
from decouple import config

from app.sessions.domain.SessionStructure import SessionStructure
from app.sessions.interface.FirestoreRepository import SessionRepository


class CreateSession(SessionStructure):
    def execute(self):
        user_id = self.getUserId()
        token = hashlib.md5(user_id.encode()).hexdigest()
        self.setToken(token)

        now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.setCreationDate(now)
        self.setLastActivity(now)

        self.setLifeTime(config('TOKEN_LIFE_TIME'))

        repo = SessionRepository()
        repo.createSession(self.to_dict())

        return True
