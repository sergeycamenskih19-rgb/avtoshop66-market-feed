import os
import requests

TOKEN = os.getenv("ACMA:LSxK4GcZmXVI8vVBE9c9RhRttqN1Qv6vCtMcLeFs:13e575ed")
CAMPAIGN_ID = os.getenv("147507763")

url = f"https://api.partner.market.yandex.ru/businesses/{CAMPAIGN_ID}/offer-mappings/update"

headers = {
    "Api-Key": 5f11f103349aaf7a664cc9f9eaf89349,
    "Content-Type": "application/json"
}

payload = {
    "offerMappings": [
        {
            "offer": {
                "shopSku": "TEST-001",
                "name": "FEBEST Ступица колеса",
                "category": "Автозапчасти",
                "vendor": "FEBEST"
            }
        }
    ]
}

r = requests.post(
    url,
    headers=headers,
    json=payload
)

print(r.status_code)
print(r.text)
