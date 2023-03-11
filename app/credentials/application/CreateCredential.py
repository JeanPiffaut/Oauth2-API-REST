from flask import abort

from app.credentials.domain.CredentialStructure import CredentialStructure
from app.credentials.interface.FirestoreRepository import CredentialRepository
from app.auth_types.interface.FirestoreRepository import AuthTypeRepository


class CreateCredential(CredentialStructure):
    def setAuthTypeId(self, credential_auth_type_id):
        auth_repo = AuthTypeRepository()
        result = auth_repo.listAuthTypeById(credential_auth_type_id)

        self.setAuthTypeRef(result.reference)

    def execute(self):
        auth_type = AuthTypeRepository()
        result = auth_type.listAuthTypeById(self.getAuthTypeRef().id)
        if result.exists is False:
            abort(404, "Auth Type not found")

        cred_repo = CredentialRepository()
        return cred_repo.createCredential(self.to_dict())
