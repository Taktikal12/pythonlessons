# 1. Что такое словарь в Python?
#    - Словарь — это структура данных, которая хранит пары "ключ: значение".
#    - Ключи уникальны и неизменяемы.
#    - Значения могут быть любыми типами данных.

# 2. Создание словаря:
#    - Пустой словарь:
#         my_dict = {}
#         dictionary = dict()
#    - Заполненный словарь:
# student = {
#      "name": "Алексей",
#      2: 33,
#      True: [1, 2, 3],
#      "status": True,
#      "age": 21
# }

# 3. Обращение к значениям по ключу:
# print(student["name"])  # Алексей
# # print(student["age2"])  # keyError ключ не существует в словаре
# print(student.get("city", "Москва"))
# print(student.get("status"))
# print(student.get("status2"))

# 4. Методы словарей:
#    - .get(key, default) — безопасное получение значения.
#    - .keys() — возвращает все ключи словаря.
#    - .values() — возвращает все значения.
#    - .items() — возвращает пары (ключ, значение).
#    - .update() — обновляет словарь.
#    - .pop(key[, default]) — удаляет ключ и возвращает его значение.
#    - .clear() — очищает словарь.

# print(student.keys())  # возвращает все ключи
# print(student.values())  # возвращает все значения
# print(student.items())  # возвращает все пары (ключ, значение)
# student.update({"name": "vlad", "city": "Bishkek"})
# print(student)
#
# name = student.pop("name")  # удаляет пару по ключу и возвращает значение
# print(name)
# print(student)
#
# student.clear()
# print(student)
#
#
# 5. Добавление и изменение элементов:
# student["age"] = 22  # Изменение значения
# student["grade"] = "A"  # Добавление новой пары
# print(student)
#
# # 6. Удаление элементов:
# student.pop("city")  # Удаляет пару с ключом 'city'
# del student["name"]  # Удаляет ключ 'name'
#
# # 7. Проверка наличия ключа:
# if "name" in student:
#     print("Ключ 'name' есть в словаре!")


# Ознакомительные задачи:
# 1. Создай словарь, содержащий информацию о книге (название, автор, год издания). Выведи автора книги.
book = {
     "name": "Python",
     "avtor": "Dilmurat",
     "publish_year": 2025
}
print(book["avtor"])
print(book.get("avtor"))

# 2. Создай пустой словарь и добавь в него три ключа: имя, возраст, город.
slovar = {}

slovar["name"] = "Улугбек"
slovar["vozrast"] = 23
slovar["gorod"] = "Алай"
print(slovar)
# 3. Удали ключ "город" из словаря и выведи результат.
slovar.pop("gorod")
print(slovar)
# 4. Проверь, есть ли ключ "телефон" в словаре и выведи сообщение об этом.
if "name" in slovar:
     print("Ключ 'телефон' в словаре!")
# # 5. Измени значение ключа "возраст" на 30.
slovar["vozrast"] = 30
print(slovar)
# 6. Создай словарь с именами друзей и их любимыми цветами. Выведи любимый цвет одного из друзей.
friends = {
     "Семетей": "Желтый",
     "Сайтама": "Синий",
     "Мырзалы": "Черный",
}
print(friends["Сайтама"])

# 7. Создай словарь студентов и их оценок. Выведи всех студентов и их оценки.
students = {
     "Aselya": "5+",
     "Naima": "5",
     "Idris": "5",
}
print(students)

# 8. Используя .get(), получи значение несуществующего ключа с выводом "Нет такого ключа".
print(students.get("vyvod","Нет такоко ключа"))

# 9. Создай словарь с продуктами и их ценами. Добавь новый продукт и выведи обновленный словарь.
products = {
     "Meat": "180000rp",
     "Srawberry": "15000rp",
     "Oil": "32000rp",
}
print(products)
products["Chicken"] = "17000rp"
print(products)

# 10. Подсчитай количество ключей в словаре.
print(len(products))

# 11. Создай словарь с номерами автомобилей и их владельцами. Выведи владельца одного из автомобилей.
auto_numbers = {
     "01kg222ajj": "Shabdanbek",
     "01kg908ajj": "Azamat",
     "0001SM": "Shabdan",
}
print(auto_numbers["0001SM"])

# 12. Добавь нового владельца и автомобиль в словарь.
auto_numbers["9000BP"] = "Mukashovich"
print(auto_numbers)

# 13. Удали информацию о владельце автомобиля по номеру.
del auto_numbers["01kg222ajj"]
print(auto_numbers)

# 14. Используй метод .items() для вывода всех пар "ключ: значение".
print(auto_numbers.items())

# 15. Используй метод .values() для получения всех значений словаря.
print(auto_numbers.values())

