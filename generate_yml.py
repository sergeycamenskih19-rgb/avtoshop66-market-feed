```python id="k9x7q2"
import os
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

# ====================================
# API KEYS
# ====================================

API_KEY1 = os.getenv("API_KEY1")
API_KEY2 = os.getenv("API_KEY2")

# ====================================
# НАСТРОЙКИ
# ====================================

SHOP_NAME = "AvtoShop66"
SHOP_URL = "https://automotix.ru"

# Наценка +400%
MARKUP = 5

# ====================================
# ROOT XML
# ====================================

root = ET.Element("yml_catalog")
root.set("date", datetime.now().strftime("%Y-%m-%d %H:%M"))

shop = ET.SubElement(root, "shop")

ET.SubElement(shop, "name").text = SHOP_NAME
ET.SubElement(shop, "company").text = SHOP_NAME
ET.SubElement(shop, "url").text = SHOP_URL

# ====================================
# CURRENCIES
# ====================================

currencies = ET.SubElement(shop, "currencies")

currency = ET.SubElement(currencies, "currency")
currency.set("id", "RUR")
currency.set("rate", "1")

# ====================================
# CATEGORIES
# ====================================

categories = ET.SubElement(shop, "categories")

category = ET.SubElement(categories, "category")
category.set("id", "1")
category.text = "Автозапчасти"

# ====================================
# OFFERS
# ====================================

offers = ET.SubElement(shop, "offers")

# ====================================
# ТЕСТОВЫЕ ТОВАРЫ
# (пока вместо Rossko)
# ====================================

products = [
    {
        "article": "2182-FOCMF",
        "brand": "FEBEST",
        "name": "Ступица колеса",
        "price": 2500
    },
    {
        "article": "HU7020Z",
        "brand": "MANN",
        "name": "Масляный фильтр",
        "price": 1200
    },
    {
        "article": "0986AF1111",
        "brand": "BOSCH",
        "name": "Тормозные колодки",
        "price": 3200
    }
]

for item in products:

    # Наценка +400%
    final_price = int(item["price"] * MARKUP)

    offer = ET.SubElement(offers, "offer")

    offer.set("id", item["article"])
    offer.set("available", "true")

    ET.SubElement(
        offer,
        "name"
    ).text = f'{item["brand"]} {item["name"]}'

    ET.SubElement(
        offer,
        "vendor"
    ).text = item["brand"]

    ET.SubElement(
        offer,
        "price"
    ).text = str(final_price)

    ET.SubElement(
        offer,
        "currencyId"
    ).text = "RUR"

    ET.SubElement(
        offer,
        "categoryId"
    ).text = "1"

    ET.SubElement(
        offer,
        "description"
    ).text = (
        f'{item["brand"]} '
        f'{item["name"]}. '
        f'Оригинальная автозапчасть.'
    )

tree = ET.ElementTree(root)

tree.write(
    "feed.yml",
    encoding="utf-8",
    xml_declaration=True
)

print("feed.yml generated")
```
