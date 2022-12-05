from flask import abort

from app.auth_types.interface.FirestoreRepository import AuthTypeRepository
from app.credentials.domain.CredentialStructure import CredentialStructure
from app.credentials.interface.FirestoreRepository import CredentialRepository
from app.users.interface.FirestoreRepository import UserRepository


class CreateCredential(CredentialStructure):
    def execute(self):
        auth_repo = AuthTypeRepository()
        auth_list = auth_repo.listAuthTypeById(self.getAuthTypeId())
        if auth_list.exists is False:
            abort(400)

        user_repo = UserRepository()
        user_list = user_repo.listUsersById(self.getUserId())
        if user_list.exists is False:
            abort(400)

        cred_repo = CredentialRepository()
        return cred_repo.createCredential(self.to_dict())
