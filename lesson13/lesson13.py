"""
Урок 13: Углубленное изучение списков: генераторы списков.
Циклы в словарях, zip(), enumerate()
"""

# Генераторы списков
"""
Генераторы списков позволяют создавать списки в одну строку кода, что делает их удобными и читаемыми.

Синтаксис:
[выражение for переменная in последовательность if условие]

Пример:
"""
# Создадим список квадратов чисел от 1 до 10
# squares = [x ** 2 for x in range(1, 11)]
# print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Оставим только чётные квадраты
# even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
# print(even_squares)  # [4, 16, 36, 64, 100]

# Циклы в словарях
"""
Когда работаем со словарями, часто нужно итерироваться по ключам, значениям или сразу по парам (ключ, значение).
"""
# example_dict = {'apple': 3, 'banana': 5, 'cherry': 2}

# Перебор ключей
# for key in example_dict:
#     print(key)

# Перебор значений
# for value in example_dict.values():
#     print(value)

# Перебор ключей и значений
# for key, value in example_dict.items():
#     print(f"{key}: {value}")

# Функция zip()
"""
Функция zip() используется для объединения нескольких последовательностей в кортежи.
"""
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]
#
# for name, score in zip(names, scores):
#     print(f"{name} набрал {score} баллов")

# Функция enumerate()
"""
enumerate() добавляет индекс к элементам последовательности.
"""
# fruits = ["apple", "banana", "cherry"]
# for index, fruit in enumerate(fruits, start=1):
#     print(f"{index}. {fruit}")

# ДОМАШНЕЕ ЗАДАНИЕ (45 задач)

# 1. Создайте список квадратов чисел от 1 до 20 с помощью генератора списков.
squares = [x ** 2 for x in range(1, 21)]
print(squares)
# 2. Создайте список четных чисел от 1 до 50.
even_squares = [x ** 2 for x in range(1, 51) if x % 2 == 0]
print(even_squares)
# 3. Создайте список чисел от 1 до 50, заменяя все числа, кратные 3, на 'Fizz'.
fz = ["Fizz" if x % 3 == 0 else x for x in range(1, 51)]
print(fz)
# 4. Создайте список из первых 10 чисел Фибоначчи с помощью генератора списков и цикла.
fib = [0, 1]
for _ in range(8):
    fib.append(fib[-1] + fib[-2])
print(fib)

# 5. Запросите у пользователя 5 чисел и сохраните их в список, умножив каждое на 2.
nums = [int(input(f"Введите число {i+1}: ")) * 2 for i in range(5)]
print(nums)

# 6. Запросите у пользователя строку и создайте список, содержащий только гласные буквы.
s = input("Введите строку: ")
vowels = [ch for ch in s if ch.lower() in 'aeiouаеёиоуыэюя']
print(vowels)

# 7. Создайте словарь, где ключи — числа от 1 до 5, а значения — их квадраты.
squares = {x: x**2 for x in range(1, 6)}
print(squares)

# 8. Используя zip(), объедините два списка и создайте из них словарь.
keys = ['a', 'b', 'c']
values = [1, 2, 3]
combined = dict(zip(keys, values))
print(combined)

# 9. Запросите у пользователя 3 пары ключ-значение и сохраните их в словарь.
d = {}
for _ in range(3):
    key = input("Введите ключ: ")
    value = input("Введите значение: ")
    d[key] = value
print(d)

# 10. Используя enumerate(), создайте список строк формата "Индекс: значение" из списка чисел.
numbers = [5, 10, 15]
result = [f"{i}: {val}" for i, val in enumerate(numbers)]
print(result)

# 11. Переберите словарь и выведите только те пары, где значение больше 10.
d = {'a': 5, 'b': 15, 'c': 8, 'd': 20}
for k, v in d.items():
    if v > 10:
        print(k, v)

# 12. Создайте генератор списка, содержащий длины слов в заданной строке.
s = "Пример строки с несколькими словами"
lengths = [len(word) for word in s.split()]
print(lengths)

# 13. Переберите список кортежей (имя, возраст) и выведите строки "Имя - возраст".
people = [("Айкыз", 25), ("Бабур", 30)]
for name, age in people:
    print(f"{name} - {age}")

# 14. Создайте словарь квадратов чисел от 1 до 10.
squares = {x: x**2 for x in range(1, 11)}
print(squares)

# 15. Сгенерируйте список кортежей (число, его квадрат) для чисел от 1 до 10.
result = [(x, x**2) for x in range(1, 11)]
print(result)

# 16. Запросите у пользователя 5 чисел. Если введено отрицательное число — прекратите ввод (break).
nums = []
for _ in range(5):
    n = int(input("Введите число: "))
    if n < 0:
        break
    nums.append(n)
print(nums)

# 17. Используя zip(), объедините два списка в список кортежей.
a = [1, 2, 3]
b = ['a', 'b', 'c']
zipped = list(zip(a, b))
print(zipped)

# 18. Переберите словарь с разными типами данных и выведите только числовые значения.
d = {'x': 10, 'y': 'строка', 'z': 3.14}
for v in d.values():
    if isinstance(v, (int, float)):
        print(v)

# 19. Используя zip(), создайте словарь из двух списков (названия стран и их столицы).
countries = ['Кыргызстан', 'Франция', 'Япония']
capitals = ['Бишкек', 'Париж', 'Токио']
country_capital = dict(zip(countries, capitals))
print(country_capital)

