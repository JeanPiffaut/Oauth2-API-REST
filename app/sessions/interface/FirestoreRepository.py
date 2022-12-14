from flask import abort

from app.common.domain.RepositoryModel import RepositoryModel
from config.firestore import fr


class SessionRepository(RepositoryModel):
    _collection = 'Sessions'

    def listSessions(self, fill_user_id=None, fill_token=None, fill_creation_date=None, fill_last_activity=None,
                     fill_life_time=None):
        coll = fr.collection(self._collection)

        if fill_user_id is not None:
            coll = coll.where('user_id', '==', fill_user_id)

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
