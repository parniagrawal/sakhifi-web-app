import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('sakhifi-14b0f-firebase-adminsdk-fbsvc-fd215c1d67.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
