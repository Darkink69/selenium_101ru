import requests
import json
import time
import uni_telegram_bot
chat_id = "813012401"


channel_id = 79  # cyber space
channel = "Cyber Space"


for i in range(10000):
    url_101 = f'https://101.ru/api/channel/getTrackOnAir/{channel_id}'
    headers = {
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) "
                      "AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
    }
    r = requests.get(url_101, headers=headers)

    try:
        title = r.json()["result"]["short"]["title"]
        cover = r.json()["result"]["short"]["cover"]["coverHTTP"]
        mp3 = r.json()["result"]["short"]["audiofile"]
        print(title)
        print(cover)
        print(mp3)

        data = json.load(open("db101.json", "r", encoding='utf-8'))
        all_tracks = []
        for track in data["tracks"]:
            all_tracks.append(list(track.keys())[0])

        print(len(all_tracks), "- all unique tracks parsed")

        if title not in all_tracks:
            json_data = {
                title: r.json()["result"]["short"]
            }

            data["tracks"].append(json_data)
            with open("db101.json", "w", encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)

            uni_telegram_bot.send_message(chat_id, len(all_tracks))

        left_sec = r.json()["result"]["stat"]["finishSong"] - int(round(time.time()))
        print(left_sec, "- sec next track")
    except BaseException:
        left_sec = 15

    time.sleep(left_sec + 15)

