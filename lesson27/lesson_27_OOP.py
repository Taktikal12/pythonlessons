
# Урок 27: Введение в ООП (Объектно-Ориентированное Программирование)

# 1. Что такое ООП (Объектно-Ориентированное Программирование)?
# ООП — это методология программирования, основанная на концепции объектов и классов.
# Классы представляют собой шаблоны для создания объектов.
# Объекты — это экземпляры классов, которые содержат данные (атрибуты) и методы для работы с этими данными.

# Пример:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# person1 = Person("John", 30)
# print(person1.greet())  # Output: Hello, my name is John and I am 30 years old.


# 2. Основные элементы ООП:
# Классы и объекты:
# Класс — это как шаблон для объектов.
# Объект — это экземпляр класса.

# Пример:

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# animal1 = Animal("Dog")
# print(animal1.speak())  # Output: Dog makes a sound.


# Конструктор __init__():
# Метод __init__ используется для инициализации объекта с атрибутами, которые он будет содержать.

# Пример:

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

# my_car = Car("Mercedes", "w223 amg6.3")
# print(my_car.make, my_car.model)  # Output: Toyota Corolla


# 3. Методы и атрибуты:
# Атрибуты — это переменные, которые хранят информацию о объекте.
# Методы — это функции, которые выполняют операции с атрибутами объекта.

# Пример:

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} barks!"

# dog1 = Dog("Buddy", "Golden Retriever")
# print(dog1.bark())  # Output: Buddy barks!


# 4. Подведение итогов:
# ООП является мощной концепцией, которая позволяет создавать гибкие и масштабируемые программы.
# В ООП важны классы и объекты как основные элементы. 
# В следующем уроке мы подробно рассмотрим инкапсуляцию, полиморфизм, наследование и абстракцию в ООП.




# Домашнее задание (Задачи для практики):
# 1. Создайте класс Car, который имеет атрибуты make (марка автомобиля), model (модель) и year (год выпуска).
# Добавьте метод get_car_info(), который выводит информацию о машине.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_car_info(self):
        return f"Car Info: {self.year} {self.make} {self.model}"

# car = Car("Mercedes", "w223 amg 6.3", 2025)
# print(car.get_car_info())  # Output: Car Info: 2022 Toyota Camry


# 2. Создайте класс Circle, который имеет атрибут radius (радиус).
# Добавьте методы для вычисления площади и периметра круга.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# circle = Circle(5)
# print(circle.area())  # Output: 78.53981633974483
# print(circle.perimeter())  # Output: 31.41592653589793


# 3. Создайте класс Rectangle, который имеет атрибуты width (ширина) и height (высота).
# Добавьте метод для вычисления площади прямоугольника.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# rectangle = Rectangle(10, 5)
# print(rectangle.area())  # Output: 50


# 4. Реализуйте полиморфизм, создав классы Bird и Fish, которые переопределяют метод move(),
# в котором будет описан способ передвижения (полет и плавание соответственно).

class Bird:
    def move(self):
        return "I fly in the sky!"

class Fish:
    def move(self):
        return "I swim in the water!"

# bird = Bird()
# fish = Fish()
# print(bird.move())  # Output: I fly in the sky!
# print(fish.move())  # Output: I swim in the water!


# 5. Создайте класс Person с атрибутами name и age. Реализуйте метод greet(), который будет возвращать приветствие.
# Используя наследование, создайте класс Student, который будет добавлять атрибут student_id и переопределит метод greet().

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old, and my student ID is {self.student_id}."

# student = Student("Alice", 20, "S1234")
# print(student.greet())  # Output: Hello, my name is Alice, I am 20 years old, and my student ID is S1234.


# ДЗ


# 1. **Класс «Круг»**
#    Создайте класс `Circle` с публичным атрибутом `radius` (радиус). Добавьте метод `area()`, возвращающий площадь круга (`π * radius**2`), и метод `circumference()`, возвращающий длину окружности (`2 * π * radius`).
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius  # Публичный атрибут

    def area(self):
        """Возвращает площадь круга"""
        return math.pi * self.radius ** 2

    def circumference(self):
        """Возвращает длину окружности"""
        return 2 * math.pi * self.radius

