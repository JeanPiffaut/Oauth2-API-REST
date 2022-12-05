from flask import abort

from app.credentials.domain.CredentialId import CredentialId
from app.credentials.domain.CredentialStructure import CredentialStructure
from app.credentials.interface.FirestoreRepository import CredentialRepository


class DeleteCredential(CredentialStructure):
    def execute(self, fill_id):
        credential_id = CredentialId(fill_id)
        if credential_id.is_valid() is False:
            abort(400)

        repo = CredentialRepository()
        return repo.deleteCredential(credential_id.value)
