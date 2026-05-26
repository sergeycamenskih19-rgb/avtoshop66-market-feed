import os
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

API_KEY1 = os.getenv("API_KEY1")
API_KEY2 = os.getenv("API_KEY2")

root = ET.Element("yml_catalog")
root.set("date", datetime.now().strftime("%Y-%m-%d %H:%M"))

shop = ET.SubElement(root, "shop")

ET.SubElement(shop, "name").text = "AvtoShop66"
ET.SubElement(shop, "company").text = "AvtoShop66"
ET.SubElement(shop, "url").text = "https://automotix.ru"

currencies = ET.SubElement(shop, "currencies")

currency = ET.SubElement(currencies, "currency")
currency.set("id", "RUR")
currency.set("rate", "1")

categories = ET.SubElement(shop, "categories")

cat = ET.SubElement(categories, "category")
cat.set("id", "1")
cat.text = "Автозапчасти"

offers = ET.SubElement(shop, "offers")

offer = ET.SubElement(offers, "offer")
offer.set("id", "TEST-001")
offer.set("available", "true")

ET.SubElement(offer, "name").text = "Тестовый товар"
ET.SubElement(offer, "vendor").text = "AvtoShop66"
ET.SubElement(offer, "price").text = "9990"
ET.SubElement(offer, "currencyId").text = "RUR"
ET.SubElement(offer, "categoryId").text = "1"

ET.SubElement(offer, "description").text = "Тестовая выгрузка"

tree = ET.ElementTree(root)

tree.write(
    "feed.yml",
    encoding="utf-8",
    xml_declaration=True
)

print("feed.yml generated")
