from app.common.domain.RepositoryModel import RepositoryModel
from config.firestore import fr


class CredentialRepository(RepositoryModel):
    collection = 'Credentials'
