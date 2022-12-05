from flask import abort

from app.credentials.domain.Credential import Credential
from app.credentials.domain.CredentialId import CredentialId
from app.credentials.domain.CredentialStructure import CredentialStructure
from app.credentials.interface.FirestoreRepository import CredentialRepository


class ShowCredentials(CredentialStructure):

    def execute(self, fill_id=None):
        repo = CredentialRepository()
        credentials = []
        if fill_id is not None:
            credential_id = CredentialId(fill_id)
            if credential_id.is_valid() is False:
                abort(400)

            result = repo.listCredentialsById(credential_id.value)
            if result.exists:
                credential = Credential()
                credential.from_firestore_document(result)
                credentials.append(credential.to_dict())
        else:
            result = repo.listCredentials(self.getUserId(), self.getAuthTypeId(), self.getUsername(), self.getToken())
            for doc in result:
                if doc.exists:
                    credential = Credential()
                    credential.from_firestore_document(doc)
                    credentials.append(credential.to_dict())

        return credentials
