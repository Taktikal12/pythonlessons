# 🔢 Упражнения с целыми числами (int)
# print("\n🔢 Упражнения с целыми числами")
#
# 1️⃣ Преобразование и вычисления
# print("\n1️⃣ Преобразование и вычисления")
# - Преобразуйте строку "250" в целое число.
# - Преобразуйте число с плавающей точкой 14.75 в целое число.
# - Сложите оба числа и выведите результат.

# Ваш код здесь
s = "250"
n = int(s)
print(type(s))
print(type(n))

float_ = 14.75
float1 = int(float_)
print(type(float1))
print(float1)

e = n + float1
print(e)

# 2️⃣ Поиск максимального и минимального значения
# print("\n2️⃣ Поиск максимального и минимального значения")
# - Даны числа: 45, 12, 89, 32, 67.
# - Найдите:
#   - Максимальное значение.
#   - Минимальное значение.

# Ваш код здесь
print(max( 45, 12, 89, 32, 67))
print(min( 45, 12, 89, 32,67))

# 3️⃣ Возведение в степень
# print("\n3️⃣ Возведение в степень")
# - Вычислите 3 в степени 4 с помощью pow().
# - Сделайте то же самое с помощью **.

# Ваш код здесь
print(pow(3, 4))
print(3 ** 4)

# 4️⃣ Абсолютное значение и округление
# print("\n4️⃣ Абсолютное значение и округление")
# - Найдите абсолютное значение числа -100.
# - Округлите 5.786 до 2 десятичных знаков.

# Ваш код здесь
num = -100
print(abs(num))
num1 = 5.786
print(round(num1, 2))

# 🟡 Упражнения с числами с плавающей точкой (float)
# print("\n🟡 Упражнения с float")

# 5️⃣ Преобразование строки в число с плавающей точкой
# print("\n5️⃣ Преобразование строки в float")
# - Преобразуйте строку "45.99" в float.
# - Преобразуйте 18 (целое число) в float.
# - Сложите оба числа и выведите результат.

# Ваш код здесь
shabdan = "45.99"
num = float(shabdan)
n1 = 18
n2 = float(n1)
print(num + n1)

# 6️⃣ Округление чисел
# print("\n6️⃣ Округление чисел")
# - Округлите 9.8765 до 3 десятичных знаков.
# - Округлите 7.4 до ближайшего целого числа.

# Ваш код здесь

num3 = 9.8765
print(round(num3, 3))
float2 = 7.4
float3 = int(float2)
print(type(float3))
print(float3)

# 🔠 Упражнения со строками (str)
# print("\n🔠 Упражнения со строками")

# 7️⃣ Изменение регистра строки
# print("\n7️⃣ Изменение регистра строки")
# - Преобразуйте строку "python programming" в:
#   - ВЕРХНИЙ РЕГИСТР.
#   - нижний регистр.
#   - Заглавные слова (Title case).

# Ваш код здесь

text = "  West Cost  "
print("Uppercase:", text.upper())
print("Lowercase:",text.lower())
print("Title Case:", text.title())

# 8️⃣ Удаление лишних пробелов
# print("\n8️⃣ Удаление лишних пробелов")
# - Дана строка "   Code in Python   ":
#   - Удалите пробелы слева.
#   - Удалите пробелы справа.
#   - Удалите пробелы с обеих сторон.

# Ваш код здесь

text = "   Snoop Dogg   "
print("Left stripped:", text.lstrip())
print("Right stripped:", text.rstrip())
print("Stripped spaces:", text.strip())


# 9️⃣ Поиск и замена в строке
# print("\n9️⃣ Поиск и замена в строке")
# - Дана строка "Learning Python is fun":
#   - Найдите индекс слова "Python".
#   - Замените "fun" на "awesome".

# Ваш код здесь

text = "Learning Python is fun"
print("Index of 'Python':", text.find("Python"))
print("Replace 'fun' with 'awesome':", text.replace("fun", "awesome"))

# 🔟 Разделение и объединение строк
# print("\n🔟 Разделение и объединение строк")
# - Преобразуйте строку "apple,banana,grape" в список.
# - Объедините список обратно в строку, разделяя элементы с помощью " | ".

# Ваш код здесь
fruits = "apple,banana,grape"
words = fruits.split(",")
print("Split string:", words)
print("Joined string:", "|".join(words))

# 1️⃣1️⃣ Проверка содержимого строки
# print("\n1️⃣1️⃣ Проверка содержимого строки")
# - Проверьте, состоит ли "54321" только из цифр.
# - Проверьте, является ли "Hello123" буквенно-цифровым значением.
# - Проверьте, состоит ли "PYTHON" только из заглавных букв.

# Ваш код здесь

print("Is '54321' all digits?:", "54321".isdigit())
print("Is 'Hello123' alphanumeric?:", "Hello123".isalnum())
print("PYTHON".isupper())

# 1️⃣2️⃣ Форматирование строк с помощью f-строк
# print("\n1️⃣2️⃣ Форматирование строк с f-strings")
# - Сохраните "David" в переменную name.
# - Сохраните 30 в переменную age.
# - Выведите строку "Меня зовут David, и мне 30 лет." с помощью f-строк.

# Ваш код здесь

name = "David"
age = 30
print(f"My name is {name} and I am {age} years old.")

# 🔵 Упражнения с булевыми значениями (bool)
# print("\n🔵 Упражнения с bool")

# 1️⃣3️⃣ Преобразование значений в булево
# print("\n1️⃣3️⃣ Преобразование значений в bool")
# - Определите булево значение для:
#   - 0
#   - 1
#   - "" (пустая строка)
#   - "Hello"
#   - None
#   - [] (пустой список)
#   - [1, 2, 3] (непустой список)

# Ваш код здесь

print("Boolean of 0:", bool(0))
print("Boolean of 1:", bool(1))
print("Boolean of empty string:", bool(""))
print("Boolean of non-empty string:", bool("Hello"))
print("Boolean of None:", bool(None))
print("Boolean of empty list:", bool([]))
print("Boolean of non-empty list:", bool([1, 2, 3]))

# 1️⃣4️⃣ Булева логика
# print("\n1️⃣4️⃣ Булева логика")
# - Даны:
#   x = True
#   y = False
#   - Найдите результат выражений:
#     - x and y
#     - x or y
#     - not x

# Ваш код здесь

x = True
y = False
print(x and y)
print(x or y)
print(not x)

# 🎯 Дополнительное задание: ввод данных и проверка возраста
# print("\n🎯 Дополнительное задание: ввод данных и проверка возраста")
#
# - Попросите пользователя ввести его имя.
# - Попросите ввести возраст (в виде строки, затем преобразуйте в целое число).
# - Проверьте, исполнилось ли пользователю 18 лет, и выведите:
#   - "Вы совершеннолетний", если возраст >= 18.
#   - "Вы несовершеннолетний" в противном случае.
# - Отформатируйте вывод с помощью f-строки.
#
# Ваш код здесь

username = input("Enter username:")
print("Username is: " + username)
userage = int(input("Enter userage:"))
print(type(userage))
if userage > 18:
    print(f"Вы совершеннолетний")
else:
  print(f"Вы несовершеннолетний")
