
# Урок 24: Парсинг сайтов (основы)

# 🔸 Что такое pip и зачем он нужен

# pip — это стандартный менеджер пакетов в Python.
# Он используется для установки дополнительных библиотек, таких как requests или beautifulsoup4,
# которые не входят в стандартную библиотеку языка.

# Пример установки через терминал:
# pip install requests
# pip install beautifulsoup4

# Эти библиотеки нужны для парсинга HTML-страниц — скачивания и разбора содержимого сайта.

# 🔸 Что такое парсинг (веб-скрапинг)

# Парсинг сайтов — это автоматическое извлечение данных с HTML-страниц.
# Он используется в проектах для сбора новостей, цен товаров, прогнозов погоды и другой информации.

# 🔸 Основные библиотеки:
# - requests — получает HTML-код страницы.
# - BeautifulSoup — разбирает HTML и позволяет находить нужные элементы.

# Установка:
# pip install requests beautifulsoup4

# 🔸 Базовый пример кода для парсинга

import requests
from bs4 import BeautifulSoup

def basic_scraper():
    url = "https://example.com"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            titles = soup.find_all("h1")
            for t in titles:
                print(t.text)
        else:
            print("Ошибка загрузки страницы:", response.status_code)
    except Exception as e:
        print("Ошибка при запросе:", e)

# basic_scraper()

# 🔸 Основные методы BeautifulSoup
# find()      — находит первый тег по условию
# find_all()  — находит все теги по условию
# .text       — извлекает текст из тега
# [attr]      — получает значение атрибута (например, href, src)

# Примеры:
# soup.find("p", class_="info")
# soup.find("a")["href"]

# 🔸 Извлечение ссылок со страницы

def extract_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a")
        return [link.get("href") for link in links if link.get("href")]
    except Exception as e:
        return [f"Ошибка: {e}"]

print(extract_links("https://example.com"))

# 🔸 Парсинг таблицы

def extract_table_rows(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        rows = soup.find_all("a", class_="lf-ad-tile__link")
        for row in rows:
            print(row.text)
        return None
    except Exception as e:
        return [f"Ошибка: {e}"]

print(extract_table_rows("https://lalafo.kg/"))
# 🔸 Этические правила
# - Уважай robots.txt сайта (он может запрещать парсинг)
# - Используй паузы между запросами (time.sleep)
# - Не создавай нагрузку на сервер
# - Всегда проверяй, можно ли использовать собранные данные

# Для запуска:
# basic_scraper()
# print(extract_links("https://example.com"))
