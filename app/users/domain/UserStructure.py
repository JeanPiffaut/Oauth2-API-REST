from flask_restful import abort

from app.common.domain.ModuleModel import ModuleModel
from app.users.domain.UserEmail import UserEmail
from app.users.domain.UserId import UserId
from app.users.domain.UserName import UserName


class UserStructure(ModuleModel):
    id = UserId(None)
    name = UserName(None)
    email = UserEmail(None)

    def setId(self, user_id):
        self.id = UserId(user_id)
        if self.id.is_valid() is False:
            abort(400)

    def setName(self, user_name):
        self.name = UserName(user_name)
        if self.id.is_valid() is False:
            abort(400)

    def setEmail(self, user_email):
        self.email = UserEmail(user_email)
        if self.id.is_valid() is False:
            abort(400)

    def getId(self):
        return self.id.value

    def getName(self):
        return self.name.value

    def getEmail(self):
        return self.email.value
