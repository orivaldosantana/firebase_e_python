from firebase_init import db 
import json 


with open('./dados/json_turmas.json', 'r') as classes_file:
  classes_data = json.load(classes_file) 
  for c in classes_data:
    print(c['id_class']) 
    print(c) 
    doc_ref = db.collection(u'classes').document(c['id_class'])   
    doc_ref.set(c)
    print("Adding with success!!!\n\n") 