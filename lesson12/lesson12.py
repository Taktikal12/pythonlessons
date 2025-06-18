"""
Урок 12: Прерывание циклов (break, continue, else)
"""

# 1. break - досрочное завершение цикла
"""
Оператор break прерывает выполнение цикла и выходит из него.
"""
# for i in range(1, 11):
#     if i == 5:
#         print("Остановлено на", i)
#         break  # Выход из цикла при i == 5
#     print(i)  # Выведет 1, 2, 3, 4

# 2. continue - пропуск итерации текущего цикла
"""
Оператор continue пропускает текущую итерацию цикла и переходит к следующей.
"""
# for i in range(1, 6):
#     if i == 3:
#         continue  # Пропускаем число 3
#     print(i)  # Выведет 1, 2, 4, 5

# 3. else в циклах закончился без обрывов т,е без break
"""
Блок else выполняется, если цикл завершился без использования break.
"""
# for i in range(1, 6):
#     print(i)
# else:
#     print("Цикл завершился без прерываний")  # Этот код выполнится
#
# print()

# for i in range(1, 6):
#     if i == 3:
#         break  # Прерываем цикл
#     print(i)
# else:
#     print("Этот код не выполнится, так как цикл прерван")

# ОЗНАКОМИТЕЛЬНЫЕ ЗАДАЧИ (10 штук)

# 1. Используя break, прервите цикл при достижении числа 7.
# for i in range(1, 9):
#     if i == 7:
#         print("Остановлено на", i)
#         break
#     print(i)

# 2. Используя continue, пропустите число 4 в цикле от 1 до 10.
# for i in range(1, 10):
#     if  i == 4:
#         continue
#     print(i)
# 3. Выведите все числа от 1 до 10, но остановитесь при первом четном числе.
# for i in range(1, 11):
#     print(i)
#     if i % 2 == 0:
#         break
# 4. Найдите первое число, делящееся на 7 в диапазоне 10-100.
# for i in range(10, 101):
#     if  i % 7 == 0:
#         print(i)
#         break
# 5. Используйте else в цикле, чтобы определить, было ли найдено число 5 в списке [1, 2, 3, 6, 7].
# num = [1, 2, 3, 4, 6, 7]
# target = 5
# for num in num:
#     if num == target:
#         print("Число найден!")
#         break
# else:
#     print("Число не найден.")
# 6. Выведите все буквы слова "Python", кроме "o".
# for i in "Python":
#     if i == 'o':
#         continue
#     print(i, end='')
# 7. Используйте continue, чтобы вывести все нечетные числа от 1 до 20.
# for i in range(1, 21):
#     if 1 % 2 == 0:
#         continue
# print (1)
# 8. Используйте break, чтобы найти первое число, кратное 13 в диапазоне 1-100.
# for i in range(1, 100):
#     if  i % 13 == 0:
#         print(i)
#         break
# 9. Используйте else в while-цикле, чтобы определить, был ли завершен поиск числа.
# lst = list(range(1, 21))
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# i = 0
# while i < len(lst):
#     if lst[i] == 10:
#         print("10 found")
#         break
#     print(lst[i])
#     i += 1
# else:
#     print("No 10 found")

# 10. Напишите программу, которая завершает ввод пользователя после слова "стоп".


# ДОМАШНЕЕ ЗАДАНИЕ (40 задач)

# 1. Прервите цикл, если пользователь ввел отрицательное число.
while True:
    bintang = int(input("Введите число (для выхода введите отрицательное число):"))
    if bintang < 9:
        print("Вы ввели отрицательное число")
        break
    print("Вы ввели: {bintang}")
# 2. Используйте continue, чтобы пропустить все гласные буквы в введенной строке.
s = input("Введите строку: ")
vowels = 'aeiouAEIOU'
for char in s:
    if char in vowels:
        continue
    print(char, end='')
# 3. Напишите программу, которая запрашивает у пользователя числа, суммируя их, пока не введено 0.
total = 0
while True:
    num = int(input("Введите число (0 для выхода): "))
    if num == 0:
        break
    total += num
print("Сумма:", total)

# 4. Найдите первое число больше 50, которое делится на 9 без остатка.
for i in range(51, 1000):
    if i % 9 == 0:
        print(i)
        break