# c = Circle(5)
# print("Радиус:", c.radius)
# print("Площадь:", c.area())
# print("Длина окружности:", c.circumference())

# 2. **Класс «Студент»**
#    Определите класс `Student` с атрибутами `name` (имя) и `grades` (список оценок). Реализуйте методы:
#
#    * `add_grade(grade)` — добавить оценку в список;
#    * `average()` — вычислить и вернуть среднее арифметическое всех оценок.
class Student:
    def __init__(self, name):
        self.name = name         # Имя студента
        self.grades = []         # Список оценок (изначально пустой)

    def add_grade(self, grade):
        """Добавляет оценку в список"""
        self.grades.append(grade)

    def average(self):
        """Вычисляет и возвращает среднее арифметическое оценок"""
        if not self.grades:
            return 0  # Возвращаем 0, если оценок нет
        return sum(self.grades) / len(self.grades)

s = Student("Шабдан")
s.add_grade(5)
s.add_grade(4)
s.add_grade(3)

# print("Имя:", s.name, "Оценки:", s.grades, "Средний балл:", s.average())

# 3. **Класс «Вектор 2D»**
#    Напишите класс `Vector2D` с атрибутами `x` и `y`. Реализуйте «магические» методы:
#
#    * `__add__(other)` для сложения двух векторов;
#    * `__sub__(other)` для вычитания;
#    * `__repr__()` для удобного строкового представления.
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Сложение двух векторов"""
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Вычитание двух векторов"""
        return Vector2D(self.x - other.x, self.y - other.y)

    def __repr__(self):
        """Строковое представление вектора"""
        return f"Vector2D(x={self.x}, y={self.y})"

# v1 = Vector2D(2, 3)
# v2 = Vector2D(4, 1)
#
# print("v1:", v1)
# print("v2:", v2)
# print("v1 + v2:", v1 + v2)
# print("v1 - v2:", v1 - v2)

# 4. **Класс «Книга»**
#    Создайте класс `Book` с атрибутами `title`, `author` и `pages` (кол-во страниц). Добавьте метод `description()`, возвращающий строку:
#
#    ```
#    "<title> — автор <author>, <pages> стр."
#    ```
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        return f"{self.title} — автор {self.author}, {self.pages} стр."


# Создание книги "Атомные привычки"
atomic_habits = Book("Атомные привычки", "Джеймс Клир", 320)

# Вывод описания книги
# print(atomic_habits.description())

# 5. **Класс «Точка»**
#    Определите класс `Point` с координатами `x` и `y`. Добавьте метод `distance_to_origin()`, возвращающий расстояние от точки до начала координат, и метод `distance_to(other)`, возвращающий расстояние до другой точки.
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        """Возвращает расстояние от точки до начала координат (0, 0)"""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def distance_to(self, other):
        """Возвращает расстояние до другой точки"""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

# p1 = Point(3, 4)
# p2 = Point(6, 8)
#
# print("Расстояние от p1 до начала координат:", p1.distance_to_origin())
# print("Расстояние от p1 до p2:", p1.distance_to(p2))

# 6. **Класс «Конвертер температур»**
#    Напишите класс `TemperatureConverter` с двумя статическими методами (без использования `@classmethod`):
#
#    * `c_to_f(celsius)` — перевод из °C в °F;
#    * `f_to_c(fahrenheit)` — перевод из °F в °C.
class TemperatureConverter:
    @staticmethod
    def c_to_f(celsius):
        """Перевод из градусов Цельсия в Фаренгейты"""
        return (celsius * 9/5) + 32

    @staticmethod
    def f_to_c(fahrenheit):
        """Перевод из градусов Фаренгейта в Цельсии"""
        return (fahrenheit - 32) * 5/9

# print("25°C в °F:", TemperatureConverter.c_to_f(25))
# print("77°F в °C:", TemperatureConverter.f_to_c(77))

