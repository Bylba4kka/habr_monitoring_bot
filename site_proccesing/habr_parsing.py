import json
import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import glob


payload = ""
headers = {
    "cookie": "_session_id=dXMwcFJleGVIZGxoc1NGSTR0K0ZWNE5EdFNCbDVEcUJsTnhFR3dZeVZJN2pwRExvMVpuSW0ya29ybytJd1d2NjNxanYzNW8wSncxWmR5VmVNTVJkVk1vVUtTMVQySzFwaEtCdGhxWFJ1c0tCMHg5VjlNQXk3SWF5U1J1S3QyaXVMNVJyb2Z5cVJYU3BqanlPbSs2TmNLdUlUZWNCQTE3NjdEZlNSSlNPVnVieUVWMy9wWG9XUUtrTlZjYlllNW1CandUSjRSbWZqYm1COVlhZjBDOVFJa3dXNUVpM3Z4VThnM1hjeGNJbE9Wak1mVXJrekRSalNLNm9tWVdkUFhUaFhWTXVUdXkxekZ2QUlweW1BMEg1QlE9PS0taVJ1cFlROWRxQXFpWWNHYXl3RmZNQT09--4cf2cd599fe6b69e8820ac14d19cd73dae4edd5d",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Cookie": "habr_uuid=YUNJWHFteE1vM1IxUkw1bW9GUGZRWnZtcHZlcWZ2ZnZqL2hBMjVUTjJXVWMrQ2hCTjFMNjZuZGZXWGpmdEJDYw^%^3D^%^3D; _ga=GA1.3.2142801339.1707395195; _ym_uid=1707395195829209979; _ym_d=1707395195; _ga_HD710FM6BY=GS1.3.1709721388.4.0.1709721388.0.0.0; FCCDCF=^%^5Bnull^%^2Cnull^%^2Cnull^%^2C^%^5B^%^22CP6OgQAP6OgQAEsACBENAnEoAP_gAEPgACiQINJD7D7FbSFCwHpzaLsAMAhHRsCAQoQAAASBAmABQAKQIAQCgkAQFASgBAACAAAAICZBIQAECAAACUAAQAAAAAAEAAAAAAAIIAAAgAEAAAAIAAACAAAAEAAIAAAAEAAAmAgAAIIACAAAhAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAQOhQD2F2K2kKFkPCmQWYAQBCijYEAhQAAAAkCBIAAgAUgQAgFIIAgAIFAAAAAAAAAQEgCQAAQABAAAIACgAAAAAAIAAAAAAAQQAAAAAIAAAAAAAAEAAAAAAAQAAAAIAABEhCAAQQAEAAAAAAAQAAAAAAAAAAABAAA.f_gAAAAAAAA^%^22^%^2C^%^222~2072.70.89.93.108.122.149.196.2253.2299.259.2357.311.313.323.2373.338.358.2415.415.449.2506.2526.486.494.495.2568.2571.2575.540.574.2624.609.2677.864.981.1029.1048.1051.1095.1097.1126.1201.1205.1211.1276.1301.1344.1365.1415.1423.1449.1451.1570.1577.1598.1651.1716.1735.1753.1765.1870.1878.1889.1958~dv.^%^22^%^2C^%^222E0D5EBB-6F05-4CF0-AF74-888EA85F439E^%^22^%^5D^%^5D; FCNEC=^%^5B^%^5B^%^22AKsRol_wmeitut7_JC9O_aW9oL3OuMP20qxNmUL0CNwS2UlxDfaYTYjpe44gOTg9IJiVTq0xwRRAj-R363PIbJ5XjxWkJT_fOndNu1HCMCC4JJDam5V6eQWrKYuBwYvPyAdo8YEpFHBoja1R2KNpX49YoTs07a8ZRQ^%^3D^%^3D^%^22^%^5D^%^5D; remember_user_token=BAhbCFsGaQM1eBJJIiIkMmEkMTAkSjFtUUdMT1NmN1hFNS9yOHFadkFHdQY6BkVUSSIWMTcxMDkyOTA3NC44NTkwOTIGOwBG--2a40c0ebe9d57c15a66ae08aee84195b07cf345e; _session_id=Z2puVU9yYjFQMEsvVlB6OXZWY3F6OHFiNTRIbVZoMUpiSkVxRFIzd21ta0NsOW52VS8wZ05RZkxLYjlPYmxMcURGeElKelNIZmg2c0Ivb2ladkFva1VUM0J6ZDJiMU42Y2JZZHR5WXI3WEhZbHJmd05ONmo5d3VxZE9CclR6MmJtY28yNFRlVVAzNVRodjFxWWFGZkxiOWFKR1Zjc09sVWpLUk1FNmhOSW9XbU15WVp2VThFVkdzMnh4SExTSUIraDJGSG8vSThCZUN4cUhmWFF5cXhhTUVtWHFaNFhBcE0xQzVRZW1hUGVpNng3ZEdpN1laeTkyM29JM2RRTC80OEl5ZXdNeEVCQyswNDhvVTVIZ2xqTXc9PS0tNmxTQVNabmx5dkdxWDZoeGU1MWhadz09--977843f779c3452c0c28429e657525ae923a68ff",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-GPC": "1",
    "If-None-Match": "W/86e668fb7e390ffb104ef24731ca298a"
}

