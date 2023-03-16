from flask import abort

from app.credentials.domain.Credential import Credential
from app.credentials.domain.CredentialId import CredentialId
from app.credentials.domain.CredentialStructure import CredentialStructure
from app.credentials.interface.FirestoreRepository import CredentialRepository
from app.users.interface.FirestoreRepository import UserRepository


class ShowCredentials(CredentialStructure):
    def setUserId(self, user_id):
        user_repo = UserRepository()
        result = user_repo.listUsersById(user_id)
        if result.exists is False:
            abort(404, "User not found")

        self.setUserRef(result.reference)

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
                params['user_id'] = params['user'].id
                params.pop('user')
                params['auth_type_id'] = params['auth_type'].id
                params.pop('auth_type')
                credentials.append(params)
        else:
            result = repo.listCredentials(self.getUserRef(), self.getAuthType(), self.getUsername(), self.getToken())
            for doc in result:
                if doc.exists:
                    credential = Credential()
                    credential.from_firestore_document(doc)
                    params = credential.to_dict()
                    params['user_id'] = params['user'].id
                    params.pop('user')
                    params['auth_type_id'] = params['auth_type'].id
                    params.pop('auth_type')
                    credentials.append(params)

        return credentials
