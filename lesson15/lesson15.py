# === Урок 15: Функции в Python ===
from runpy import run_path


# --- Объяснение темы ---

# Функции — это блоки кода, которые можно переиспользовать.
# Они помогают структурировать программу, избегать повторений и повышать читаемость.

# Синтаксис определения функции:
# def имя_функции(аргументы):
#     блок_кода
#     return значение (необязательно)

# Пример:

# Функция без аргументов:
def say_hello():
    print("Привет, мир!")


say_hello()  # Вызов функции без аргументов


def greet(name):
    print(f"Привет, {name}!")


greet("Анна")  # Вызов функции


# Функция с возвратом значения:
def square(x):
    return x ** 2


result = square(5)
print(result)  # 25


# Функция с несколькими аргументами:
def add(a, b):
    return a + b


print(add(2, 3))  # 5


# Аргументы по умолчанию:
def greet_user(name="гость"):
    print(f"Привет, {name}!")

# --- Ознакомительные задачи (10) ---

# 1. Напиши функцию, которая выводит "Привет, мир!".
def say_hello():
    print("Привет, мир!")
# 2. Напиши функцию, которая принимает имя (например, 'Иван') и приветствует пользователя.
def greet(name):
    print(f"Привет, {name}")

greet("Иван")
# 3. Напиши функцию, которая возвращает квадрат числа (например, 4).
def square(x):
    return x ** 2

result = square(4)
print(result)
# 4. Напиши функцию, которая возвращает сумму двух чисел (например, 5 и 7).
def add(a, b):
    return a + b
print(add(5, 7))
# 5. Напиши функцию, которая проверяет, чётное число или нет (например, 10).
def num(x):
    return x % 2 == 0
print(num(10))
# 6. Напиши функцию, которая возвращает длину строки (например, 'python').
def get_length(s):
    return len(s)
print(get_length('python'))
# 7. Напиши функцию, которая принимает список (например, [1, 2, 3]) и возвращает его сумму.
zero = [1, 2, 3]
def sum_of_list(one):
    return sum(one)
result = sum_of_list(zero)
print(result)
# 8. Напиши функцию, которая принимает строку (например, 'hello') и возвращает строку в верхнем регистре.
def to_upprecase(a):
    return a.upper()
print(to_upprecase('hello'))
# 9. Напиши функцию, которая возвращает True, если число (например, 15) делится на 3 и 5.
a = 15
print()
# 10. Напиши функцию, которая принимает имя и возраст ('Анна', 25), и возвращает строку вида
# "Меня зовут ... мне ... лет".
name = "Анна"
age = 25
print(f"My name is {name} and I am {age} years old.")

# --- Домашнее задание (40 задач) ---

# 1. Функция, возвращающая разность двух чисел (например, 10 и 3).
def difference(a, b):
    return a - b
# 2. Функция, принимающая число (например, -7) и возвращающая его модуль.
def absolute_value(n):
    return abs(n)
# 3. Функция, проверяющая, является ли число (например, -5) отрицательным.
def is_negative(n):
    return n < 0
# 4. Функция, возвращающая максимальное из двух чисел (например, 5 и 8).
def maximum(a, b):
    return max(a, b)
# 5. Функция, возвращающая минимальное из трёх чисел (например, 3, 7, 2).
def minimum_of_three(a, b, c):
    return min(a, b, c)
# 6. Функция, возвращающая True, если строка (например, 'python is fun') содержит слово 'python'.
def contains_python(s):
    return 'python' in s.lower()
# 7. Функция, проверяющая, пустая строка или нет (например, '').
def is_empty(s):
    return s == ''
# 8. Функция, считающая количество символов в строке без пробелов (например, 'hello world').
def count_chars_no_spaces(s):
    return len(s.replace(' ', ''))
# 9. Функция, возвращающая True, если в строке (например, 'abc123') есть хотя бы одна цифра.
def has_digit(s):
    return any(char.isdigit() for char in s)
# 10. Функция, возвращающая строку наоборот (например, 'python' -> 'nohtyp').
def reverse_string(s):
    return s[::-1]
# 11. Функция, проверяющая, является ли число (например, 17) простым.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# 12. Функция, возвращающая все делители числа (например, 12 -> [1, 2, 3, 4, 6, 12]).
def divisors(n):
    return [i for i in range(1, n+1) if n % i == 0]