def scrape_data():
    url = "https://freelance.habr.com/tasks?categories=development_all_inclusive,development_backend,development_frontend,development_prototyping,development_ios,development_android,development_desktop,development_bots,development_games,development_1c_dev,development_scripts,development_voice_interfaces,development_other"
    folder_path = os.getcwd() + '/site_proccesing/site_backups/'

    # Получить текущую дату и время
    current_datetime = datetime.now()

    # Преобразовать дату и время в строку
    current_datetime_str = current_datetime.strftime('%Y-%m-%d_%H-%M-%S')

    file_name = "freelance.habr.com_" + str(current_datetime_str)

    task_data = list()

    r = requests.request("GET", url, data=payload, headers=headers)

    soup = BeautifulSoup(r.content, "html.parser")

    # Берём все блоки с заданиями
    data = soup.find_all("li", class_="content-list__item")

    # Итерируемся по блокам для дальнейшего парса
    for i in data:
        try:
            name = i.find("div", class_="task__title").find("a").text
        except:
            name = None

        try:
            time = i.find("div", class_="task__params params").\
                find("span", class_="params__published-at icon_task_publish_at").text.strip()
        except:
            time = None

        try:
            price = i.find("aside", class_="task__column_price").text
        except:
            price = None

        try:
            url = i.find("div", class_="task__title").find("a")
            url = "https://freelance.habr.com" + url['href']
        except:
            url = None

        try:
            responses = i.find("div", class_="task__params params").\
                find("span", class_="params__responses icon_task_responses").text.strip()
        except:
            responses = None

        try:
            views = i.find("div", class_="task__params params").\
                find("span", class_="params__views icon_task_views").text.strip()
        except:
            views = None

        task_data.append(
            {
                "name": name,
                "responses": responses,
                "views": views,
                "time": time,
                "price": price,
                "url": url,
            }
        )
    # Бэкап страницы
    with open(folder_path + f"{file_name}.json", "w", encoding="utf-8") as file:
        json.dump(task_data, file, indent=4, ensure_ascii=False)


    # Получение списка файлов
    files = os.listdir(folder_path)
    files = [os.path.join(folder_path, file) for file in files]

    # Последний бэкап
    file1 = files[-1]

    # Предпоследний бэкап
    try:
        file2 = files[-2]
    except:
        file2 = file1


    # Получить список всех файлов в папке, отсортированный по времени последней модификации
    files = sorted(glob.glob(os.path.join(folder_path, '*')), key=os.path.getmtime)

    # Проверить количество файлов в папке
    if len(files) > 2:
        # Удалить все бэкапы, кроме двух последних
        for file_to_delete in files[:-2]:
            os.remove(file_to_delete) 

    return file1, file2


def unique_values(file1, file2):
    # Загрузка данных из первого JSON файла
    with open(file1, 'r', encoding='utf-8') as file1:
        data1 = json.load(file1)

    # Загрузка данных из второго JSON файла
    with open(file2, 'r', encoding='utf-8') as file2:
        data2 = json.load(file2)

    # Создаем пустой список для хранения значений, которые есть в первом файле, но отсутствуют во втором
    unique = []

    # Проходим по каждому элементу из первого файла
    for item in data1:
        # Получаем значения из текущего элемента
        name = item["name"]
        responses = item["responses"]
        views = item["views"]
        time = item["time"]
        price = item["price"]
        url = item["url"]


        # Проверяем, есть ли эти значения во втором файле
        if not any(d["name"] == name for d in data2):
            # Если значение отсутствует во втором файле, добавляем его в список уникальных значений.

            unique.append(
                {
                    "name": name,
                    "responses": responses,
                    "views": views,
                    "time": time,
                    "price": price,
                    "url": url,
                }
            )


    return unique
