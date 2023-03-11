from flask import abort

from app.common.domain.ModuleModel import ModuleModel
from app.credentials.domain.AuthTypeRef import AuthTypeRef
from app.credentials.domain.CredentialId import CredentialId
from app.credentials.domain.CredentialToken import CredentialToken
from app.credentials.domain.CredentialUsername import CredentialUsername
from app.credentials.domain.UserRef import UserRef


class CredentialStructure(ModuleModel):
    _id = CredentialId(None)
    _user = UserRef(None)
    _auth_type = AuthTypeRef(None)
    _username = CredentialUsername(None)
    _token = CredentialToken(None)

    def setId(self, credential_id):
        self._id = CredentialId(credential_id)
        if self._id.is_valid() is False:
            abort(400)

    def setUserRef(self, credential_user_id):
        self._user = UserRef(credential_user_id)

    def setAuthTypeRef(self, credential_auth_type_id):
        self._auth_type = AuthTypeRef(credential_auth_type_id)

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

    def getUserRef(self):
        return self._user.value

    def getAuthTypeRef(self):
        return self._auth_type.value

    def getUsername(self):
        return self._username.value

    def getToken(self):
        return self._token.value

    def to_dict(self):
        credential_id = self.getId()
        user = self.getUserRef()
        auth_type = self.getAuthTypeRef()
        username = self.getUsername()
        token = self.getToken()

        params = dict()

        if credential_id is not None:
            params['id'] = credential_id

        if user is not None:
            params['user'] = user

        if auth_type is not None:
            params['auth_type'] = auth_type

        if username is not None:
            params['username'] = username

        if token is not None:
            params['token'] = token

        return params
