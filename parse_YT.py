import json
import time
import datetime as dt
import subprocess
import os


# def add_to_json():
#     json_data = {
#         "name": name,
#         "phone": phone,
#     }
#     data = json.load(open("db.json"))
#     data.append(json_data)
#     with open("db.json", "w") as file:
#         json.dump(data, file, indent=2, ensure_ascii=False)

# add_to_json()

with open('db.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(len(items))
# print(items)

for index, item in enumerate(items):
    # print(index, item)
    if item['song'] in ['Реклама', ' ', '', '—', '–', '-']:
        # print(index, item)
        del items[index]

print(len(items))
# for i in items:
#     if items[3]['name'] == i['name']:
#         print(i['name'], i['song'])

all_artists = []

for index, item in enumerate(items):
    name = items[index]['name']
    del item['cover']
    if item['name'] == name:
        if item not in all_artists:
            # print(item['name'], '-', item['song'], item['cover'])
            all_artists.append(item)


# print(all_artists)
print(len(all_artists))


for i in all_artists:
    if all_artists[15]['name'] == i['name']:
        print(i['name'], i['song'])


req = f"{all_artists[33]['name']} - {all_artists[33]['song']}"
print(req)

pro = f'yt-dlp "ytsearch3:{req}" --get-id --get-title'
pr = subprocess.check_output(pro, shell=True)

print(pr)



