from app.auth_types.domain.AuthTypeClientId import AuthTypeClientId
from app.auth_types.domain.AuthTypeClientSecret import AuthTypeClientSecret
from app.auth_types.domain.AuthTypeId import AuthTypeId
from app.auth_types.domain.AuthTypeName import AuthTypeName
from app.common.domain.ModuleModel import ModuleModel


class AuthTypeStructure(ModuleModel):
    _id: AuthTypeId = None
    _name: AuthTypeName = None
    _client_id: AuthTypeClientId = None
    _client_secret: AuthTypeClientSecret = None

    def setId(self, auth_type_id):
        self._id = AuthTypeId(auth_type_id)

    def setName(self, auth_type_name):
        self._name = AuthTypeName(auth_type_name)

    def setClientId(self, auth_type_client_id):
        self._client_id = AuthTypeClientId(auth_type_client_id)

    def setClientSecret(self, auth_type_client_secret):
        self._client_secret = AuthTypeClientSecret(auth_type_client_secret)

    def getId(self):
        return self._id.value

    def getName(self):
        return self._name.value

    def getClientId(self):
        return self._client_id.value

    def getClientSecret(self):
        return self._client_secret.value
