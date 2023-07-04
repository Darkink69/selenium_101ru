from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json


driver = webdriver.Chrome()
driver.get("https://101.ru/radio/channel/79")

def add_to_json(name, song, cover_url):
    json_data = {
        "name": name,
        "song": song,
        "cover": cover_url
    }
    # try:
    data = json.load(open("db.json", "r", encoding='utf-8'))
    data.append(json_data)

    with open("db.json", "w", encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    # except BaseException:
    #     print("Error read/write")


for i in range(10000):
    elements = driver.find_elements(By.CLASS_NAME, 'channel-info__captions')
    cover = driver.find_elements(By.XPATH, '//*[@id="content"]/div/div[1]/div[1]/div[2]/div[1]/a[1]/img')

    temp = []
    for e in elements:
        temp.append(e.text)

    temp = temp[0].split('\n')
    try:
        name = temp[1]
        song = temp[0]
        print(name)
        print(song)
    except BaseException:
        name = ''
        song = ''


    temp = []
    for i in cover:
        temp.append(i.get_attribute('src'))

    try:
        temp = temp[0].split('\n')
        cover_url = temp[0]
    except BaseException:
        cover_url = ''
    print(cover_url)

    add_to_json(name, song, cover_url)

    time.sleep(200)
