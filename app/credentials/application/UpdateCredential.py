from flask import abort

from app.auth_types.interface.FirestoreRepository import AuthTypeRepository
from app.credentials.domain.CredentialId import CredentialId
from app.credentials.domain.CredentialStructure import CredentialStructure
from app.credentials.interface.FirestoreRepository import CredentialRepository


class UpdateCredential(CredentialStructure):
    def execute(self, fill_id):
        credential_id = CredentialId(fill_id)
        if credential_id.is_valid() is False:
            abort(400)

        repo = CredentialRepository()
        return repo.updateCredential(credential_id.value, self.to_dict())

    def setAuthTypeId(self, credential_auth_type_id):
        auth_repo = AuthTypeRepository()
        result = auth_repo.listAuthTypeById(credential_auth_type_id)

        self.setAuthTypeRef(result.reference)
