import os
import requests

API_URL = "https://api.rossko.ru/service/v2/GetSearch"

payload = {
    "KEY1": os.getenv("API_KEY1"),
    "KEY2": os.getenv("API_KEY2"),
    "text": "filter"
}

r = requests.post(API_URL, json=payload)

print(r.status_code)
print(r.text[:1000])
