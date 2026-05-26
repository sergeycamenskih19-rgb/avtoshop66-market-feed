import os
import requests

TOKEN = os.getenv("MARKET_API_KEY")

url = "https://api.partner.market.yandex.ru/campaigns"

headers = {
    "Api-Key": TOKEN,
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0"
}

try:
    r = requests.get(
        url,
        headers=headers,
        timeout=60
    )

    print("STATUS:", r.status_code)
    print(r.text)

except Exception as e:
    print("ERROR:", e)
