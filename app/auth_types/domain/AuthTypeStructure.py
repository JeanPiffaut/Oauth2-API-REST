from flask import abort

from app.auth_types.domain.AuthTypeClientId import AuthTypeClientId
from app.auth_types.domain.AuthTypeClientSecret import AuthTypeClientSecret
from app.auth_types.domain.AuthTypeId import AuthTypeId
from app.auth_types.domain.AuthTypeName import AuthTypeName
from app.common.domain.ModuleModel import ModuleModel


class AuthTypeStructure(ModuleModel):
    _id = AuthTypeId(None)
    _name = AuthTypeName(None)
    _client_id = AuthTypeClientId(None)
    _client_secret = AuthTypeClientSecret(None)

    def setId(self, auth_type_id):
        self._id = AuthTypeId(auth_type_id)
        if self._id.is_valid() is False:
            abort(400)

    def setName(self, auth_type_name):
        self._name = AuthTypeName(auth_type_name)
        if self._name.is_valid() is False:
            abort(400)

    def setClientId(self, auth_type_client_id):
        self._client_id = AuthTypeClientId(auth_type_client_id)
        if self._client_id.is_valid() is False:
            abort(400)

    def setClientSecret(self, auth_type_client_secret):
        self._client_secret = AuthTypeClientSecret(auth_type_client_secret)
        if self._client_secret.is_valid() is False:
            abort(400)

    def getId(self):
        return self._id.value

    def getName(self):
        return self._name.value

    def getClientId(self):
        return self._client_id.value

    def getClientSecret(self):
        return self._client_secret.value

    def to_dict(self):
        auth_id = self.getId()
        name = self.getName()
        client_id = self.getClientId()
        client_secret = self.getClientSecret()

        params = dict()

        if auth_id is not None:
            params['id'] = auth_id

        if name is not None:
            params['name'] = name

        if client_id is not None:
            params['client_id'] = client_id

        if client_secret is not None:
            params['client_secret'] = client_secret

        return params
