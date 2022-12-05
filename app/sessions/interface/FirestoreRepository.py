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
