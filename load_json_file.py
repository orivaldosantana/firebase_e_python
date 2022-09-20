from firebase_init import db 

# https://www.freecodecamp.org/news/python-parse-json-how-to-read-a-json-file/

import json 

with open('./dados/json_turmas.json', 'r') as classes_file:
  classes_data = json.load(classes_file) 
  for c in classes_data:
    print(c) 