# 5. Выведите все числа от 10 до 1, пропуская числа, делящиеся на 3.
for i in range(10, 0, -1):
    if i % 3 == 0:
        continue
    print(i)

# 6. Проверьте, содержит ли список число 10, используя else в for.
lst = [1, 5, 8, 9]
for x in lst:
    if x == 10:
        print("Есть 10")
        break
else:
    print("10 не найдено")

# 7. Выведите только четные числа из списка [1, 3, 4, 7, 8, 10].
lst = [1, 3, 4, 7, 8, 10]
for num in lst:
    if num % 2 == 0:
        print(num)

# 8. Найдите первый символ "а" в строке и завершите поиск.
s = input("Введите строку: ")
for char in s:
    if char == 'a':
        print("Найдена 'a'")
        break

# 9. Прервите цикл, если число из списка [2, 4, 6, 8, 9] делится на 5.
lst = [2, 4, 6, 8, 9]
for num in lst:
    if num % 5 == 0:
        break
    print(num)

# 10. Выведите первые 5 чисел Фибоначчи, но остановитесь, если встретите число больше 10.
a, b = 0, 1
count = 0
while count < 5:
    if a > 10:
        break
    print(a)
    a, b = b, a + b
    count += 1

# 11. Напишите программу, которая ищет первое четное число в списке и прекращает выполнение.
lst = [1, 3, 7, 8, 5]
for num in lst:
    if num % 2 == 0:
        print("Первое четное:", num)
        break

# 12. Используйте while, чтобы выводить числа от 100 до 1, пропуская числа, делящиеся на 5.
i = 100
while i >= 1:
    if i % 5 == 0:
        i -= 1
        continue
    print(i)
    i -= 1

# 13. Используйте break в бесконечном цикле, если число больше 100.
while True:
    num = int(input("Введите число: "))
    if num > 100:
        print("Завершено")
        break

# 14. Переберите список и пропустите все элементы, содержащие букву "e".
lst = ["apple", "dog", "tree", "sun"]
for item in lst:
    if 'e' in item:
        continue
    print(item)

# 15. Используйте else в цикле while, который завершится без break.
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Цикл завершился без break")

# 16. Найдите первое число, большее 1000, которое делится на 37 без остатка.
i = 1001
while True:
    if i % 37 == 0:
        print(i)
        break
    i += 1

# 17. Запросите у пользователя пароль и прекратите цикл, если введен правильный пароль.
correct = "python123"
while True:
    pwd = input("Введите пароль: ")
    if pwd == correct:
        print("Доступ разрешён")
        break

# 18. Используйте continue, чтобы пропускать числа, которые делятся на 4.
for i in range(1, 21):
    if i % 4 == 0:
        continue
    print(i)

# 19. Прервите цикл, если сумма всех чисел превысила 200.
total = 0
for i in range(1, 100):
    total += i
    if total > 200:
        print("Сумма превысила 200 на числе:", i)
        break

# 20. Выведите таблицу умножения на 9, но прекратите после 9 x 5.
for i in range(1, 11):
    if i > 5:
        break
    print(f"9 x {i} = {9 * i}")

# 21. Найдите первую букву в строке, которая не является заглавной.
s = input("Введите строку: ")
for ch in s:
    if not ch.isupper():
        print("Первая не заглавная:", ch)
        break

# 22. Переберите список имен и пропустите все, которые начинаются на "A".
names = ["Alice", "Bob", "Anna", "Tom"]
for name in names:
    if name.startswith("A"):
        continue
    print(name)

# 23. Используйте break, чтобы прервать выполнение при нахождении простого числа.
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

nums = [4, 6, 8, 11, 12]
for n in nums:
    if is_prime(n):
        print("Найдено простое число:", n)
        break

# 24. Используйте else в цикле for, чтобы проверить, все ли числа четные.
lst = [2, 4, 6, 8]
for x in lst:
    if x % 2 != 0:
        print("Есть нечётное")
        break
else:
    print("Все числа чётные")

# 25. Запросите у пользователя числа, и прекратите ввод, если сумма превысила 1000.
total = 0
while True:
    num = int(input("Введите число: "))
    total += num
    if total > 1000:
        print("Сумма превысила 1000")
        break

