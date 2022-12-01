from app.common.domain.ModuleModel import ModuleModel
from app.auth_types.domain import AuthTypeId, AuthTypeName, AuthTypeClientId, AuthTypeClientSecret


class AuthType(ModuleModel):
    _id: AuthTypeId = None
    _name: AuthTypeName = None
    _client_id: AuthTypeClientId = None
    _client_secret: AuthTypeClientSecret = None

    def setId(self, auth_type_id: AuthTypeId):
        self._id = auth_type_id

    def setName(self, auth_type_name: AuthTypeName):
        self._name = auth_type_name

    def setClientId(self, auth_type_client_id: AuthTypeClientId):
        self._client_id = auth_type_client_id

    def setClientSecret(self, auth_type_client_secret: AuthTypeClientSecret):
        self._client_secret = auth_type_client_secret

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getClientId(self):
        return self._client_id

    def getClientSecret(self):
        return self._client_secret
