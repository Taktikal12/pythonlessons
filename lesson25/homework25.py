
# Задание 1: Получение случайной цитаты
# Напишите функцию get_random_quote(), которая запрашивает случайную цитату с API https://api.quotable.io/random и возвращает её.
# Условия:
# - Используйте requests.get().
# - Ответ должен быть возвращён в виде строки с цитатой.
# - Обработайте ошибки, если запрос не удался.
# Пример:
# Входные данные: Нет входных данных, так как цитата генерируется случайным образом.
# Выходные данные:
# {
#   "content": "The only way to do great work is to love what you do.",
#   "author": "Steve Jobs"
# }

# Задание 2: Получение курса валют
# Напишите функцию get_exchange_rate(), которая получает курс валюты (например, курс доллара к тенге) с API https://api.exchangerate.host/latest с параметрами base="USD" и symbols="KZT".
# Условия:
# - Используйте requests.get().
# - Возвращайте результат в виде словаря, где указаны данные по курсу валют.
# - Обработайте возможные ошибки (например, неверный формат ответа).
# Пример:
# Входные данные: Нет входных данных, так как функция просто получает курс валют.
# Выходные данные:
# {
#   "base": "USD",
#   "date": "2025-05-01",
#   "rates": {
#   "KZT": 464.50
#   }
# }

# Задание 3: Прогноз погоды
# Напишите функцию get_weather(), которая запрашивает данные о погоде для города Алматы с API OpenWeatherMap.
# Условия:
# - Используйте requests.get() с URL, где в строке запроса передаются название города и ваш API-ключ.
# - Верните информацию о температуре в Цельсиях.
# - Если API-ключ неверный, обработайте ошибку.
# Пример:
# Входные данные:
# - Город: "Almaty"
# - Ваш API-ключ
# Выходные данные:
# {
#   "main": {
#     "temp": 293.25
#   }
# }

import requests

def get_weather(api_key):
    city = "Almaty"
    url = f"hhttps://api.openweathermap.org/data/2.5/weather?q=Almaty&appid=5eb0a0f6f1c97be143dd682574c358b4"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 401:
            return "Ошибка: неверный API-ключ."
        elif response.status_code != 200:
            return f"Ошибка: {data.get('message', 'Неизвестная ошибка')}"

        temp_kelvin = data["main"]["temp"]
        temp_celsius = temp_kelvin - 273.15

        return round(temp_celsius, 2)

    except requests.RequestException as e:
        return f"Ошибка запроса: {e}"

# api_key = "5eb0a0f6f1c97be143dd682574c358b4"
# print(get_weather(api_key))

# Задание 4: Взаимодействие с API методом POST
# Напишите функцию send_message(), которая отправляет сообщение на сервер с помощью POST-запроса.
# Условия:
# - Для этого задания используйте любой публичный API, который поддерживает отправку сообщений через POST (например, API для отправки уведомлений).
# - Функция должна принимать параметры: user_id и message.
# - Сохраните результат запроса и возвращайте его.
# Пример:
# Входные данные:
# - user_id: 123
# - message: "Hello, world!"
# Выходные данные:
# {
#   "status": "success",
#   "message": "Message sent successfully!"
# }

import requests

def send_message(user_id, message):
    url = "https://httpbin.org/post"
    payload = {
        "user_id": user_id,
        "message": message
    }

    try:
        response = requests.post(url, json=payload)
        data = response.json()

        return {
            "status": "success",
            "message": "Message sent successfully!",
            "server_response": data
        }

    except requests.RequestException as e:
        return {
            "status": "error",
            "message": f"Ошибка при отправке запроса: {e}"
        }

# print(send_message(123, "Hello, world!"))

# Задание 5: Получение данных о пользователе
# Напишите функцию get_user_info(), которая получает информацию о пользователе с API (например, https://jsonplaceholder.typicode.com/users).
# Условия:
# - Функция должна выводить имя и email пользователя.
# - Используйте метод GET для получения данных.
# Пример:
# Входные данные:
# Нет входных данных.
# Выходные данные:
# {
#   "name": "Leanne Graham",
#   "email": "Sincere@april.biz"
# }

import requests

def get_user_info():
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return f"Ошибка: {response.status_code}"

        user = data[0]
        return {
            "name": user["name"],
            "email": user["email"]
        }

    except requests.RequestException as e:
        return f"Ошибка запроса: {e}"

# print(get_user_info())

# Задание 6: Отправка данных формы на сервер
# Напишите функцию submit_form(), которая отправляет данные формы на сервер с помощью POST-запроса.
# Условия:
# - Используйте API https://reqres.in для отправки данных.
# - Формат данных для отправки: name и job.
# - Верните ответ от сервера.
# Пример:
# Входные данные:
# - name: "John Doe"
# - job: "Software Developer"
# Выходные данные:
# {
#   "name": "John Doe",
#   "job": "Software Developer",
#   "id": "1",
#   "createdAt": "2025-05-01T12:00:00.000Z"
# }

import requests

def submit_form(name, job):
    url = "https://reqres.in"
    payload = {
        "name": name,
        "job": job
    }

    try:
        response = requests.post(url, json=payload)
        data = response.json()

        if response.status_code == 201:
            return data
        else:
            return f"Ошибка: {response.status_code} - {data}"

    except requests.RequestException as e:
        return f"Ошибка запроса: {e}"

# print(submit_form("John Doe", "Software Developer"))
# print(submit_form("Alice", "Data Analyst"))


