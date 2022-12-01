from app.auth_types.domain import AuthTypeId
from app.common.domain.ModelBase import ModelBase
from app.credentials.domain import CredentialId, CredentialUsername, CredentialToken
from app.users.domain import UserId


class Credential(ModelBase):
    _id: CredentialId
    _user_id: UserId
    _auth_type_id: AuthTypeId
    _username: CredentialUsername
    _token: CredentialToken

    def setId(self, credential_id: CredentialId):
        self._id = credential_id

    def setUserId(self, user_id: UserId):
        self._user_id = user_id

    def setAuthTypeId(self, auth_type_id: AuthTypeId):
        self._auth_type_id = auth_type_id

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
