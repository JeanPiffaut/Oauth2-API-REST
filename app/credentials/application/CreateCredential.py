from flask import abort

from app.credentials.domain.CredentialStructure import CredentialStructure
from app.credentials.interface.FirestoreRepository import CredentialRepository
from app.auth_types.interface.FirestoreRepository import AuthTypeRepository
from app.users.interface.FirestoreRepository import UserRepository


class CreateCredential(CredentialStructure):
    def setAuthTypeId(self, credential_auth_type_id):
        auth_repo = AuthTypeRepository()
        result = auth_repo.listAuthTypeById(credential_auth_type_id)
        if result.exists is False:
            abort(404, "Auth Type not found")

        self.setAuthTypeRef(result.reference)

    def setUserId(self, user_id):
        user_repo = UserRepository()
        result = user_repo.listUsersById(user_id)
        if result.exists is False:
            abort(404, "User not found")

        self.setUserRef(result.reference)

    def execute(self):
        cred_repo = CredentialRepository()
        return cred_repo.createCredential(self.to_dict())
