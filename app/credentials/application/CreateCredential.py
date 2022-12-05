from app.credentials.domain.CredentialStructure import CredentialStructure
from app.credentials.interface.FirestoreRepository import CredentialRepository


class CreateCredential(CredentialStructure):
    def execute(self):
        repo = CredentialRepository()
        return repo.createCredential(self.to_dict())
