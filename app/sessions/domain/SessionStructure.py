from flask import abort

from app.common.domain.ModuleModel import ModuleModel
from app.sessions.domain.SessionCreationDate import SessionCreationDate
from app.sessions.domain.SessionId import SessionId
from app.sessions.domain.SessionLastActivity import SessionLastActivity
from app.sessions.domain.SessionLifeTime import SessionLifeTime
from app.sessions.domain.SessionToken import SessionToken
from app.sessions.domain.UserId import UserId


class SessionStructure(ModuleModel):
    _id = SessionId(None)
    _user_id = UserId(None)
    _token = SessionToken(None)
    _creation_date = SessionCreationDate(None)
    _last_activity = SessionLastActivity(None)
    _life_time = SessionLifeTime(None)

    def setId(self, session_id):
        self._id = SessionId(session_id)
        if self._id.is_valid() is False:
            abort(400)

    def setUserId(self, session_user_id):
        self._user_id = UserId(session_user_id)
        if self._user_id.is_valid() is False:
            abort(400)

    def setToken(self, session_token):
        self._token = SessionToken(session_token)
        if self._token.is_valid() is False:
            abort(400)

    def setCreationDate(self, session_creation_date):
        self._creation_date = SessionCreationDate(session_creation_date)
        if self._creation_date.is_valid() is False:
            abort(400)

    def setLastActivity(self, session_last_activity):
        self._last_activity = SessionLastActivity(session_last_activity)
        if self._last_activity.is_valid() is False:
            abort(400)

    def setLifeTime(self, session_life_time):
        self._life_time = SessionLifeTime(session_life_time)
        if self._life_time.is_valid() is False:
            abort(400)

    def getId(self):
        return self._id.value

    def getUserId(self):
        return self._user_id.value

    def getToken(self):
        return self._token.value

    def getCreationDate(self):
        return self._creation_date.value

    def getLastActivity(self):
        return self._last_activity.value

    def getLifeTime(self):
        return self._life_time.value

    def to_dict(self):
        session_id = self.getId()
        user_id = self.getUserId()
        token = self.getToken()
        creation_date = self.getCreationDate()
        last_activity = self.getLastActivity()
        life_time = self.getLifeTime()

        params = dict()

        if session_id is not None:
            params['id'] = session_id

        if user_id is not None:
            params['user_id'] = user_id

        if token is not None:
            params['token'] = token

        if creation_date is not None:
            params['creation_date'] = creation_date

        if last_activity is not None:
            params['last_activity'] = last_activity

        if life_time is not None:
            params['life_time'] = life_time

        return params
