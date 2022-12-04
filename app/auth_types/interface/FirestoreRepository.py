from app.common.domain.RepositoryModel import RepositoryModel
from config.firestore import fr


class AuthTypeRepository(RepositoryModel):
    _collection = 'AuthTypes'

    def createAuthType(self, data):
        coll = fr.collection(self._collection)
        result = coll.add(data)
        if result:
            return True
        else:
            return False

    def listAuthType(self, fill_name=None, client_id=None, client_secret=None):
        coll = fr.collection(self._collection)

        if fill_name is not None:
            coll = coll.where('name', '==', fill_name)

        if client_id is not None:
            coll = coll.where('client_id', '==', client_id)

        if client_secret is not None:
            coll = coll.where('client_secret', '==', client_secret)

        return coll.limit(100).get()

    def listAuthTypeById(self, auth_type_id):
        coll = fr.collection(self._collection)
