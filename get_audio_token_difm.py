import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import random
import time
import os

audio_token = "615841863e5533f627fa26bd6e921776"

ua = UserAgent()

headers = {"User-Agent": ua.random}
sites = ['di', 'rockradio', 'radiotunes', 'jazzradio', 'classicalradio', 'zenradio']
link = f'https://qh8bsvaksadb2kj9.public.blob.vercel-storage.com/audio/audio.json'
id = 1
count_fetch = 20

r = requests.get(link, headers=headers)
tokens = r.json()

print('Всего токенов -', len(tokens))

new_tokens = []
for token in tokens:
    # print(token)
    try:
        link_hidden = f'https://api.audioaddict.com/v1/{sites[0]}/routines/channel/{id}?tune_in=true&audio_token={token}'
        headers = {"User-Agent": ua.random}
        r = requests.get(link_hidden, headers=headers)
        # print(r.json())
        print(token, '- валидный токен')
        new_tokens.append(token)

        time.sleep(random.randint(1, 5))
    except BaseException:
        print(token, '- ############ не валидный токен ############')

# Список прокси (пример)
proxies = [
    "188.191.164.55:4890",
    "195.74.86.205:80"
]

for i in range(count_fetch):
    chrome_options = Options()
    chrome_options.add_argument("--disable-application-cache")
    chrome_options.add_argument("--disable-extensions")
    # Опции для обхода детектирования
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    # Используем прокси из списка (циклически)
    # proxy = proxies[i % len(proxies)]
    # chrome_options.add_argument(f'--proxy-server=socks5://188.120.226.45:80')
    # chrome_options.add_argument(f'--proxy-server=http://{proxy}')

    driver = None
    try:
        url = 'https://www.di.fm/'
        driver = webdriver.Chrome(options=chrome_options)
        # Маскируем WebDriver
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": ua.random
        })

        driver.get(url)

        elements = driver.page_source
        position = elements.find("audio_token")
        print(elements[position + 14: position + 46], '- новый токен')
        new_tokens.append(elements[position + 14 : position + 46])

    except Exception as e:
        print(f'Не удалось получить: {e}')
    finally:
        if driver:
            driver.close()
            driver.quit()

    time.sleep(random.randint(1, 5))


with open(f"audio.json", "w", encoding='utf-8') as file:
    json.dump(new_tokens, file, indent=2, ensure_ascii=False)

print('Всего токенов -', len(new_tokens))
