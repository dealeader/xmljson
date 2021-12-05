import json
import xml.etree.ElementTree as ET
import requests

response = requests.get('https://lenta.ru/rss')

root = ET.fromstring(response.text)
json_container = []

for item in root.findall(r'./channel/item'):
    pubDate = item.findtext('pubDate')
    title = item.findtext('title')
    json_container.append(
        {
            'pubDate': pubDate,
            'title': title
        }
    )

with open('news.json', 'w', encoding='utf=8') as wf:
    json.dump(json_container, fp=wf, ensure_ascii=False, indent=4)