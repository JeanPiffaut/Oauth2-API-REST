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