# 26. Переберите все цифры числа и остановитесь, если встретите 7.
num = 123756
for ch in str(num):
    print(ch)
    if ch == '7':
        break
# 27. Напишите программу, которая ищет первое четное число среди случайных чисел.
import random
nums = [random.randint(1, 100) for _ in range(10)]
for n in nums:
    if n % 2 == 0:
        print("Чётное:", n)
        break

# 28. Используйте continue, чтобы пропустить числа, оканчивающиеся на 5.
for i in range(1, 51):
    if i % 10 == 5:
        continue
    print(i)
# 29. Выведите буквы слова "Programming", пропуская гласные.
for ch in "Programming":
    if ch.lower() in 'aeiou':
        continue
    print(ch, end='')
print()
# 30. Напишите игру, где пользователь вводит числа, и проигрывает при вводе отрицательного числа.
while True:
    n = int(input("Введите число: "))
    if n < 0:
        print("Вы проиграли!")
        break
# 31. Выведите все делители числа 100, но прекратите при нахождении первого простого делителя.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(1, 101):
    if 100 % i == 0:
        print(i)
        if is_prime(i):
            break
# 32. Найдите сумму всех цифр числа, но прекратите, если цифра равна 0.
num = 1234056
total = 0
for ch in str(num):
    if ch == '0':
        break
    total += int(ch)
print("Сумма:", total)
# 33. Переберите список дат и прекратите выполнение, если встретится 1 января.
dates = ["31 декабря", "1 января", "2 января"]
for date in dates:
    print(date)
    if date == "1 января":
        break
# 34. Используйте while для проверки пароля, запрашивая ввод, пока он не будет правильным.
while input("Пароль: ") != "1234":
    print("Неверный пароль")
# 35. Найдите первую букву в строке, которая является заглавной, и прекратите выполнение.
s = "hello World"
for ch in s:
    if ch.isupper():
        print("Заглавная:", ch)
        break
# 36. Прервите цикл, если встречается два подряд идущих одинаковых числа.
nums = [1, 2, 3, 3, 4]
for i in range(len(nums) - 1):
    if nums[i] == nums[i+1]:
        print("Повтор:", nums[i])
        break
# 37. Используйте break для выхода из вложенного цикла, если сумма элементов превышает 50.
matrix = [[10, 20], [15, 40], [30, 25]]
for row in matrix:
    s = sum(row)
    if s > 50:
        print("Сумма > 50:", s)
        break
# 38. Переберите числа от 1 до 100, останавливаясь на первом числе, делящемся на 17.
for i in range(1, 101):
    if i % 17 == 0:
        print("Найдено:", i)
        break

# 39. Используйте continue для пропуска всех слов, содержащих букву "z".
words = ["apple", "pizza", "orange", "zebra", "mango"]
for word in words:
    if 'z' in word:
        continue
    print(word)
# 40. Переберите список и прекратите выполнение, если элемент встречается второй раз.
items = [1, 2, 3, 2, 4]
seen = set()
for item in items:
    if item in seen:
        print("Повтор:", item)
        break
    seen.add(item)

# Дополнительные задачи с вложенными циклами
# 1. Нарисуйте треугольник из символов "*" с помощью вложенного цикла.
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
# 2. Создайте шахматную доску 8x8, используя символы "#" и ".".
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("#", end="")
        else:
            print(".", end="")
    print()
# 3. Переберите числа от 1 до 100 и найдите первую пару чисел, сумма которых равна 50.
found = False
for i in range(1, 100):
    for j in range(1, 100):
        if i + j == 50:
            print("Пара:", i, j)
            found = True
            break
    if found:
        break
# 4. Переберите строку и найдите первую букву, которая встречается дважды.
s = "abacabad"
seen = set()
for ch in s:
    if ch in seen:
        print("Повторная буква:", ch)
        break
    seen.add(ch)
# 5. Переберите список списков и найдите первый вложенный список, содержащий отрицательное число.
lists = [[1, 2], [3, 4], [-1, 5], [6, 7]]
for sublist in lists:
    for n in sublist:
        if n < 0:
            print("Список с отрицательным:", sublist)
            break
    else:
        continue
    break
