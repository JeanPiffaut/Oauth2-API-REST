from app.users.domain import UserId, UserName, UserEmail


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
        return {
            'id': self.getId(),
            'name': self.getName(),
            'email': self.getEmail()
        }
