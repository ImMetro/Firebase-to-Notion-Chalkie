import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

to_sort = {}
counter = 0
sorted_list = []
cred_obj = credentials.Certificate('serviceAccountKey.json')
default_app = firebase_admin.initialize_app(cred_obj)

db = firestore.client()

info = db.collection('User').get()

for i in info:
    to_sort[counter] = i.to_dict()
    counter += 1

with open("data.json", "w") as file:
    json.dump(to_sort, file, indent=4, sort_keys=True)
file.close()

with open("data.json", "r") as file:
    to_sort = json.load(file)
file.close()

for i in range(0, len(to_sort)):
    temp = []
    temp.append(to_sort[f'{i}']['name'])
    temp.append(to_sort[f'{i}']['email'])
    temp.append(to_sort[f'{i}']['university_email'])
    if (to_sort[f'{i}']['name'] == "The Australian National University"):
        temp.append("ANU")
    else:
        temp.append("ANU")
    a = to_sort[f'{i}']['degree']
    a = json.dumps(a)
    if "name" in a:
        a = a.strip(" '[{:,")
        a = a.split("name")[1]
        a = a.split('"}')[0]
        a = a.strip('": ')
        temp.append(a)
    else:
        temp.append("N/A")
    temp.append(to_sort[f'{i}']['image_url'])
    sorted_list.append(temp)

for i in range(len(sorted_list)):

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        "Authorization": "Bearer secret_lwPqsWTSrfX3LZ4MdTiWFZUlKRX1WgPq6OpMGe9333a"
    }

    payload = {"page_size": 100,
    "filter": {
        "or": [{
            "property": "Name",
            "title": {
                "contains": sorted_list[i][0]
            }
        }]
    }}

    test_exist = requests.post("https://api.notion.com/v1/databases/redaccted/query", json=payload, headers=headers)
    if (test_exist.status_code != 200):
        print(f'Error, API Code Status code: {test_exist.status_code}')
    if (('"results":[]' not in test_exist.text)):
        print(f'{sorted_list[i][0]} already exists in the database, skipping...')
    else:
        url = "https://api.notion.com/v1/pages"
        payload = {
            "parent": {"database_id": "b35659dddb6441d59683401712ff4916"},
            "properties": {
                "Name": {
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": sorted_list[i][0]
                            }
                        }
                    ]
                },
                "Personal email": {
                    "email": sorted_list[i][1]
                },
                "University email": {
                    "email": sorted_list[i][2]
                },
                "University": {
                    "select": {
                        "name": sorted_list[i][3]
                    }
                },
                "Degrees": {
                    "multi_select": [
                        {
                            "name": sorted_list[i][4]
                        }
                    ]
                }
            },
            "icon": {
                "type": "external",
                "external": {
                    "url": sorted_list[i][5]
                }
            }
        }
        response = requests.post(url, json=payload, headers=headers)

        print("Piping: ",sorted_list[i][0],sorted_list[i][1],sorted_list[i][2],sorted_list[i][3],sorted_list[i][4],"into Notion DB")

r = requests.get('https://app.chequptime.com/webhook-heartbeat/e7ed982dba54caf7cb498c2ca31bed86')
print(r.status_code)