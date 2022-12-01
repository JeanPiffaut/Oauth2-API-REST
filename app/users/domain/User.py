from app.users.domain.UserStructure import UserStructure


class User(UserStructure):

    def from_firestore_document(self, document):
        self.setId(document.id)
        self.setName(document.get('name'))
        self.setEmail(document.get('email'))

    def from_dict(self, dict_setter):
        self.setId(dict_setter['id'])
        self.setName(dict_setter['name'])
        self.setEmail(dict_setter['email'])
