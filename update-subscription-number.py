import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


input = input("Enter the template id that you would like to change: ")

#get_info = {}
counter = 0
cred_obj = credentials.Certificate('service-account-staging.json')
default_app = firebase_admin.initialize_app(cred_obj)

db = firestore.client()

# Get info from selected template from input value
info = db.collection('Template').document(input).get().to_dict()

subscriberNo = info['subscriber_no']

db.collection('Template').document(input).update({"subscriber_no": subscriberNo + 1})
print(f'Updated Subscriber Number from {subscriberNo} to {subscriberNo + 1} --- Template id: {input}')

#todo 
# Template in Firestore
# PUT/DELETE
# Url variable in easier to do in Flask