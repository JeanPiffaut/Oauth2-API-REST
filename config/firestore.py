from decouple import config
from google.cloud import firestore

fr = firestore.Client.from_service_account_json(config('GOOGLE_APPLICATION_CREDENTIALS'))