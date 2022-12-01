from app.users.domain.UserId import UserId
from app.users.domain.UserStructure import UserStructure
from app.users.interface.FirestoreRepository import UserRepository


class UpdateUser(UserStructure):

    def execute(self, fill_id):
        user_id = UserId(fill_id)
        if user_id.is_valid() is False:
            return False

        if self.name.is_valid() is False:
            return False

        if self.email.is_valid() is False:
            return False

        repo = UserRepository()
        return repo.updateUser(user_id.value, self.to_dict())
