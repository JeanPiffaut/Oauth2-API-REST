from decouple import config

from app.credentials.domain.CredentialStructure import CredentialStructure
from app.credentials.interface.FirestoreRepository import CredentialRepository


class ValidateCredentials(CredentialStructure):
    def execute(self, username, token, auth_type="main_auth_type"):
        if auth_type == config('DEFAULT_AUTH_TYPE'):
            token = self.setPassword(token)

        self.setUsername(username)
        self.setToken(token)

        credential_repo = CredentialRepository()
        credentials = credential_repo.listCredentials(fill_username=self.getUsername(), fill_token=self.getToken())
        for doc in credentials:
            if doc.exists:
                return doc.to_dict()
            else:
                return False

        return False
