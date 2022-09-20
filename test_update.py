from firebase_init import db 

doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Adaa',
    u'last': u'Lovelace',
    u'born': 1815
})

# Update https://firebase.google.com/docs/firestore/manage-data/add-data#update-data  
doc_ref.update({
    u'test': 2013,
})
