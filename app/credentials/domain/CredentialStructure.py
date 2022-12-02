from app.auth_types.domain.AuthTypeId import AuthTypeId
from app.credentials.domain.CredentialId import CredentialId
from app.credentials.domain.CredentialToken import CredentialToken
from app.credentials.domain.CredentialUsername import CredentialUsername
from app.users.domain.UserId import UserId


class CredentialStructure:
    _id: CredentialId = None
    _user_id: UserId = None
    _auth_type_id: AuthTypeId = None
    _username: CredentialUsername = None
    _token: CredentialToken = None

    def setId(self, credential_id):
        self._id = CredentialId(credential_id)

    def setUserId(self, credential_user_id):
        self._user_id = UserId(credential_user_id)

    def setAuthTypeId(self, credential_auth_type_id):
        self._auth_type_id = AuthTypeId(credential_auth_type_id)

    def setUsername(self, credential_username):
        self._username = CredentialUsername(credential_username)

    def setToken(self, credential_token):
        self._token = CredentialToken(credential_token)

    def getId(self):
        return self._id.value

    def getUserId(self):
        return self._user_id.value

    def getAuthTypeId(self):
        return self._auth_type_id.value

    def getUsername(self):
        return self._username.value

    def getToken(self):
        return self._token.value

    def to_dict(self):
        structure_dict = {}

        if self._id is not None:
            structure_dict['id'] = self.getId()

        if self._user_id is not None:
            structure_dict['user_id'] = self.getUserId()

        if self._auth_type_id is not None:
            structure_dict['auth_type_id'] = self.getAuthTypeId()

        if self._username is not None:
            structure_dict['username'] = self.getUsername()

        if self._token is not None:
            structure_dict['token'] = self.getToken()

        return structure_dict
