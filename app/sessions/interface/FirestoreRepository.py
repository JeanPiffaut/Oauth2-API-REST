from flask import abort

from app.common.domain.RepositoryModel import RepositoryModel
from config.firestore import fr


class SessionRepository(RepositoryModel):
    _collection = 'Sessions'

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
