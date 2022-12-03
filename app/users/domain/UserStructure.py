from flask_restful import abort

from app.common.domain.ModuleModel import ModuleModel
from app.users.domain.UserEmail import UserEmail
from app.users.domain.UserId import UserId
from app.users.domain.UserName import UserName


class UserStructure(ModuleModel):
    _id = UserId(None)
    _name = UserName(None)
    _email = UserEmail(None)

    def setId(self, user_id):
        self._id = UserId(user_id)
        if self._id.is_valid() is False:
            abort(400)

    def setName(self, user_name):
        self._name = UserName(user_name)
        if self._id.is_valid() is False:
            abort(400)

    def setEmail(self, user_email):
        self._email = UserEmail(user_email)
        if self._id.is_valid() is False:
            abort(400)

    def getId(self):
        return self._id.value

    def getName(self):
        return self._name.value

    def getEmail(self):
        return self._email.value

    def to_dict(self):
        user_id = self.getId()
        name = self.getName()
        email = self.getEmail()

        params = dict()

        if user_id is not None:
            params['id'] = user_id

        if name is not None:
            params['name'] = name

        if email is not None:
            params['email'] = email

        return params



