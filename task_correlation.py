import requests
from itertools import groupby

url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500'

response = requests.get(url, params= { 'titles':'Бельмондо, Жан-Поль'}).json()

revisions = response['query']['pages']['192203']['revisions']
for key, group in groupby(revisions, key=lambda item: item['timestamp'][:item['timestamp'].index('T')]):
    print(f"{key} {len(list(group))}")

# 6 сентября - наибольшее количество правок, соответствует дню смерти, такой метрикой можно пользоваться.