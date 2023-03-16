from flask import abort

from app.credentials.domain.CredentialId import CredentialId
from app.credentials.domain.CredentialStructure import CredentialStructure
from app.credentials.interface.FirestoreRepository import CredentialRepository
from app.users.interface.FirestoreRepository import UserRepository


class UpdateCredential(CredentialStructure):
    def setUserId(self, user_id):
        user_repo = UserRepository()
        result = user_repo.listUsersById(user_id)
        if result.exists is False:
            abort(404, "User not found")

        self.setUserRef(result.reference)

    def execute(self, fill_id):
        credential_id = CredentialId(fill_id)
        if credential_id.is_valid() is False:
            abort(400)

        repo = CredentialRepository()
        return repo.updateCredential(credential_id.value, self.to_dict())
