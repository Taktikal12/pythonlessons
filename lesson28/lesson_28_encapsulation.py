### Инкапсуляция в ООП (Объектно-Ориентированном Программировании)

# **Инкапсуляция** — это принцип ООП, который заключается в скрытии внутренней реализации объекта от внешнего мира и предоставлении
# доступа к данным и методам объекта только через специально определённые интерфейсы.
#
# Этот принцип позволяет:
#
# 1. Защитить данные от прямого изменения, обеспечив контроль над тем, как данные используются.
# 2. Сделать код более гибким и безопасным, так как изменения в одной части программы не повлияют на другие.
# 3. Спрятать детали реализации объекта, оставив только необходимые интерфейсы для работы с ним.
#
# ### Пример 1: Простая инкапсуляция с использованием геттеров и сеттеров
#
# В этом примере создадим класс `Person`, который инкапсулирует возраст человека, чтобы нельзя было установить отрицательное значение для возраста.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Приватный атрибут

    # Геттер для получения возраста
    def get_age(self):
        return self.__age

    # Сеттер для установки возраста с проверкой
    def set_age(self, age):
        if age < 0:
            print("Возраст не может быть отрицательным.")
        else:
            self.__age = age

# Создание объекта
person = Person("John", 25)

# Доступ к возрасту через методы
# print(person.get_age())  # 25

# Попытка установить неправильный возраст
# person.set_age(-5)  # Возраст не может быть отрицательным.

# Установка корректного возраста
# person.set_age(30)
# print(person.get_age())  # 30

# **Объяснение:**
#
# * Приватный атрибут `__age` не доступен напрямую извне класса.
# * Используем методы `get_age` и `set_age` для безопасного получения и изменения значения возраста. Метод `set_age` проверяет корректность значения перед установкой.

### Пример 2: Инкапсуляция с приватным методом

# В следующем примере создадим класс `BankAccount`, который инкапсулирует балансы и методы для их изменения.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Приватный атрибут

    # Геттер для получения баланса
    def get_balance(self):
        return self.__balance

    # Приватный метод для обновления баланса
    def __update_balance(self, amount):
        self.__balance += amount

    # Метод для пополнения счета
    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)
            print(f"Пополнено на {amount}")
        else:
            print("Сумма пополнения должна быть положительной.")

    # Метод для снятия средств
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__update_balance(-amount)
            print(f"Снято {amount}")
        else:
            print("Недостаточно средств или неверная сумма.")

# Создание объекта
# account = BankAccount("Alice", 1000)

# Пополнение счета
# account.deposit(500)  # Пополнено на 500

# Снятие средств
# account.withdraw(300)  # Снято 300

# Получение текущего баланса
# print(account.get_balance())  # 1200

# **Объяснение:**
#
# * Приватный метод `__update_balance` обновляет баланс, но не доступен для прямого использования извне.
# * Метод `deposit` и `withdraw` предоставляют интерфейс для работы с балансом, а детали реализации скрыты.
# * Использование инкапсуляции позволяет избежать ошибок, связанных с прямым изменением баланса.

### Пример 3: Инкапсуляция с абстракцией

# Теперь создадим класс `Employee`, который инкапсулирует имя, возраст и зарплату, но скрывает детали, как рассчитывается зарплата.


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary  # Приватный атрибут

    # Геттер для зарплаты
    def get_salary(self):
        return self.__salary

    # Сеттер для установки зарплаты
    def set_salary(self, salary):
        if salary < 0:
            print("Зарплата не может быть отрицательной.")
        else:
            self.__salary = salary

    # Метод для увеличения зарплаты
    def increase_salary(self, percentage):
        if percentage > 0:
            self.__salary += self.__salary * (percentage / 100)
            print(f"Зарплата увеличена на {percentage}%")
        else:
            print("Процент повышения должен быть положительным.")

# Создание объекта
# employee = Employee("Eve", 30, 5000)

# Увеличение зарплаты
# employee.increase_salary(10)  # Зарплата увеличена на 10%

# Получение зарплаты
# print(employee.get_salary())  # 5500

# Установка новой зарплаты
# employee.set_salary(6000)
# print(employee.get_salary())  # 6000


# **Объяснение:**
#
# * Метод `increase_salary` скрывает детали, как именно вычисляется увеличение зарплаты, предоставляя абстракцию для пользователей.
# * Приватный атрибут `__salary` не может быть изменен напрямую извне, и любые изменения должны проходить через предоставленные методы.

### Резюме:

# Инкапсуляция — это принцип ООП, который скрывает внутреннюю реализацию класса и предоставляет интерфейс для работы с объектами.
# Это помогает обеспечить контроль над доступом к данным и улучшить безопасность программы.
#
# * Приватные атрибуты и методы скрыты от пользователя и доступны только через публичные интерфейсы (геттеры и сеттеры).
# * С помощью инкапсуляции можно скрыть сложную логику и оставить только необходимые для пользователя функции.



# Урок 28: Инкапсуляция - Задачи

# 1. Создайте класс Person, который имеет публичный атрибут name и приватный атрибут age.
# Реализуйте геттер и сеттер для age, чтобы нельзя было установить возраст менее 0.
# Используйте геттер для получения возраста и сеттер для изменения значения.
class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            print("Возраст не может быть отрицательным.")
        else:
            self.__age = age

# person = Person("Boorsok", 22)
# print(person.get_age())
#
# person.set_age(-12)
#
# person.set_age(30)
# print(person.get_age())

