import hashlib
import uuid
from datetime import datetime
from decouple import config

from app.sessions.domain.SessionStructure import SessionStructure
from app.sessions.interface.FirestoreRepository import SessionRepository


class CreateSession(SessionStructure):
    def execute(self):
        token = hashlib.md5(uuid.uuid4().__str__().encode()).hexdigest()
        self.setToken(token)

        now = datetime.now().strftime(config('DATE_TIME_FORMAT'))
        self.setCreationDate(now)
        self.setLastActivity(now)

        self.setLifeTime(config('TOKEN_LIFE_TIME'))

        repo = SessionRepository()
        repo.createSession(self.to_dict())

        return True
