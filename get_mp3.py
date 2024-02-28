import requests
from bs4 import BeautifulSoup
import json
import time

search = "Jambo Jambo Jambo"

req = search.split(' ')
text = ''
for i in req:
    text += i + '%20'

url_101 = f'https://101.ru/search/category/tracks/q/{text[0:-3]}'
headers = {
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) "
                  "AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
}
r = requests.get(url_101, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser').findAll("li", class_="grid__item")

for i in soup:
    try:
        print(i.find('audio').attrs.get('data-title'), '-', i.find('audio').attrs.get('data-track'))
        print(i.findAll('meta')[0].attrs.get('content'))
        print(i.findAll('meta')[1].attrs.get('content'))
        print(i.findAll('meta')[3].attrs.get('content'))
        print(i.findAll('meta')[2].attrs.get('content'))

        link = i.find('audio').attrs.get('src')
        date = link.split('=')[1][0:-5]
        hash = link.split('=')[2][0:-6]
        mp3_link = f'https://cdn1.101.ru/vardata/modules/musicdb/files/{date}/{hash}.mp3'
        print(mp3_link)

        # print(i.find('meta').attrs.get('content'))
        print('------------------------------------------------')
    except BaseException:
        pass


