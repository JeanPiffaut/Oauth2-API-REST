from flask import abort

from app.common.domain.RepositoryModel import RepositoryModel
from config.firestore import fr


class UserRepository(RepositoryModel):
    _collection = 'Users'

    def listUsers(self, fill_name=None, fill_email=None):
        coll = fr.collection(self._collection)

        if fill_name is not None:
            coll = coll.where('name', '==', fill_name)

        if fill_email is not None:
            coll = coll.where('email', '==', fill_email)

        return coll.limit(100).get()

    def listUsersById(self, fill_id):
        coll = fr.collection(self._collection)
        return coll.document(fill_id).get()

    def createUser(self, data):
        coll = fr.collection(self._collection)
        result = coll.add(data)
        if result:
            return True
        else:
            return False

    def deleteUser(self, user_id):
        coll = fr.collection(self._collection)
        doc = coll.document(user_id)
        if doc.get().exists is False:
            abort(403, 'The user don\'t exist')

        result = doc.delete()
        if result:
            return True
        else:
            return False

    def updateUser(self, user_id, data):
        coll = fr.collection(self._collection)
        doc = coll.document(user_id)

        if doc.get().exists is False:
            abort(403, 'The user don\'t exist')

        result = doc.update(data)
        if result:
            return True
        else:
            return False
