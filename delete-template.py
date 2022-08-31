import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#get_info = {}
counter = 0
cred_obj = credentials.Certificate('service-account-staging.json')
default_app = firebase_admin.initialize_app(cred_obj)

db = firestore.client()

# Get info from selected template from input value
info = db.collection('Template').get()

for i in info:
    template_id = i
    i = i.to_dict()
    if (i['subscriber_no'] == 0 and i['owner'] == ''):
        print(f'No owner and subscribers, deleting: {template_id.id}')
        db.collection('Template').document(template_id).delete()
    else:
        print(f'Contains either owner or subscribers: {template_id.id}')