# 13. Функция, возвращающая факториал числа (например, 5 -> 120).
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
# 14. Функция, преобразующая список строк (например, ['cat', 'dog']) в список их длин.
def word_lengths(words):
    return [len(word) for word in words]
# 15. Функция, проверяющая, все ли элементы списка (например, [2, 4, 6]) чётные.
def all_even(lst):
    return all(x % 2 == 0 for x in lst)
# 16. Функция, считающая количество чётных чисел в списке (например, [1, 2, 3, 4, 5]).
def count_even(lst):
    return sum(1 for x in lst if x % 2 == 0)
# 17. Функция, возвращающая сумму квадратов всех чисел в списке (например, [1, 2, 3]).
def sum_of_squares(lst):
    return sum(x**2 for x in lst)
# 18. Функция, возвращающая True, если два слова (например, 'listen', 'silent') являются анаграммами.
def are_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)
# 19. Функция, принимающая список (например, [1, 2, 2, 3]) и возвращающая только уникальные элементы.
def unique_elements(lst):
    return list(set(lst))
# 20. Функция, соединяющая два списка без повторений (например, [1, 2], [2, 3] -> [1, 2, 3]).
def union_lists(lst1, lst2):
    return list(set(lst1 + lst2))
# 21. Функция, возвращающая среднее значение чисел из списка (например, [4, 8, 12]).
def average(lst):
    return sum(lst) / len(lst) if lst else 0
# 22. Функция, проверяющая, входит ли элемент (например, 5) в список [1, 3, 5, 7].
def contains_element(element, lst):
    return element in lst
# 23. Функция, принимающая строку (например, 'hello world') и возвращающая количество слов.
def count_words(s):
    return len(s.split())
# 24. Функция, удаляющая все пробелы из строки (например, 'hello world' -> 'helloworld').
def remove_spaces(s):
    return s.replace(' ', '')
# 25. Функция, преобразующая строку (например, 'one two three') в список слов.
def string_to_word_list(s):
    return s.split()
# 26. Функция, возвращающая True, если слово (например, 'madam') читается одинаково в обе стороны.
def is_palindrome(word):
    return word == word[::-1]
# 27. Функция, удаляющая дубликаты из списка (например, [1, 2, 2, 3]).
def remove_duplicates(lst):
    return list(set(lst))
# 28. Функция, заменяющая все гласные в строке (например, 'hello') на *.
def replace_vowels(s):
    return ''.join('*' if c.lower() in 'aeiou' else c for c in s)
# 29. Функция, проверяющая, все ли символы в строке (например, 'abc') уникальны.
def all_unique_chars(s):
    return len(set(s)) == len(s)
# 30. Функция, принимающая два числа (например, 3 и 7) и возвращающая список чисел между ними.
def numbers_between(a, b):
    return list(range(a + 1, b))
# 31. Функция, преобразующая список чисел (например, [1, 2, 3]) в строку '1,2,3'.
def list_to_string(lst):
    return ','.join(map(str, lst))
# 32. Функция, находящая максимальное и минимальное число в списке (например, [4, 2, 9]).
def max_and_min(lst):
    return max(lst), min(lst)
# 33. Функция, возвращающая True, если список (например, [1, 2, 3, 4]) отсортирован по возрастанию.
def is_sorted(lst):
    return lst == sorted(lst)
# 34. Функция, возвращающая количество положительных чисел в списке (например, [-2, 3, 4]).
def count_positive(lst):
    return sum(1 for x in lst if x > 0)
# 35. Функция, возвращающая произведение всех чисел в списке (например, [2, 3, 4]).
def product_of_list(lst):
    result = 1
    for x in lst:
        result *= x
    return result
# 36. Функция, объединяющая значения словаря (например, {'a': 'hi', 'b': 'there'}) в одну строку 'hithere'.
def concat_dict_values(d):
    return ''.join(str(v) for v in d.values())
# 37. Функция, сортирующая словарь (например, {'a': 3, 'b': 1}) по значениям.
def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))
# 38. Функция, принимающая строку (например, 'hello') и возвращающая словарь частот символов.
def char_frequencies(s):
    return {char: s.count(char) for char in set(s)}
# 39. Функция, возвращающая словарь квадратов чисел от 1 до N (например, N = 5).
def squares_up_to_n(n):
    return {i: i**2 for i in range(1, n+1)}
# 40. Функция, проверяющая, является ли введённый год (например, 2024) високосным.
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
