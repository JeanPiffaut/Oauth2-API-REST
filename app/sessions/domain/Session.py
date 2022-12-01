from app.common.domain.ModelBase import ModelBase
from app.sessions.domain import SessionId, SessionToken, SessionCreationDate, SessionLastActivity, SessionLifeTime
from app.users.domain import UserId


class Session(ModelBase):
    _id: SessionId
    _user_id: UserId
    _token: SessionToken
    _creation_date: SessionCreationDate
    _last_activity: SessionLastActivity
    _life_time: SessionLifeTime

    def setId(self, session_id: SessionId):
        self._id = session_id

    def setUserId(self, session_user_id: UserId):
        self._user_id = session_user_id

    def setToken(self, session_token: SessionToken):
        self._token = session_token

    def setCreationDate(self, session_creation_date: SessionCreationDate):
        self._creation_date = session_creation_date

    def setLastActivity(self, session_last_activity: SessionLastActivity):
        self._last_activity = session_last_activity

    def setLifeTime(self, session_life_time: SessionLifeTime):
        self._life_time = session_life_time

    def getId(self):
        return self._id

    def getUserId(self):
        return self._user_id

    def getToken(self):
        return self._token

    def getCreationDate(self):
        return self._creation_date

    def getLastActivity(self):
        return self._last_activity

    def getLifeTime(self):
        return self._life_time