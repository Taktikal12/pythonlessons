# === Урок 16: Расширенные возможности функций в Python ===

#   Аргументы функций:
# - позиционные аргументы: def f(x, y)
# - аргументы по умолчанию: def f(x=10)
# - переменное число позиционных аргументов: *args
# - переменное число именованных аргументов: **kwargs


#   Примеры аргументов по умолчанию:
# def greet(name="Гость"):
#     print(f"Привет, {name}!")


# greet("Анна")  # Привет, Анна
# greet()         # Привет, Гость


#   Пример *args: любое количество позиционных аргументов
# def multiply_all(*args):
#     print(args)
#     result = 1
#     for number in args:
#         result *= number
#     return result
#
#
# print(multiply_all(2, 3, 4))  # 24


#   Пример **kwargs: любое количество именованных аргументов
# def show_info(**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
#
# show_info(name="Иван", age=30, city="Москва")

#   Функции как объекты (их можно передавать в другие функции)

#   Вложенные функции (одна функция внутри другой)

#   Лямбда-функции — короткий способ записать функцию:
# def double2(y):
#     return x * 2
# # Пример:
# double = lambda x: x * 2
# print(double(5))  # 10

#   Функции высшего порядка — принимают функции как аргументы или возвращают функции
#   Область видимости переменных: глобальные и локальные, ключевые слова global и nonlocal

# Пример глобальной переменной:
x = 5


# def change_global():
#     global x
#     x = 10
#     print("x in function", x)
#
#
# print("x before function", x)
# change_global()
# print("x after function", x)  # 10


# Пример nonlocal:
# def outer():
#     y = 3
#
#     def inner():
#         nonlocal y
#         y += 2
#         print("Внутри inner:", y)
#     inner()
#     inner()
#     print("Внутри outer:", y)
#
#
# outer()

#   Декораторы:
# Декораторы — это функции, которые принимают другую функцию и возвращают новую функцию с дополнительным поведением.
# Обычно используются для логирования, проверки прав доступа, измерения времени выполнения и др.


# Пример простого декоратора:
# def my_decorator(func):
#     def wrapper():
#         print("До выполнения функции")
#         func()
#         print("После выполнения функции")
#     return wrapper
#
#
# @my_decorator
# def say_hi():
#     print("Привет!")
#
#
# say_hi()
# # Вывод:
# # До выполнения функции
# # Привет!
# # После выполнения функции
#
#
# # Декоратор с аргументами:
# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"Вызов функции {func.__name__} с аргументами: {args}, {kwargs}")
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @logger
# def add(a, b):
#     return a + b
#
#
# print(add(2, 3))
#
# # --- Ознакомительные задачи (10) ---

# 1. Напиши функцию, которая принимает любое количество чисел и возвращает их произведение.
def many(*args):
    print(args)
    result = 1
    for number in args:
        result *= number
    return result

print(many(3, 5, 7, 2))
# 2. Напиши функцию с именованными аргументами name и age, которая выводит: "Имя: ..., Возраст: ...".
def info_user(name=None, age=None):
    print(f"Name: {name}, Age: {age}")
# 3. Напиши функцию, которая принимает список и возвращает сумму только положительных чисел.
def num(*args):
    result = 0
    for number in args:
        if number > 0:
            result += number
    return result
    print(num([1, 2, 3, 4]))
# 4. Напиши лямбда-функцию, которая принимает число и возвращает его куб.
triple = lambda x: x ** 3
print(triple(3))
# 5. Напиши функцию, которая возвращает другую функцию, которая возводит число в квадрат.
def outer():
    x = 5
    def inner():
        nonlocal x
        x **= 2
        print(x)
    inner()
    print(x)
outer()
# 6. Напиши функцию, которая использует global для изменения глобальной переменной.
x = 25
def change_global():
    global x
    x = 40
    print(x)
change_global()
print(x)
# 7. Напиши функцию, которая принимает **kwargs и возвращает их ключи в списке.
def get_list(**kwargs):
    l = []
    for key in kwargs.keys():
        l.append(key)
    return l

print(get_list(apple = "Irlanda", grapes = "Kyrgyz"))
# 8. Напиши функцию, которая считает сумму всех чисел в списке с помощью вложенной функции.
def sum_of_numbers(numbers):
    def calculate_sum(nums):
        total = 0
        for num in nums:
            total += num
        return total

    return calculate_sum(numbers)
numbers = [1, 2, 3, 4, 5]
print(sum_of_numbers(numbers))
# 9. Напиши функцию, принимающую другую функцию и число, и возвращающую результат.
def apply_function(func, num):
    return func(num)
def square(x):
    return x ** 2
result = apply_function(square, 5)
print(result)
# 10. Напиши функцию, использующую nonlocal для изменения переменной во вложенной функции.
def outer_function():
    count = 0
    def inner_function():
        nonlocal count
        count += 1
        print(f"Count inside inner function: {count}")

    inner_function()
    return count
result = outer_function()
print(f"Count after calling outer function: {result}")

# --- Домашнее задание (40 задач) ---

