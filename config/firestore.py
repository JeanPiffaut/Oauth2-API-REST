import os

from google.cloud import firestore
print(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))
fr = firestore.Client.from_service_account_json(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))
