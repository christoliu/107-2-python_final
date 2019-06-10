import json
import datetime
import requests

item_list =[]
fuk = datetime.datetime.now()
time = str(datetime.datetime.now().isoformat('T'))+'Z'
jf = {'nextPageToken': ''}
for i in range(0, 6):
    PT = jf['nextPageToken']
    my_params = {
        'part': 'snippet',
        'channelId': 'UCpu3bemTQwAU8PqM4kJdoEQ',
        'maxResults': '50',
        'order': 'date',
        'pageToken': PT,
        'publishedBefore': time,
        'q': '韓國瑜',
        'key': 'AIzaSyA626qXLy1ZOPeB0wDy9-YoR0TB4HwP_7A'
    }
    res = requests.get('https://www.googleapis.com/youtube/v3/search', params = my_params)
    res.json()
    jf = json.loads(res.text)
    for i in jf['items']:
        item = {'videoId': i['id']['videoId'], 'publishedAt': i['snippet']['publishedAt'], 'title': i['snippet']['title'], 'description': i['snippet']['description']}
        item_list.append(item)
with open('FaDaChoi.json', 'w') as f:
    f.write(json.dumps(item_list, ensure_ascii=False))
print(datetime.datetime.now() - fuk)