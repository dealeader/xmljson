import json
import xml.etree.ElementTree as ET
import requests

response = requests.get('https://lenta.ru/rss')

root = ET.fromstring(response.text)
json_container = []

for item in root.findall(r'./channel/item'):
    item_container = {}
    for child in item: 
        item_container[child.tag] = child.text
    json_container.append(item_container)

with open('news2.json', 'w', encoding='utf=8') as wf:
    json.dump(json_container, fp=wf, ensure_ascii=False, indent=4, sort_keys=True)