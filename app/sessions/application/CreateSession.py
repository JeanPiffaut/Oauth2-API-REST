import hashlib
import uuid
from datetime import datetime

import pytz
from decouple import config
from flask import abort

from app.sessions.domain.SessionStructure import SessionStructure
from app.sessions.interface.FirestoreRepository import SessionRepository
from app.users.interface.FirestoreRepository import UserRepository


class CreateSession(SessionStructure):
    def execute(self):
        token = hashlib.md5(uuid.uuid4().__str__().encode()).hexdigest()
        self.setToken(token)

        tz = pytz.timezone(config('TIMEZONE'))
        now = datetime.now(tz).strftime(config('DATE_TIME_FORMAT'))

        self.setCreationDate(now)
        self.setLastActivity(now)

        self.setLifeTime(config('TOKEN_LIFE_TIME'))

        repo = SessionRepository()
        params = self.to_dict()
        repo.createSession(self.to_dict())

        return True

    def setUserId(self, user_id):
        user_repo = UserRepository()
        result = user_repo.listUsersById(user_id)
        if result.exists is False:
            abort(404, "User not found")

        self.setUserRef(result.reference)
