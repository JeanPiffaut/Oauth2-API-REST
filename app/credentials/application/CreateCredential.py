from app.credentials.domain.CredentialStructure import CredentialStructure
from app.credentials.interface.FirestoreRepository import CredentialRepository


class CreateCredential(CredentialStructure):
    def execute(self):
        cred_repo = CredentialRepository()
        return cred_repo.createCredential(self.to_dict())