# 16. Создай словарь с названиями стран и их столицами. Выведи столицу указанной страны.
countries = {
     "Kyrgyzstan": "Bishkek",
     "Qazakstan": "Astana",
     "Germany": "Berlin",
}
print(countries["Kyrgyzstan"])

# 17. Измени название столицы одной из стран.
countries["Germany"] = "Munchen"
print(countries)

# 18. Проверь наличие страны в словаре перед получением её столицы.
if "Qazakstan" in countries:
     print("'Qazakstan'")

# 19. Используй метод .update() для объединения двух словарей.
auto_numbers.update(countries)
print(auto_numbers)

# 20. Создай словарь с логинами и паролями пользователей. Проверь правильность пароля для заданного логина.
user = {
     "sm12": "0000",
     "luxurybala": "password12"
}
login = "sm12"
password = "0000"
if user.get(login) == password:
     print('Пароль верный')
else:
     print('Неверный логин,пароль')

# 21. Создай словарь с днями недели и их порядковыми номерами. Выведи номер среды.
week = {
     "monday": "1",
     "Tuesday": "2",
     "Wednesday": "3",
     "Thursday": "4",
     "Friday": "5",
     "Saturday": "6",
     "Sunday": "7",
}
print(week["Wednesday"])

# 22. Проверь, есть ли в словаре ключ "воскресенье".
print("Sunday" in week)

# 23. Создай словарь с курсами валют и их значениями. Получи значение курса доллара.
currency = {
     "USD": "87,9",
     "Euro": "93,5",
     "Rub": "1,1",
     "IndRP": "0,016",
}
print(currency["USD"])

# 24. Добавь новую валюту и её курс.
currency["Dogcoin"] = "1,123"
print(currency)

# 25. Создай словарь с любимыми фильмами друзей. Выведи фильмы одного из друзей.
movie = {
     "Семетей": "Царство небесное", "Сайтама": "Гладиадор", "Мырзалы": "Троя",
}
print(movie["Сайтама"])

# 26. Измени фильм в словаре для одного из друзей.
movie["Семетей"] = "Pornhub"
print(movie)

# 27. Создай словарь с наименованиями товаров и их количество. Уменьши количество одного из товаров.
product = {
     "Potato": "1kg", "Tomato": "2kg", "Carrot": "3kg", "Lamb": "5kg",
}
print(product)
product["Lamb"] = "4,5kg"
print(product)

# 28. Используй метод .clear() для очистки словаря.
product.clear()
print(product)

# 29. Создай словарь с именами сотрудников и их должностями. Выведи должность указанного сотрудника.
community = {
     "Johongir": "Ceo", "Dilmurat": "Ticher", "Gaggur": "HR",
}
print(community["Dilmurat"])

# 30. Удали информацию о сотруднике по имени.
del community["Johongir"]
print(community)

# 31. Создай словарь с предметами и их баллами. Посчитай общую сумму баллов.
lesson = {
     "Chimestry": 100, "Biology": 95, "Anotomy": 120,
}
total = sum(lesson.values())
print(total)

# 32. Создай словарь с животными и их звуками. Выведи звук указанного животного.
animals = {
     "Cat": "meow",
     "Dog": "gaw",
     "Wolf": "auu",
}
print(animals["Cat"])

# 33. Измени звук одного из животных.
animals["Dog"] = "cria-cria"
print(animals)

# 34. Создай словарь с товарами и их ценами. Увеличь цену одного из товаров на 10%.
tovary = {
     "Iphone": 1300, "Macbook": 2350, "Airpods": 220,
}
tovary["Airpods"] *= 1.10
print(tovary)

# 35. Создай словарь с именами студентов и их возрастом. Выведи возраст студента с заданным именем.
students = {
     "Azim": "21", "Almaz": "28", "Aisultan": "25",
}
print(students["Aisultan"])

# 36. Проверь наличие студента в словаре перед выводом его возраста.
if "Azim" in students:
     print("Azim есть в словаре!")

# 37. Создай словарь с названиями городов и численностью населения. Увеличь численность одного из городов.
cities = {
     "Alay": 10000000, "Kemin": 900000, "Karakol": 3000,
}
cities["Karakol"] *= 35
print(cities)

# 38. Используй метод .pop() для удаления ключа и получения его значения.
cities = cities.pop("Karakol")
print("Karakol")
print(cities)

# 39. Создай словарь с играми и их рейтингами. Выведи игру с наивысшим рейтингом.
games = {
     "CS2.0": 4.9, "Dota": 4.8,
}
print(games["CS2.0"])

# 40. Создай словарь с контактами и их телефонами. Выведи телефон указанного контакта.
contacts = {
     "Nika": "0555252525", "Gulya": "0777777777", "Jibek": "+42986653421",
}
print(contacts["Nika"])

