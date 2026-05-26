import requests

url = "https://api.rossko.ru/service/v2/GetSearch"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json"
}

payload = {
    "KEY1": "your_key1",
    "KEY2": "your_key2",
    "text": "filter"
}

try:
    r = requests.post(url, json=payload, headers=headers, timeout=30)
    print("STATUS:", r.status_code)
    print(r.text[:1000])
except Exception as e:
    print("ERROR:", e)
