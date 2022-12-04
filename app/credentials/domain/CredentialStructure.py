from flask import abort

from app.auth_types.domain.AuthTypeId import AuthTypeId
from app.common.domain.ModuleModel import ModuleModel
from app.credentials.domain.CredentialId import CredentialId
from app.credentials.domain.CredentialToken import CredentialToken
from app.credentials.domain.CredentialUsername import CredentialUsername
from app.users.domain.UserId import UserId


class CredentialStructure(ModuleModel):
    _id = CredentialId(None)
    _user_id = UserId(None)
    _auth_type_id = AuthTypeId(None)
    _username = CredentialUsername(None)
    _token = CredentialToken(None)

    def setId(self, credential_id):
        self._id = CredentialId(credential_id)
        if self._id.is_valid() is False:
            abort(400)

    def setUserId(self, credential_user_id):
        self._user_id = UserId(credential_user_id)
        if self._user_id.is_valid() is False:
            abort(400)

    def setAuthTypeId(self, credential_auth_type_id):
        self._auth_type_id = AuthTypeId(credential_auth_type_id)
        if self._auth_type_id.is_valid() is False:
            abort(400)

    def setUsername(self, credential_username):
        self._username = CredentialUsername(credential_username)
        if self._username.is_valid() is False:
            abort(400)

    def setToken(self, credential_token):
        self._token = CredentialToken(credential_token)
        if self._token.is_valid() is False:
            abort(400)

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
        credential_id = self.getId()
        user_id = self.getUserId()
        auth_id = self.getAuthTypeId()
        username = self.getUsername()
        token = self.getToken()

        params = dict()

        if credential_id is not None:
            params['id'] = credential_id

        if user_id is not None:
            params['user_id'] = user_id

        if auth_id is not None:
            params['auth_type_id'] = auth_id

        if username is not None:
            params['username'] = username

        if token is not None:
            params['token'] = token

        return params
