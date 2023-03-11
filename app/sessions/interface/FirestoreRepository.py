import pytz
from decouple import config
from flask import abort

from app.common.domain.RepositoryModel import RepositoryModel
from config.firestore import fr


class SessionRepository(RepositoryModel):
    _collection = 'Sessions'

    def listSessions(self, fill_user=None, fill_token=None, fill_creation_date=None, fill_last_activity=None,
                     fill_life_time=None):
        coll = fr.collection(self._collection)

        if fill_user is not None:
            coll = coll.where('user', '==', fill_user)

        if fill_token is not None:
            coll = coll.where('token', '==', fill_token)

        if fill_creation_date is not None:
            coll = coll.where('creation_date', '==', fill_creation_date)

        if fill_last_activity is not None:
            coll = coll.where('last_activity', '==', fill_last_activity)

        if fill_life_time is not None:
            coll = coll.where('life_time', '==', fill_life_time)

        return coll.get()

    def listSessionsById(self, fill_id):
        coll = fr.collection(self._collection)
        return coll.document(fill_id).get()

    def createSession(self, data):
        coll = fr.collection(self._collection)

        tz = pytz.timezone(config('TIMEZONE'))
        print(data['creation_date'])
        data['creation_date'] = data['creation_date'].replace(tzinfo=tz).timestamp()
        print(data['creation_date'])
        print(data['last_activity'])
        data['last_activity'] = data['last_activity'].timestamp()
        print(data['last_activity'])
        result = coll.add(data)
        if result:
            return True
        else:
            return False

    def deleteSession(self, session_id):
        coll = fr.collection(self._collection)
        doc = coll.document(session_id)
        if doc.get().exists is False:
            abort(400)

        result = doc.delete()
        if result:
            return True
        else:
            return False

    def updateSession(self, session_id, data):
        coll = fr.collection(self._collection)
        doc = coll.document(session_id)
        if doc.get().exists is False:
            abort(400)

        result = doc.update(data)
        if result:
            return True
        else:
            return False

    def delete_by_user_id(self, user_id):
        coll = fr.collection(self._collection)
        result = coll.where('user_id', '==', user_id).get()
        for doc in result:
            doc.reference.delete()

        result = coll.where('user_id', '==', user_id).get()
        if len(result) == 0:
            return True
        else:
            return False
