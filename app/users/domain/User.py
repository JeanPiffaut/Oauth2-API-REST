from app.users.domain.UserEmail import UserEmail
from app.users.domain.UserId import UserId
from app.users.domain.UserName import UserName


class User:
    id: UserId = None
    name: UserName = None
    email: UserEmail = None

    def setId(self, user_id: UserId):
        self.id = user_id

    def setName(self, user_name: UserName):
        self.name = user_name

    def setEmail(self, user_email: UserEmail):
        self.email = user_email

    def getId(self):
        return self.id.value

    def getName(self):
        return self.name.value

    def getEmail(self):
        return self.email.value

    def to_dict(self):
        user_dict = {}

        if self.id is not None:
            user_dict['id'] = self.getId()

        if self.name is not None:
            user_dict['name'] = self.getName()

        if self.email is not None:
            user_dict['email'] = self.getEmail()

        return user_dict

    def from_firestore_document(self, document):
        self.setId(UserId(document.id))
        self.setName(UserName(document.get('name')))
        self.setEmail(UserEmail(document.get('email')))

    def from_dict(self, dict_setter):
        self.setId(UserId(dict_setter['id']))
        self.setName(UserName(dict_setter['name']))
        self.setEmail(UserEmail(dict_setter['email']))