# 20. Запросите у пользователя строку и создайте список её символов в обратном порядке.
s = input("Введите строку: ")
reversed_list = list(s[::-1])
print(reversed_list)

# 21. Используйте генератор списка для создания списка кубов чисел от 1 до 10.
cubes = [x**3 for x in range(1, 11)]
print(cubes)

# 22. Используйте enumerate(), чтобы вывести все элементы списка с их индексами.
lst = ['a', 'b', 'c']
for i, val in enumerate(lst):
    print(f"{i}: {val}")

# 23. Переберите словарь и удалите из него элементы, где значение меньше 5.
d = {'a': 1, 'b': 10, 'c': 3, 'd': 8}
d = {k: v for k, v in d.items() if v >= 5}
print(d)

# 24. Объедините два списка в список кортежей и отсортируйте его по второму элементу.
a = ['x', 'y', 'z']
b = [3, 1, 2]
zipped = sorted(zip(a, b), key=lambda x: x[1])
print(zipped)

# 25. Запросите у пользователя числа, добавляйте их в список, пока не введёт 'стоп' (break).
lst = []
while True:
    val = input("Введите число или 'стоп': ")
    if val.lower() == 'стоп':
        break
    lst.append(int(val))
print(lst)

# 26. Запросите у пользователя строку и создайте словарь с подсчетом всех символов.
s = input("Введите строку: ")
counts = {ch: s.count(ch) for ch in set(s)}
print(counts)

# 27. Создайте словарь, где ключами будут числа от 1 до 10, а значениями их факториалы.
import math
factorials = {x: math.factorial(x) for x in range(1, 11)}
print(factorials)

# 28. Создайте список всех слов из строки, начинающихся с определённой буквы.
s = "Анна любит апельсины и арбузы"
letter = 'а'
words = [word for word in s.split() if word.lower().startswith(letter)]
print(words)

# 29. Используя zip(), создайте список пар (число, его факториал) для чисел от 1 до 5.
import math
nums = list(range(1, 6))
facts = [math.factorial(x) for x in nums]
pairs = list(zip(nums, facts))
print(pairs)

# 30. Создайте список, содержащий произведения пар чисел из двух списков.
a = [1, 2, 3]
b = [4, 5, 6]
products = [x*y for x, y in zip(a, b)]
print(products)

# 31. Используйте генератор списка, чтобы получить все чётные числа из списка.
lst = [1, 2, 3, 4, 5, 6]
evens = [x for x in lst if x % 2 == 0]
print(evens)

# 32. Переберите словарь и замените все его значения на их квадраты.
d = {'a': 2, 'b': 3, 'c': 4}
for k in d:
    d[k] = d[k]**2
print(d)

# 33. Используя zip(), создайте список пар значений из трёх списков разной длины.
a = [1, 2]
b = [3, 4]
c = [5, 6]
zipped = list(zip(a, b, c))
print(zipped)

# 34. Запросите у пользователя 10 чисел, если число нечётное — пропустите его (continue).
result = []
for _ in range(10):
    n = int(input("Введите число: "))
    if n % 2 != 0:
        continue
    result.append(n)
print(result)

# 35. Используйте zip(), чтобы поменять местами ключи и значения в словаре.
d = {'a': 1, 'b': 2}
swapped = dict(zip(d.values(), d.keys()))
print(swapped)

# 36. Используя генератор списка, создайте список всех четных чисел от 1 до 100.
evens = [x for x in range(1, 101) if x % 2 == 0]
print(evens)

# 37. Используя zip() и enumerate(), создайте словарь с индексами элементов списка.
lst = ['a', 'b', 'c']
indexed = dict(zip(range(len(lst)), lst))
print(indexed)

# 38. Создайте список кортежей (буква, её ASCII-код) для всех букв алфавита.
alphabet = [(chr(i), i) for i in range(ord('a'), ord('z')+1)]
print(alphabet)

# 39. Используя генератор списка, создайте список всех слов длиннее 5 символов.
s = "Это строка с несколькими длинными словами"
long_words = [word for word in s.split() if len(word) > 5]
print(long_words)

# 40. Используя zip(), объедините несколько списков и найдите среднее значение каждого набора значений.
a = [10, 20, 30]
b = [40, 50, 60]
c = [70, 80, 90]
averages = [sum(x)/len(x) for x in zip(a, b, c)]
print(averages)

# 41. Используйте set(), чтобы оставить только уникальные элементы в списке чисел.
lst = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(lst))
print(unique)

# 42. Запросите у пользователя строку и создайте множество уникальных символов.
s = input("Введите строку: ")
unique_chars = set(s)
print(unique_chars)

# 43. Используйте set(), чтобы найти пересечение двух списков чисел.
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common = set(a) & set(b)
print(common)

# 44. Используйте defaultdict() для создания словаря со значением по умолчанию.
from collections import defaultdict
d = defaultdict(int)
d['a'] += 1
d['b'] += 2
print(dict(d))

# 45. Создайте вложенный словарь, где ключ — имя человека, а значение — другой словарь с возрастом и городом проживания.
people = {
    "Айнура": {"возраст": 27, "город": "Бишкек"},
    "Нурбек": {"возраст": 32, "город": "Ош"},
    "Жанара": {"возраст": 24, "город": "Талас"}
}

print(people)


