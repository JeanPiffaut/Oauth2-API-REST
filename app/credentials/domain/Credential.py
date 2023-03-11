from app.credentials.domain.CredentialStructure import CredentialStructure


class Credential(CredentialStructure):
    def from_firestore_document(self, document):
        self.setId(document.id)
        self.setUserId(document.get('user_id'))
        self.setAuthTypeRef(document.get('auth_type'))
        self.setUsername(document.get('username'))
        self.setToken(document.get('token'))
