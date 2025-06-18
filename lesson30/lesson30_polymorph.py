"""
Основные виды полиморфизма в Python:
1. Ad-hoc полиморфизм (перегрузка операторов и функций)
2. Параметрический полиморфизм (дженерики)
3. Полиморфизм подтипов (наследование)

Полиморфизм — это возможность объектов с одинаковым интерфейсом использовать разные реализации.
Это один из основных принципов ООП, который делает код гибким и удобным для расширения.

Проявления полиморфизма:
- Полиморфизм функций/методов — одна и та же функция может работать с разными типами.
- Полиморфизм классов — один и тот же метод/интерфейс работает по-разному в разных классах.

Duck typing (утиная типизация): "Если объект выглядит как утка и крякает как утка, то это утка".
В Python важна не принадлежность к классу, а наличие нужных методов.

"""

# "\n=== 1.2.1 Встроенный полиморфизм ==="
# print("5 + 3 =", 5 + 3)  # Сложение чисел
# print("'Hello' + '!' =", "Hello" + "!")  # Конкатенация строк
# print("[1, 2] + [3] =", [1, 2] + [3])  # Объединение списков



# Полиморфизм с разными типами данных
def process(data):
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, list):
        return [process(item) for item in data]
    elif isinstance(data, dict):
        return {k: process(v) for k, v in data.items()}
    else:
        return data

# print("Пример 1:")
# print(process("hello"))
# print(process(["hello", "world"]))
# print(process({"a": "hello", "b": "world"}))
# print()



# "=== 1.2.2 Полиморфизм через наследование ==="


class Animal:
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Гав!"


class Cat(Animal):
    def make_sound(self):
        return "Мяу!"


# animals = [Dog(), Cat()]
# for animal in animals:
#     print(f"{animal.__class__.__name__}: {animal.make_sound()}")

# Создайте функцию my_max() и my_mmin() которая может принимать:
# 1. Список чисел (int, float)
# 2. Список строк (string)
# 3. Строку (string)

def my_max(data):
    max_value = ""
    if isinstance(data, str) and len(data) > 0:
        max_value = data[0]
        # Hello World
        # max_value = "H"
        # char = "e"
        for char in data:
            print(ord(char), char)
            if char > max_value:
                max_value = char
    elif isinstance(data, list):
        print("list")
    return max_value

def my_min(data):
    pass

print(my_max([1, 2, 3]), " == ", max([1, 2, 3]))
print(my_max(["a", "b", "c"]), " == ", max(["a", "b", "c"]))
print(my_max(["Hello World!"]), " == ", max(["Hello World!"]))

# print(my_min([1, 2, 3]), " == ", min([1, 2, 3]))
# print(my_min(["a", "b", "c"]), " == ", min(["a", "b", "c"]))
# print(my_min(["Hello World!"]), " == ", min(["Hello World!"]))


# ========================
# 2. ПРАКТИЧЕСКИЕ ЗАДАНИЯ
# ========================

# "\n=== 2.1 Задания на понимание полиморфизма ==="
# "1. Создайте классы Bird и Fish с методом move(). У птицы метод должен возвращать 'Летит', у рыбы — 'Плывет'.",
class Animal:
    def move(self):
        pass

class Bird(Animal):
    def move(self):
        return 'Летит'

class Fish(Animal):
    def move(self):
        return 'Плывет'

animals = [Bird(), Fish()]
for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.move()}")
# "2. Перегрузите оператор * для класса String, чтобы он повторял строку N раз.",

class String:
    def __init__(self, value):
        self.value = str(value)

    def __mul__(self, n):
        if isinstance(n, int):
            return String(self.value * n)
        raise TypeError("Ожидалось целое число справа от оператора *")

    def __rmul__(self, n):
        return self.__mul__(n)

    def __str__(self):
        return self.value

    def __repr__(self):
        return f'String("{self.value}")'

s = String("Привет ")
print(s * 3)
print(2 * s)

