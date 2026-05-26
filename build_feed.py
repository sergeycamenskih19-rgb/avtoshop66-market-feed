python
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

# ========= НАСТРОЙКИ =========

INPUT_FILE = "258745.xlsx"

SHOP_NAME = "AvtoShop66"
SHOP_URL = "https://automotix.ru"

MARKUP = 5  # +400%

# ========= ЧТЕНИЕ EXCEL =========

df = pd.read_excel(INPUT_FILE)

# ========= XML ROOT =========

rss = ET.Element(
    "rss",
    {
        "version": "2.0",
        "xmlns:g": "http://base.google.com/ns/1.0"
    }
)

channel = ET.SubElement(rss, "channel")

ET.SubElement(channel, "title").text = SHOP_NAME
ET.SubElement(channel, "link").text = SHOP_URL
ET.SubElement(channel, "description").text = "Автозапчасти"

# ========= ТОВАРЫ =========

for index, row in df.iterrows():

    try:

        article = str(row.iloc[0])
        brand = str(row.iloc[1])
        name = str(row.iloc[2])

        price = float(row.iloc[3])

        final_price = int(price * MARKUP)

        item = ET.SubElement(channel, "item")

        ET.SubElement(
            item,
            "g:id"
        ).text = article

        ET.SubElement(
            item,
            "g:title"
        ).text = f"{brand} {name}"

        ET.SubElement(
            item,
            "g:description"
        ).text = f"{brand} {name}"

        ET.SubElement(
            item,
            "g:link"
        ).text = SHOP_URL

        ET.SubElement(
            item,
            "g:image_link"
        ).text = (
            "https://upload.wikimedia.org/"
            "wikipedia/commons/3/3f/"
            "Placeholder_view_vector.svg"
        )

        ET.SubElement(
            item,
            "g:availability"
        ).text = "in_stock"

        ET.SubElement(
            item,
            "g:price"
        ).text = f"{final_price} RUB"

        ET.SubElement(
            item,
            "g:condition"
        ).text = "new"

        ET.SubElement(
            item,
            "g:brand"
        ).text = brand

        ET.SubElement(
            item,
            "g:mpn"
        ).text = article

    except:
        continue

# ========= СОХРАНЕНИЕ =========

tree = ET.ElementTree(rss)

ET.indent(tree, space="  ", level=0)

with open("feed.xml", "wb") as f:

    tree.write(
        f,
        encoding="utf-8",
        xml_declaration=True
    )

print("feed.xml generated")
