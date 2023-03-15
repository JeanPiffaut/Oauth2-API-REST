from flask import abort

from app.common.domain.RepositoryModel import RepositoryModel
from config.firestore import fr


class CredentialRepository(RepositoryModel):
    _collection = 'Credentials'

    def listCredentials(self, fill_user=None, fill_auth_type=None, fill_username=None, fill_token=None):
        coll = fr.collection(self._collection)

        if fill_user is not None:
            coll = coll.where('user', '==', fill_user)

        if fill_auth_type is not None:
            coll = coll.where('auth_type', '==', fill_auth_type)

        if fill_username is not None:
            print(fill_username)
            coll = coll.where('username', '==', fill_username)

        if fill_token is not None:
            print(fill_token)
            coll = coll.where('token', '==', fill_token)

        return coll.limit(100).get()

    def listCredentialsById(self, fill_id):
        coll = fr.collection(self._collection)
        return coll.document(fill_id).get()

    def createCredential(self, data):
        coll = fr.collection(self._collection)
        result = coll.add(data)
        if result:
            return True
        else:
            return False

    def updateCredential(self, fill_id, data):
        coll = fr.collection(self._collection)
        doc = coll.document(fill_id)

        if doc.get().exists is False:
            abort(403, 'The credential don\'t exist')

        result = doc.update(data)
        if result:
            return True
        else:
            return False

    def deleteCredential(self, fill_id):
        coll = fr.collection(self._collection)
        doc = coll.document(fill_id)
        if doc.get().exists is False:
            abort(403, 'The credential don\'t exist')

        result = doc.delete()
        if result:
            return True
        else:
            return False
