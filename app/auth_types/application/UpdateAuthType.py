from flask import abort

from app.auth_types.domain.AuthTypeId import AuthTypeId
from app.auth_types.domain.AuthTypeStructure import AuthTypeStructure
from app.auth_types.interface.FirestoreRepository import AuthTypeRepository


class UpdateAuthType(AuthTypeStructure):

    def execute(self, type_id):
        auth_type_id = AuthTypeId(type_id)
        if auth_type_id.is_valid() is False:
            abort(400)

        repo = AuthTypeRepository()
        return repo.updateAuthType(auth_type_id.value, self.to_dict())
