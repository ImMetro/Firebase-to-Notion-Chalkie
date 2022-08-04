import requests
import json

url = "https://api.notion.com/v1/databases/b35659dddb6441d59683401712ff4916"

headers = {
    "Accept": "application/json",
    "Notion-Version": "2022-06-28",
    "Authorization": "Bearer secret_lwPqsWTSrfX3LZ4MdTiWFZUlKRX1WgPq6OpMGe9333a"
}

r = requests.get(url, headers=headers)

parsed = json.loads(r.text)
print(json.dumps(parsed, indent=4, sort_keys=True))