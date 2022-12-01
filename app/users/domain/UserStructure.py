from app.users.domain.UserEmail import UserEmail
from app.users.domain.UserId import UserId
from app.users.domain.UserName import UserName


class UserStructure:
    id: UserId = None
    name: UserName = None
    email: UserEmail = None

    def setId(self, user_id):
        self.id = UserId(user_id)

    def setName(self, user_name):
        self.name = UserName(user_name)

    def setEmail(self, user_email):
        self.email = UserEmail(user_email)

    def getId(self):
        if self.id is not None:
            return self.id.value
        else:
            return None

    def getName(self):
        if self.name is not None:
            return self.name.value
        else:
            return None

    def getEmail(self):
        if self.email is not None:
            return self.email.value
        else:
            return None

    def to_dict(self):
        user_dict = {}

        if self.id is not None:
            user_dict['id'] = self.getId()

        if self.name is not None:
            user_dict['name'] = self.getName()

        if self.email is not None:
            user_dict['email'] = self.getEmail()

        return user_dict
