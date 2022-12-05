from flask import abort

from app.auth_types.domain.AuthType import AuthType
from app.auth_types.domain.AuthTypeId import AuthTypeId
from app.auth_types.domain.AuthTypeStructure import AuthTypeStructure
from app.auth_types.interface.FirestoreRepository import AuthTypeRepository


class ShowAuthType(AuthTypeStructure):

    def execute(self, fill_id=None):
        repo = AuthTypeRepository()
        auth_types = []
        if fill_id is not None:
            auth_type_id = AuthTypeId(fill_id)
            if auth_type_id.is_valid() is False:
                abort(400)

            result = repo.listAuthTypeById(auth_type_id.value)
            if result.exists:
                auth_type = AuthType()
                auth_type.from_firestore_document(result)
                auth_types.append(auth_type.to_dict())
        else:
            result = repo.listAuthType(self.getName(), self.getClientId(), self.getClientSecret())
            for doc in result:
                if doc.exists:
                    auth_type = AuthType()
                    auth_type.from_firestore_document(doc)
                    auth_types.append(auth_type.to_dict())

        return auth_types