# --- Дополнительные задачи по декораторам (10) ---

# 41. Напиши декоратор, который выводит 'Начало выполнения' и 'Конец выполнения' перед и после вызова функции.
# Пример: задекорируй функцию print_name(), которая печатает 'Алексей'.
def execution_decorator(func):
    def wrapper(*args, **kwargs):
        print('Начало выполнения')
        result = func(*args, **kwargs)
        print('Конец выполнения')
        return result
    return wrapper

@execution_decorator
def print_name():
    print('Алексей')

# print_name()

# 42. Напиши декоратор, который логирует аргументы и результат функции.
# Пример: задекорируй функцию multiply(a=3, b=4), которая возвращает произведение.
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Аргументы: args={args}, kwargs={kwargs}')
        result = func(*args, **kwargs)
        print(f'Результат: {result}')
        return result
    return wrapper

@log_decorator
def multiply(a, b):
    return a * b

# multiply(a=3, b=4)

# 43. Напиши декоратор, который запрещает вызов функции без аргументов.
# Пример: функция divide(a, b). Если не переданы аргументы — выводится сообщение об ошибке.
def no_empty_args(func):
    def wrapper(*args, **kwargs):
        if not args and not kwargs:
            print('Ошибка: аргументы не переданы.')
            return
        return func(*args, **kwargs)
    return wrapper

@no_empty_args
def divide(a, b):
    return a / b

# divide(10, 2), divide()

# 44. Напиши декоратор, который считает и выводит количество вызовов функции.
# Пример: задекорируй функцию hello(), вызывай её 3 раза.
def count_calls(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'Вызов №{count}')
        return func(*args, **kwargs)
    return wrapper

@count_calls
def hello():
    print('Привет!')

# hello(), hello(), hello()

