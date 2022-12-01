from app.common.domain.RepositoryModel import RepositoryModel
from config.firestore import fr


class UserRepository(RepositoryModel):
    _collection = 'Users'

    def listUsers(self, fill_name=None, fill_email=None):
        coll = fr.collection(self._collection)

        if fill_name is not None and fill_name.validate() is True:
            coll = coll.where('name', '==', fill_name.value)

        if fill_email is not None and fill_email.validate() is True:
            coll = coll.where('email', '==', fill_email.value)

        return coll.get()

    def listUsersById(self, fill_id):
        coll = fr.collection(self._collection)
        if fill_id.validate() is True:
            return coll.document(fill_id.value).get()
        else:
            return False

    def createUser(self, data):
        coll = fr.collection(self._collection)
        result = coll.add(data.to_dict())
        if result:
            return True
        else:
            return False

    def deleteUser(self, user_id):
        coll = fr.collection(self._collection)
        doc = coll.document(user_id.value)
        result = doc.delete()
        if result:
            return True
        else:
            return False
