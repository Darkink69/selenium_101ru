import requests
import json
from fake_useragent import UserAgent
import random
import time
import os

ua = UserAgent()
stations = ['somafm_spacesta_current', 'rad_smfmclqhp_current', 'soma_groovesal_current', 'somafm_drone_zone_current', 'soma_suburbgoa_current']

for i in range(10000):

    try:
        for station in stations:
            link = f'https://meta.pcradio.ru/{station}.json'
            headers = {"User-Agent": ua.random}
            r = requests.get(link, headers=headers)
            print(f'Radio: {station}')
            track = r.json()["artist"] + ' - ' + r.json()["title"]
            print(track)

            if not os.path.isfile(f"db_pcradio_{station}.json"):
                print(f"Create new json file {station}")
                all_tracks = []
                with open(f"db_pcradio_{station}.json", "w", encoding='utf-8') as file:
                    json.dump(all_tracks, file, indent=2, ensure_ascii=False)

            data = json.load(open(f"db_pcradio_{station}.json", "r", encoding='utf-8'))
            # print(data)
            all_tracks = []
            for i in data:
                item_track = i["artist"] + ' - ' + i["title"]
                all_tracks.append(item_track)

            print(len(all_tracks), "- all unique tracks parsed on radio", station)

            if track not in all_tracks:
                json_data = {
                    "artist": r.json()["artist"], "title": r.json()["title"]
                }

                data.append(json_data)
                with open(f"db_pcradio_{station}.json", "w", encoding='utf-8') as file:
                    json.dump(data, file, indent=2, ensure_ascii=False)

            print('-------------------------------------')
            time.sleep(random.randint(1, 10))
    except BaseException:
        print('Problems...')

    wait = random.randint(50, 185)
    print(f'Next parsing in {wait} seconds...')
    print('##########################################################################')
    time.sleep(wait)