# Задание 7: Скачивание изображений
# Напишите функцию download_image(), которая скачивает изображение с URL и сохраняет его на диск.
# Условия:
# - Используйте requests.get() для скачивания файла.
# - Изображение сохраните в текущей директории с именем image.jpg.
# - Проверьте, существует ли файл, прежде чем скачивать.
# Пример:
# Входные данные:
# - URL изображения: "https://example.com/image.jpg"
# Выходные данные:
# - Изображение будет сохранено в файл image.jpg в текущей директории.

import requests
import os

def download_image(url):
    filename = "https://www.google.com/imgres?q=dina%20fritz%20titan&imgurl=https%3A%2F%2Fstatic0.srcdn.com%2Fwordpress%2Fwp-content%2Fuploads%2F2020%2F08%2Fattack-on-titan-smiling-titan.jpg%3Fq%3D50%26fit%3Dcrop%26w%3D960%26h%3D500%26dpr%3D1.5&imgrefurl=https%3A%2F%2Fduniagames.co.id%2Fdiscover%2Farticle%2F10-fakta-menarik-dina-fritz-shingeki-no-kyojin%2Fen%2F&docid=swycSbA_nBkCYM&tbnid=3b_jnElqpFvSEM&vet=12ahUKEwjjov7mkqKNAxV2wzgGHcNbLmsQM3oECB0QAA..i&w=960&h=500&hcb=2&ved=2ahUKEwjjov7mkqKNAxV2wzgGHcNbLmsQM3oECB0QAA"

    if os.path.exists(filename):
        return "Файл https://www.google.com/imgres?q=dina%20fritz%20titan&imgurl=https%3A%2F%2Fstatic0.srcdn.com%2Fwordpress%2Fwp-content%2Fuploads%2F2020%2F08%2Fattack-on-titan-smiling-titan.jpg%3Fq%3D50%26fit%3Dcrop%26w%3D960%26h%3D500%26dpr%3D1.5&imgrefurl=https%3A%2F%2Fduniagames.co.id%2Fdiscover%2Farticle%2F10-fakta-menarik-dina-fritz-shingeki-no-kyojin%2Fen%2F&docid=swycSbA_nBkCYM&tbnid=3b_jnElqpFvSEM&vet=12ahUKEwjjov7mkqKNAxV2wzgGHcNbLmsQM3oECB0QAA..i&w=960&h=500&hcb=2&ved=2ahUKEwjjov7mkqKNAxV2wzgGHcNbLmsQM3oECB0QAA уже существует."

    try:
        response = requests.get(url)

        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            return "Изображение успешно сохранено как https://www.google.com/imgres?q=dina%20fritz%20titan&imgurl=https%3A%2F%2Fstatic0.srcdn.com%2Fwordpress%2Fwp-content%2Fuploads%2F2020%2F08%2Fattack-on-titan-smiling-titan.jpg%3Fq%3D50%26fit%3Dcrop%26w%3D960%26h%3D500%26dpr%3D1.5&imgrefurl=https%3A%2F%2Fduniagames.co.id%2Fdiscover%2Farticle%2F10-fakta-menarik-dina-fritz-shingeki-no-kyojin%2Fen%2F&docid=swycSbA_nBkCYM&tbnid=3b_jnElqpFvSEM&vet=12ahUKEwjjov7mkqKNAxV2wzgGHcNbLmsQM3oECB0QAA..i&w=960&h=500&hcb=2&ved=2ahUKEwjjov7mkqKNAxV2wzgGHcNbLmsQM3oECB0QAA"
        else:
            return f"Ошибка: не удалось скачать изображение (код {response.status_code})"

    except requests.RequestException as e:
        return f"Ошибка запроса: {e}"

# print(download_image("hhttps://www.google.com/imgres?q=dina%20fritz%20titan&imgurl=https%3A%2F%2Fstatic0.srcdn.com%2Fwordpress%2Fwp-content%2Fuploads%2F2020%2F08%2Fattack-on-titan-smiling-titan.jpg%3Fq%3D50%26fit%3Dcrop%26w%3D960%26h%3D500%26dpr%3D1.5&imgrefurl=https%3A%2F%2Fduniagames.co.id%2Fdiscover%2Farticle%2F10-fakta-menarik-dina-fritz-shingeki-no-kyojin%2Fen%2F&docid=swycSbA_nBkCYM&tbnid=3b_jnElqpFvSEM&vet=12ahUKEwjjov7mkqKNAxV2wzgGHcNbLmsQM3oECB0QAA..i&w=960&h=500&hcb=2&ved=2ahUKEwjjov7mkqKNAxV2wzgGHcNbLmsQM3oECB0QAA"))


# Задание 8: Получение информации о пользователях через API
# Напишите функцию get_user_info_by_id(), которая запрашивает информацию о пользователе по его ID с API https://jsonplaceholder.typicode.com/users/{id}.
# Условия:
# - Функция должна принимать user_id как аргумент.
# - Вывести информацию о пользователе (имя, email).
# - Обработайте ошибку, если введён неправильный ID.
# Пример:
# Входные данные:
# - user_id: 1
# Выходные данные:
# {
#   "id": 1,
#   "name": "Leanne Graham",
#   "username": "Bret",
#   "email": "Sincere@april.biz"
# }

# Задание 9: Работа с параметрами в URL
# Напишите функцию get_weather_by_city(), которая получает погоду для указанного города с API OpenWeatherMap.
# Условия:
# - Функция должна принимать city как аргумент.
# - Используйте requests.get() с параметрами, включающими ваш API-ключ.
# - Верните температуру в градусах Цельсия для города, указанного в параметре.
# Пример:
# Входные данные:
# - Город: "Almaty"
# - Ваш API-ключ
# Выходные данные:
# {
#   "main": {
#     "temp": 293.25
#   }
# }

