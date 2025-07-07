import requests
from bs4 import BeautifulSoup
import json

# Получаем HTML-код страницы
url = "https://101.ru/radio-top"

response = requests.get(url)


# Парсим HTML с помощью BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Находим все теги <a> с указанным классом
channel_tags = soup.find_all('a', class_='grid__title noajax')

channels = []
for tag in channel_tags:
    # Извлекаем ID канала из атрибута href
    href = tag.get('href', '')
    channel_id = href.split('/')[-1] if href else ''

    # Извлекаем название канала из тега <span>
    span = tag.find('span', itemprop='name broadcastDisplayName')
    channel_name = span.text.strip() if span else ''

    if channel_id and channel_name:
        print(f"ID: {channel_id}, Name: {channel_name}")
        channels.append({
            'id': channel_id,
            'name': channel_name
        })

# Сохраняем данные в JSON файл
if channels:
    with open('all_channel_101.json', 'w', encoding='utf-8') as f:
        json.dump(channels, f, ensure_ascii=False, indent=4)
    print("Данные успешно сохранены в all_channel_101.json")
else:
    print("Не найдено ни одного канала")
