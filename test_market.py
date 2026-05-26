import requests

TOKEN = "ACMA:LSxK4GcZmXVI8vVBE9c9RhRttqN1Qv6vCtMcLeFs:13e575ed"

headers = {
    "Api-Key": 5f11f103349aaf7a664cc9f9eaf89349
}

url = "https://api.partner.market.yandex.ru/campaigns"

r = requests.get(url, headers=headers)

print(r.status_code)
print(r.text)