# "3. Напишите функцию multiply(a, b), которая работает для чисел (умножение) и строк (повторение a b раз).",
def multiply(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b
    elif isinstance(a, str) and isinstance(b, int):
        return a * b
    elif isinstance(b, str) and isinstance(a, int):
        return b * a
    else:
        raise TypeError("Unsupported operand types for multiply(): '{}' and '{}'".format(type(a).__name__, type(b).__name__))

print(multiply(3, 4))
print(multiply("abc", 3))
print(multiply(2, "xy"))

# "5. Реализуйте полиморфное поведение в классе Calculator с методом add(a, b) (должен работать с числами и строками).",
class Calculator:
    def add(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        else:
            raise TypeError("Unsupported operand types for add(): '{}' and '{}'".format(type(a).__name__, type(b).__name__))

calc = Calculator()

print(calc.add(5, 7))         # 12
print(calc.add("Hello, ", "world!"))  # "Hello, world!"
print(calc.add(3.5, 2.1))     # 5.6

# "6. Создайте абстрактный класс Device с методом turn_on() и реализуйте его в Lamp и Computer.",
from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Lamp(Device):
    def turn_on(self):
        print("Лампа включена. Светло!")

class Computer(Device):
    def turn_on(self):
        print("Компьютер включен. Загрузка системы...")

devices = [Lamp(), Computer()]

for device in devices:
    device.turn_on()

# "7. Напишите функцию print_length(obj), которая выводит длину строки, списка или кортежа.",
def print_length(obj):
    if isinstance(obj, (str, list, tuple)):
        print(f"Длина: {len(obj)}")
    else:
        print("Объект не поддерживает операцию определения длины.")

print_length("Привет")
print_length([1, 2, 3])
print_length((10, 20))
print_length(42)

# "8. Перегрузите метод __str__ в классах Book и Author, чтобы они выводили разную информацию.",
class Author:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f"Автор: {self.name} ({self.country})"


class Book:
    def __init__(self, title, author: Author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Книга: \"{self.title}\" ({self.year}), {self.author.name}"

author = Author("Лев Толстой", "Россия")
book = Book("Война и мир", author, 1869)

print(author)
print(book)

# "9. Создайте класс Playable с методом play() и реализуйте его в Audio и Video.",
from abc import ABC, abstractmethod

class Playable(ABC):
    @abstractmethod
    def play(self):
        pass

class Audio(Playable):
    def __init__(self, title):
        self.title = title

    def play(self):
        print(f"Воспроизведение аудио: {self.title}")

class Video(Playable):
    def __init__(self, title):
        self.title = title

    def play(self):
        print(f"Воспроизведение видео: {self.title}")

media = [Audio("Музыка.mp3"), Video("Фильм.mp4")]

for item in media:
    item.play()

# "10. Напишите функцию concat(a, b), которая складывает числа и объединяет строки."
def concat(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    else:
        raise TypeError(f"Нельзя объединить объекты типов {type(a).__name__} и {type(b).__name__}")

print(concat(2, 3))
print(concat("Hello, ", "world!"))
print(concat(3.5, 2.5))
# print(concat("123", 456))


#  2.2 Задания на применение полиморфизма в ООП
# "11. Создайте иерархию классов Transport (с методом move()), реализовав его в Car, Boat, Airplane.",
from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Transport):
    def move(self):
        print("Машина едет по дороге.")

class Boat(Transport):
    def move(self):
        print("Лодка плывет по воде.")

class Airplane(Transport):
    def move(self):
        print("Самолет летит по небу.")

# "12. Реализуйте полиморфное поведение в методе draw() для классов Circle, Square, Triangle.",
class Circle:
    def draw(self):
        print("Рисуем круг.")

class Square:
    def draw(self):
        print("Рисуем квадрат.")

class Triangle:
    def draw(self):
        print("Рисуем треугольник.")

# "13. Создайте класс Database с абстрактным методом connect() и реализуйте его в MySQL и PostgreSQL.",
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQL(Database):
    def connect(self):
        print("Подключение к базе данных MySQL.")

class PostgreSQL(Database):
    def connect(self):
        print("Подключение к базе данных PostgreSQL.")

# "14. Напишите функцию process_data(data), которая работает с int, str и list по-разному.",
def process_data(data):
    if isinstance(data, int):
        print(f"Удвоенное число: {data * 2}")
    elif isinstance(data, str):
        print(f"Строка в верхнем регистре: {data.upper()}")
    elif isinstance(data, list):
        print(f"Количество элементов в списке: {len(data)}")
    else:
        print("Неподдерживаемый тип данных.")

# "15. Создайте класс Logger с методом log() и переопределите его в FileLogger и ConsoleLogger.",
class Logger:
    def log(self, message):
        print(f"[Лог] {message}")

class FileLogger(Logger):
    def log(self, message):
        print(f"[Файл] Запись в файл: {message}")

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"[Консоль] {message}")

# "16. Реализуйте __add__ в классе Matrix для сложения матриц.",
class Matrix:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ]
        return Matrix(result)

    def __str__(self):
        return '\n'.join(str(row) for row in self.data)

# "17. Создайте класс Payment с методом pay() и реализуйте его в CreditCard, PayPal, Crypto.",
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Оплата {amount}₽ с помощью кредитной карты.")

class PayPal(Payment):
    def pay(self, amount):
        print(f"Оплата {amount}₽ через PayPal.")

class Crypto(Payment):
    def pay(self, amount):
        print(f"Оплата {amount}₽ криптовалютой.")

# "18. Напишите функцию compare(a, b), которая сравнивает числа, строки и списки.",
def compare(a, b):
    if type(a) == type(b):
        if a == b:
            print("Объекты равны.")
        else:
            print("Объекты не равны.")
    else:
        print("Объекты разных типов и не сравниваются.")

# "19. Создайте класс Animal с методом speak() и переопределите его в Dog, Cat, Cow.",
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Собака говорит: Гав!")

class Cat(Animal):
    def speak(self):
        print("Кошка говорит: Мяу!")

class Cow(Animal):
    def speak(self):
        print("Корова говорит: Муу!")

# "20. Реализуйте __mul__ в классе Fraction для умножения дробей."
from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self._reduce()

    def _reduce(self):
        g = gcd(self.numerator, self.denominator)
        self.numerator //= g
        self.denominator //= g

    def __mul__(self, other):
        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

"""
=== 4.1 Итоги урока ===
- Полиморфизм позволяет использовать одинаковые методы для разных типов
- В Python реализуется через:
  * Перегрузку операторов (__add__, __mul__ и др.)
  * Наследование и переопределение методов
- Делает код более гибким и расширяемым
"""
