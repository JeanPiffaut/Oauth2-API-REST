from app.common.domain.ModelBase import ModelBase
from app.credentials.domain import CredentialId, CredentialUsername, CredentialToken
from app.users.domain import UserId


class Credential(ModelBase):
    _id: CredentialId
    _user_id: UserId
    _username: CredentialUsername
    _token: CredentialToken

    def setId(self, credential_id: CredentialId):
        self._id = credential_id

    def setUserId(self, user_id: UserId):
        self._user_id = user_id

    def setUsername(self, credential_username: CredentialUsername):
        self._username = credential_username

    def setToken(self, credential_token: CredentialToken):
        self._token = credential_token
