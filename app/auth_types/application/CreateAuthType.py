from app.auth_types.domain.AuthTypeStructure import AuthTypeStructure
from app.auth_types.interface.FirestoreRepository import AuthTypeRepository


class CreateAuthType(AuthTypeStructure):

    def execute(self):
        repo = AuthTypeRepository()
        return repo.createAuthType(self.to_dict())
