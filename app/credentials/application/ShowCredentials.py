from app.credentials.domain.CredentialStructure import CredentialStructure
from app.credentials.interface.FirestoreRepository import CredentialRepository


class ShowCredentials(CredentialStructure):

    def execute(self, fill_id=None):
        repo = CredentialRepository()
