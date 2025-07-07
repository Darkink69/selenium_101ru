import requests
import json
import os
from fake_useragent import UserAgent
import time
import random

ua = UserAgent()


for i in range(100000):
    data = json.load(open(f"all_channel_101.json", "r", encoding='utf-8'))
    # print(data)
    for channel in data:
        print(channel["id"], channel["name"])
        file_json = channel["name"]

        url_101 = f'https://101.ru/api/channel/getTrackOnAir/{channel["id"]}'
        headers = {"User-Agent": ua.random}
        r = requests.get(url_101, headers=headers)

        try:
            title = r.json()["result"]["short"]["title"]
            cover = r.json()["result"]["short"]["cover"]["coverHTTP"]
            mp3 = r.json()["result"]["short"]["audiofile"]

            if not os.path.isfile(f"json_101/{file_json}.json"):
                print(f"Создаем новый файл {file_json}.json")
                all_tracks = {
                    "channel_id": channel["id"],
                    "channel": file_json,
                    "tracks": []
                }
                with open(f"json_101/{file_json}.json", "w", encoding='utf-8') as file:
                    json.dump(all_tracks, file, indent=2, ensure_ascii=False)
                data = json.load(open(f"json_101/{file_json}.json", "r", encoding='utf-8'))
                json_data = {
                    title: r.json()["result"]["short"]
                }

                data["tracks"].append(json_data)
                with open(f"json_101/{file_json}.json", "w", encoding='utf-8') as file:
                    json.dump(data, file, indent=2, ensure_ascii=False)

            data = json.load(open(f"json_101/{file_json}.json", "r", encoding='utf-8'))
            all_tracks = []
            for track in data["tracks"]:
                all_tracks.append(list(track.keys())[0])

            if title not in all_tracks:
                json_data = {
                    title: r.json()["result"]["short"]
                }

                data["tracks"].append(json_data)
                with open(f"json_101/{file_json}.json", "w", encoding='utf-8') as file:
                    json.dump(data, file, indent=2, ensure_ascii=False)

                print(title)
                print(cover)
                print(mp3)
                print(len(all_tracks), "- all unique tracks parsed")


            print('--------------------------------------------')
        except BaseException:
            print('Что-то идет не так...')

        time.sleep(random.randint(1, 10))
    print('##########################################################################')
    time.sleep(random.randint(100, 600))

