from app.auth_types.domain import AuthTypeId
from app.common.domain.ModuleModel import ModuleModel
from app.credentials.domain import CredentialId, CredentialUsername, CredentialToken
from app.users.domain import UserId


class Credential(ModuleModel):
    _id: CredentialId = None
    _user_id: UserId = None
    _auth_type_id: AuthTypeId = None
    _username: CredentialUsername = None
    _token: CredentialToken = None

    def setId(self, credential_id: CredentialId):
        self._id = credential_id

    def setUserId(self, credential_user_id: UserId):
        self._user_id = credential_user_id

    def setAuthTypeId(self, credential_auth_type_id: AuthTypeId):
        self._auth_type_id = credential_auth_type_id

    def setUsername(self, credential_username: CredentialUsername):
        self._username = credential_username

    def setToken(self, credential_token: CredentialToken):
        self._token = credential_token

    def getId(self):
        return self._id

    def getUserId(self):
        return self._user_id

    def getAuthTypeId(self):
        return self._auth_type_id

    def getUsername(self):
        return self._username

    def getToken(self):
        return self._token
