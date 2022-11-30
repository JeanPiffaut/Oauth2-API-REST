from app.users.domain import UserId, UserName, UserEmail


class User:
    _id: UserId
    _name: UserName
    _email: UserEmail

    def setId(self, user_id: UserId):
        self._id = user_id

    def setName(self, user_name: UserName):
        self._name = user_name

    def setEmail(self, user_email: UserEmail):
        self._email = user_email

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getEmail(self):
        return self._email
