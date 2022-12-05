from flask import abort

from app.common.domain.RepositoryModel import RepositoryModel
from config.firestore import fr


class CredentialRepository(RepositoryModel):
    _collection = 'Credentials'
