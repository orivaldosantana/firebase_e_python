# fonte: https://firebase.google.com/docs/firestore/quickstart#python 



import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('dataviewer-dev-credentials.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()


doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Adaa',
    u'last': u'Lovelace',
    u'born': 1815
})