# 7. **Класс «Матрица 2×2»**
#    Создайте класс `Matrix2x2`, хранящий четыре числа `a, b, c, d`. Реализуйте методы:
#
#    * `determinant()` — вычисление определителя;
#    * `__mul__(other)` — умножение двух матриц 2×2.
class Matrix2x2:
    def __init__(self, a, b, c, d):
        # Матрица представляется как:
        # | a  b |
        # | c  d |
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def determinant(self):
        """Вычисляет определитель матрицы 2x2"""
        return self.a * self.d - self.b * self.c

    def __mul__(self, other):
        """Умножение двух матриц 2x2"""
        return Matrix2x2(
            self.a * other.a + self.b * other.c,
            self.a * other.b + self.b * other.d,
            self.c * other.a + self.d * other.c,
            self.c * other.b + self.d * other.d
        )

    def __repr__(self):
        """Удобное строковое представление"""
        return f"|{self.a} {self.b}|\n|{self.c} {self.d}|"

# m1 = Matrix2x2(1, 2, 3, 4)
# m2 = Matrix2x2(5, 6, 7, 8)
#
# print("Матрица m1:")
# print(m1)
# print("Определитель m1:", m1.determinant())
#
# print("\nМатрица m2:")
# print(m2)
# print("m1 * m2:")
# print(m1 * m2)

# 8. **Класс «Список покупок»**
#    Определите класс `ShoppingList` с атрибутом `items` (список строк). Реализуйте методы:
#
#    * `add(item)` — добавить товар;
#    * `remove(item)` — удалить товар по имени (если есть);
#    * `show()` — вывести все товары в виде нумерованного списка.
class ShoppingList:
    def __init__(self):
        self.items = []  # Список товаров

    def add(self, item):
        """Добавить товар в список"""
        self.items.append(item)

    def remove(self, item):
        """Удалить товар по имени, если он есть в списке"""
        if item in self.items:
            self.items.remove(item)

    def show(self):
        """Показать все товары с номерами"""
        if not self.items:
            print("Список покупок пуст.")
        else:
            for i, item in enumerate(self.items, start=1):
                print(f"{i}. {item}")

# my_list = ShoppingList()
# my_list.add("Хлеб")
# my_list.add("Молоко")
# my_list.add("Яйца")
# my_list.show()
#
# print("\nУдаляем 'Молоко'...")
# my_list.remove("Молоко")
# my_list.show()

# 9. **Класс «Комплексное число»**
#    Напишите класс `ComplexNumber` с атрибутами `real` и `imag`. Реализуйте методы:
#
#    * `__add__(other)` и `__mul__(other)` для сложения и умножения комплексных чисел;
#    * `__repr__()` для отображения в формате `"a + bi"` или `"a - bi"`.
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real  # Действительная часть
        self.imag = imag  # Мнимая часть

    def __add__(self, other):
        """Сложение двух комплексных чисел"""
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        """Умножение двух комплексных чисел"""
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __repr__(self):
        """Строковое представление в формате 'a + bi' или 'a - bi'"""
        sign = '+' if self.imag >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imag)}i"

# c1 = ComplexNumber(3, 4)
# c2 = ComplexNumber(1, -2)
#
# print("c1:", c1)
# print("c2:", c2)
# print("Сумма:", c1 + c2)
# print("Произведение:", c1 * c2)

# 10. **Класс «Счётчик»**
#     Создайте класс `Counter` с атрибутом `value`, инициализируемым в конструкторе. Добавьте методы:
#
#     * `increment()` — увеличить на 1;
#     * `decrement()` — уменьшить на 1;
#     * `reset()` — обнулить;
#     * `__repr__()` — вернуть текущее значение в виде строки.
class Counter:
    def __init__(self, value=0):
        self.value = value  # Начальное значение счётчика

    def increment(self):
        """Увеличить значение на 1"""
        self.value += 1

    def decrement(self):
        """Уменьшить значение на 1"""
        self.value -= 1

    def reset(self):
        """Сбросить значение до 0"""
        self.value = 0

    def __repr__(self):
        """Строковое представление текущего значения"""
        return str(self.value)

# c = Counter(10)
# print("Начальное значение:", c)
#
# c.increment()
# c.increment()
# print("После увеличений:", c)
#
# c.decrement()
# print("После уменьшения:", c)
#
# c.reset()
# print("После сброса:", c)

