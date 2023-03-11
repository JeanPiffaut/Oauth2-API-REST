from flask import abort

from app.credentials.domain.Credential import Credential
from app.credentials.domain.CredentialId import CredentialId
from app.credentials.domain.CredentialStructure import CredentialStructure
from app.credentials.interface.FirestoreRepository import CredentialRepository
from app.auth_types.interface.FirestoreRepository import AuthTypeRepository

class ShowCredentials(CredentialStructure):

    def setAuthTypeId(self, credential_auth_type_id):
        auth_repo = AuthTypeRepository()
        result = auth_repo.listAuthTypeById(credential_auth_type_id)

        self.setAuthTypeRef(result.reference)

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
                params = credential.to_dict()
                params['auth_type_id'] = params['auth_type'].id
                params.pop('auth_type')
                credentials.append(params)
        else:
            result = repo.listCredentials(self.getUserId(), self.getAuthTypeRef(), self.getUsername(), self.getToken())
            for doc in result:
                if doc.exists:
                    credential = Credential()
                    credential.from_firestore_document(doc)
                    params = credential.to_dict()
                    params['auth_type_id'] = params['auth_type'].id
                    params.pop('auth_type')
                    credentials.append(params)

        return credentials
