from app.auth_types.domain.AuthTypeStructure import AuthTypeStructure


class AuthType(AuthTypeStructure):
    def from_firestore_document(self, document):
        self.setId(document.id)
        self.setName(document.get('name'))
        self.setClientId(document.get('client_id'))
        self.setClientSecret(document.get('client_secret'))

    def from_dict(self, dict_setter):
        self.setId(dict_setter['id'])
        self.setName(dict_setter['name'])
        self.setClientId(dict_setter['client_id'])
        self.setClientSecret(dict_setter['client_secret'])