# 2. Создайте класс BankAccount, который имеет приватный атрибут balance.
# Реализуйте геттер и сеттер для баланса, чтобы нельзя было вывести больше денег, чем на счете.
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # приватный атрибут

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Ошибка: Нельзя установить отрицательный баланс.")
        else:
            self.__balance = amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Ошибка: Недостаточно средств на счете.")
        else:
            self.__balance -= amount
            print(f"Снято: {amount}. Остаток: {self.__balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.__balance}")
        else:
            print("Ошибка: Сумма пополнения должна быть положительной.")

acc = BankAccount(100)
print(acc.balance)

acc.deposit(50)
acc.withdraw(200)
acc.withdraw(100)

acc.balance = -10
print(acc.balance)

# 3. Создайте класс Book, который имеет публичный атрибут title и приватный атрибут author.
# Реализуйте методы для изменения имени автора через сеттер.
class Book:

    def __init__(self, title, author):
        self.title = title
        self.__author = author

    def get_author(self):
        return self.__author

    def set_author(self, author):
        if not isinstance(author, str) or not author.strip():
            print("Автор не может быть другим!")
        else:
            self.__author = author

# book = Book("Атомные привычки", "Джеймс Клир")
# print(book.get_author())
#
# book.set_author("Чынгыз Айтматов")
# print(book.get_author())
#
# book.set_author("")

# 4. Создайте класс Rectangle с приватными атрибутами length и width.
# Добавьте геттеры и сеттеры для изменения этих значений.
# Реализуйте метод для вычисления площади прямоугольника.
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value > 0:
            self.__length = value
        else:
            print("Длина должна быть положительной.")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value > 0:
            self.__width = value
        else:
            print("Ширина должна быть положительной.")

    def area(self):
        return self.__length * self.__width

# 5. Создайте класс Product, который будет иметь приватные атрибуты name, price и quantity.
# Напишите методы для изменения этих атрибутов с проверками на правильность данных (например, цена не может быть отрицательной).
class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Цена не может быть отрицательной.")

    def set_quantity(self, quantity):
        if quantity >= 0:
            self.__quantity = quantity
        else:
            print("Количество не может быть отрицательным.")

    def set_name(self, name):
        self.__name = name

# 6. Создайте класс Circle, который имеет приватный атрибут radius.
# Напишите методы для получения и изменения радиуса круга и для вычисления его площади.
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("Радиус должен быть положительным.")

    def area(self):
        return math.pi * self.__radius ** 2

# 7. Создайте класс Student, который имеет публичный атрибут name и приватный атрибут marks.
# Реализуйте методы для добавления и получения оценок, с возможностью вывода среднего балла.
class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = []

    def add_mark(self, mark):
        if 0 <= mark <= 100:
            self.__marks.append(mark)
        else:
            print("Оценка должна быть от 0 до 100.")

    def get_marks(self):
        return self.__marks

    def average_mark(self):
        if self.__marks:
            return sum(self.__marks) / len(self.__marks)
        return 0

# 8. Добавьте в класс Employee метод display_salary(), который будет показывать зарплату сотрудника,
# если она больше 1000, иначе вывести сообщение "Зарплата недостаточна".
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def display_salary(self):
        if self.__salary > 1000:
            print(f"Зарплата: {self.__salary}")
        else:
            print("Зарплата недостаточна")

# 9. Создайте класс Vehicle, который имеет приватные атрибуты make, model, и year.
# Напишите методы для получения и изменения этих атрибутов.
# Реализуйте метод для вычисления возраста автомобиля.
from datetime import datetime

class Vehicle:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.__year

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

# 10. Создайте класс Person, который имеет приватные атрибуты name и phone_number.
# Реализуйте метод для изменения номера телефона с проверкой на его корректность.
import re

class Person:
    def __init__(self, name, phone_number):
        self.__name = name
        self.__phone_number = phone_number

    def set_phone_number(self, number):
        if re.match(r"^\+?\d{10,15}$", number):
            self.__phone_number = number
        else:
            print("Некорректный номер телефона.")

# 11. Создайте класс Movie, который имеет приватные атрибуты title, director, и release_year.
# Реализуйте метод для вывода информации о фильме.
class Movie:
    def __init__(self, title, director, release_year):
        self.__title = title
        self.__director = director
        self.__release_year = release_year

    def display_info(self):
        print(f"{self.__title} ({self.__release_year}), режиссёр: {self.__director}")

# 12. Создайте класс Employee, который имеет публичный атрибут name и приватный атрибут salary.
# Напишите геттер и сеттер для зарплаты, с проверкой, что зарплата не может быть меньше 0.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self.__salary = value
        else:
            print("Зарплата не может быть меньше 0.")

# 13. Создайте класс Ticket, который имеет приватные атрибуты price, seat_number.
# Реализуйте методы для изменения цены билета и номера места с проверкой на корректность данных.
class Ticket:
    def __init__(self, price, seat_number):
        self.__price = price
        self.__seat_number = seat_number

    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Цена не может быть отрицательной.")

    def set_seat_number(self, seat_number):
        if isinstance(seat_number, str) and seat_number:
            self.__seat_number = seat_number
        else:
            print("Номер места некорректный.")

# 14. Создайте класс LibraryBook, который имеет публичные атрибуты title и приватные атрибуты author и publication_year.
# Напишите методы для получения информации о книге.
class LibraryBook:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.__author = author
        self.__publication_year = publication_year

    def get_info(self):
        return f"{self.title}, {self.__author}, {self.__publication_year}"

# 15. Создайте класс Account, который имеет приватные атрибуты account_number и balance.
# Реализуйте методы для пополнения счета и вывода средств с проверкой на достаточность средств.
class Account:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Недостаточно средств.")
