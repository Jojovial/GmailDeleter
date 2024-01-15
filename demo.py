import time
from google_apis import create_service

CLIENT_FILE = 'client-secret.json'
API_NAME ='gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

gmail_service = create_service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)

#step 1.Search emails
