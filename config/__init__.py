import os

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"
GOOGLE_APPLICATION_CREDENTIALS = "venv/oauth-2-api-rest-9c6505cc1a30.json"
TOKEN_LIFE_TIME = "8000"
TIMEZONE = "America/Santiago"