# 45. Напиши декоратор, который ограничивает выполнение функции максимум 2 раза.
# Пример: задекорируй функцию greet(), которая просто печатает приветствие.
def max_two_calls(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        if count >= 2:
            print('Превышено число вызовов!')
            return
        count += 1
        return func(*args, **kwargs)
    return wrapper

@max_two_calls
def greet():
    print('Здравствуйте!')

# greet(), greet(), greet()

# 46. Напиши декоратор, который проверяет тип аргументов функции и вызывает её только если все аргументы — числа.
# Пример: функция add(a, b), вызов add(2, 'a') должен выводить сообщение об ошибке.
def numeric_only(func):
    def wrapper(*args, **kwargs):
        if not all(isinstance(x, (int, float)) for x in list(args) + list(kwargs.values())):
            print('Ошибка: все аргументы должны быть числами!')
            return
        return func(*args, **kwargs)
    return wrapper

@numeric_only
def add(a, b):
    return a + b

# add(2, 'a'), add(3, 5)

# 47. Напиши декоратор, который измеряет и выводит время выполнения функции.
# Пример: задекорируй функцию wait(), которая вызывает time.sleep(1).
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения: {end - start:.4f} сек')
        return result
    return wrapper

@timing_decorator
def wait():
    time.sleep(1)

# wait()

# 48. Напиши декоратор, который преобразует результат функции в строку.
# Пример: функция get_number() возвращает число 42, декоратор делает return '42'.
def to_string(func):
    def wrapper(*args, **kwargs):
        return str(func(*args, **kwargs))
    return wrapper

@to_string
def get_number():
    return 42

# print(get_number())  # '42'

# 49. Напиши декоратор, который к каждому выводу из функции добавляет '✔'.
# Пример: функция print_msg() выводит 'Успешно'. С декоратором — 'Успешно✔'.
def success_marker(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result + '✔'
        return result
    return wrapper

@success_marker
def print_msg():
    return 'Успешно'

# print(print_msg())  # Успешно✔

# 50. Напиши универсальный декоратор, который можно применить к любой функции и он будет выводить
# её имя и время запуска.
# Пример: задекорируй любую функцию, например def say_hello().
from datetime import datetime

def universal_logger(func):
    def wrapper(*args, **kwargs):
        print(f'Функция {func.__name__} запущена в {datetime.now()}')
        return func(*args, **kwargs)
    return wrapper

@universal_logger
def say_hello():
    print('Hello!')

# say_hello()

# 1. Функция, принимающая любое количество чисел и возвращающая максимум.
def max_of_all(*args):
    return max(args)
# 2. Функция, принимающая **kwargs и выводящая пары ключ: значение.
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
# 3. Функция, возвращающая список квадратов чисел из *args.
def squares(*args):
    return [x**2 for x in args]
# 4. Функция, возвращающая True, если в *args есть хотя бы одно чётное число.
def has_even(*args):
    return any(x % 2 == 0 for x in args)
# 5. Функция, принимающая строку и символ, возвращающая количество вхождений символа.
def count_char(s, char):
    return s.count(char)
# 6. Функция, возвращающая словарь: символ — количество его вхождений в строке.
def char_frequency(s):
    return {char: s.count(char) for char in set(s)}
# 7. Функция, принимающая список и возвращающая только уникальные значения.
def unique_values(lst):
    return list(set(lst))
# 8. Функция, которая принимает список строк и возвращает их объединение.
def join_strings(strings):
    return ''.join(strings)
# 9. Функция, возвращающая True, если слово палиндром.
def is_palindrome(word):
    return word == word[::-1]
# 10. Функция, проверяющая, все ли слова в списке начинаются с заглавной буквы.
def all_capitalized(words):
    return all(w.istitle() for w in words)
# 11. Функция, возвращающая список имён из **kwargs, где ключи — 'name1', 'name2', и т.д.
def extract_names(**kwargs):
    return [v for k, v in kwargs.items() if k.startswith('name')]
# 12. Лямбда-функция для получения остатка от деления числа на 3.
mod3 = lambda x: x % 3
# 13. Функция, которая принимает функцию и список, применяет функцию ко всем элементам и возвращает новый список.
def apply_func(func, lst):
    return [func(x) for x in lst]
# 14. Функция, возвращающая другую функцию, добавляющую префикс к строке.
def add_prefix(prefix):
    return lambda s: prefix + s
# 15. Функция, которая подсчитывает общее количество символов в строках списка.
def total_length(strings):
    return sum(len(s) for s in strings)
# 16. Функция, возвращающая сумму всех значений словаря.
def sum_dict_values(d):
    return sum(d.values())
# 17. Функция, которая преобразует все значения словаря в строки.
def values_to_str(d):
    return {k: str(v) for k, v in d.items()}
# 18. Функция, сортирующая словарь по длине ключей.
def sort_by_key_length(d):
    return dict(sorted(d.items(), key=lambda x: len(x[0])))
# 19. Функция, принимающая список чисел и возвращающая их в виде строки через точку с запятой.
def nums_to_string(lst):
    return ';'.join(str(x) for x in lst)
# 20. Функция, считающая количество чисел больше 10 в *args.
def count_gt_10(*args):
    return sum(1 for x in args if x > 10)
# 21. Функция, возвращающая True, если длина всех строк в списке больше 3.
def all_longer_than_3(words):
    return all(len(w) > 3 for w in words)
# 22. Функция, объединяющая списки, переданные через *args.
def merge_lists(*args):
    result = []
    for lst in args:
        result.extend(lst)
    return result
# 23. Функция, возвращающая минимальное значение в **kwargs.
def min_in_kwargs(**kwargs):
    return min(kwargs.values())
# 24. Функция, проверяющая, есть ли в списке строки, содержащие подстроку 'test'.
def contains_test(lst):
    return any('test' in s for s in lst)
# 25. Функция, применяющая функцию к каждому значению словаря.
def map_dict_values(d, func):
    return {k: func(v) for k, v in d.items()}
# 26. Функция, возвращающая количество параметров в **kwargs.
def count_kwargs(**kwargs):
    return len(kwargs)
# 27. Функция, принимающая список чисел и возвращающая их факториалы.
import math
def list_factorials(lst):
    return [math.factorial(x) for x in lst]
# 28. Функция, которая возвращает True, если хотя бы одно значение в словаре больше 100.
def any_value_gt_100(d):
    return any(v > 100 for v in d.values())
# 29. Функция, объединяющая строки из *args через пробел.
def join_args(*args):
    return ' '.join(args)
# 30. Функция, возвращающая True, если в **kwargs есть ключ 'email'.
def has_email(**kwargs):
    return 'email' in kwargs
# 31. Функция, возвращающая количество цифр в строке.
def count_digits(s):
    return sum(c.isdigit() for c in s)
# 32. Функция, проверяющая, входит ли строка в список (игнорируя регистр).
def string_in_list(s, lst):
    return s.lower() in [x.lower() for x in lst]
# 33. Функция, возвращающая True, если все значения в словаре уникальны.
def all_unique_values(d):
    return len(set(d.values())) == len(d.values())
# 34. Функция, принимающая список кортежей и возвращающая сумму второго элементов.
def sum_second_elements(pairs):
    return sum(y for x, y in pairs)
# 35. Функция, выводящая имя и возраст в формате: "Имя: ..., Возраст: ..." с помощью f-строки.
def print_name_age(name, age):
    print(f"Имя: {name}, Возраст: {age}")
# 36. Функция, создающая и возвращающая словарь из списка ключей и списка значений.
def create_dict(keys, values):
    return dict(zip(keys, values))
# 37. Функция, принимающая список слов и возвращающая количество слов длиной больше 5.
def count_long_words(words):
    return sum(1 for w in words if len(w) > 5)
# 38. Функция, проверяющая, начинается ли каждая строка в списке с заглавной.
def all_start_upper(lst):
    return all(s[0].isupper() for s in lst if s)
# 39. Функция, возвращающая True, если сумма всех чисел *args кратна 10.
def sum_divisible_by_10(*args):
    return sum(args) % 10 == 0
# 40. Функция, принимающая строку и возвращающая словарь с частотой каждого слова.
def word_frequency(s):
    words = s.split()
    return {word: words.count(word) for word in set(words)}

