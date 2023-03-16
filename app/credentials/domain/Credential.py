from app.credentials.domain.CredentialStructure import CredentialStructure


class Credential(CredentialStructure):
    def from_firestore_document(self, document):
        self.setId(document.id)
        self.setUserRef(document.get('user'))
        self.setAuthType(document.get('auth_type'))
        self.setUsername(document.get('username'))
        self.setToken(document.get('token'))
