import datetime

from decouple import config

from app.sessions.domain.SessionStructure import SessionStructure


class Session(SessionStructure):
    def from_firestore_document(self, document):
        self.setId(document.id)
        self.setUserId(document.get('user_id'))
        self.setToken(document.get('token'))

        creation_date = datetime.datetime.fromtimestamp(document.get('creation_date').timestamp()).strftime(
            config('DATE_TIME_FORMAT'))
        self.setCreationDate(creation_date)

        last_activity = datetime.datetime.fromtimestamp(document.get('last_activity').timestamp()).strftime(
            config('DATE_TIME_FORMAT'))
        self.setLastActivity(last_activity)
        self.setLifeTime(document.get('life_time'))
