import pandas as pd
import xml.etree.ElementTree as ET
import re

FILE = "258745.xlsx"
OUTPUT = "feed.xml"

def clean(value):
    if pd.isna(value):
        return ""
    return str(value).strip()

def safe_price(value):
    try:
        return f"{float(str(value).replace(',', '.')):.2f} RUB"
    except:
        return "0.00 RUB"

df = pd.read_excel(FILE)

rss = ET.Element("rss", version="2.0", attrib={
    "xmlns:g": "http://base.google.com/ns/1.0"
})

channel = ET.SubElement(rss, "channel")
ET.SubElement(channel, "title").text = "AvtoShop66"
ET.SubElement(channel, "link").text = "https://automotix.ru"
ET.SubElement(channel, "description").text = "Автозапчасти"

for i, row in df.iterrows():

    item = ET.SubElement(channel, "item")

    ET.SubElement(item, "g:id").text = clean(row.get("id", f"SKU-{i}"))
    ET.SubElement(item, "g:title").text = clean(row.get("title", "Автозапчасть"))
    ET.SubElement(item, "g:description").text = clean(row.get("description", "Описание отсутствует"))

    ET.SubElement(item, "g:link").text = clean(row.get("link", "https://automotix.ru"))

    image = clean(row.get("image_link", ""))
    if not image or image.endswith(".svg"):
        image = "https://automotix.ru/no-image.jpg"
    ET.SubElement(item, "g:image_link").text = image

    ET.SubElement(item, "g:availability").text = "in_stock"
    ET.SubElement(item, "g:price").text = safe_price(row.get("price", 0))
    ET.SubElement(item, "g:condition").text = "new"

    ET.SubElement(item, "g:brand").text = clean(row.get("brand", "Unknown"))
    ET.SubElement(item, "g:mpn").text = clean(row.get("mpn", ""))

tree = ET.ElementTree(rss)
tree.write(OUTPUT, encoding="utf-8", xml_declaration=True)

print("✅ feed.xml успешно создан")
