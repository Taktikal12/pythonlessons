"""
Урок: Принцип Абстракции в ООП на Python

1. Теоретическая часть
2. Примеры с подробным объяснением
3. Практические задания (20 шт.)
"""

# 1. Теоретическая часть
"""
Абстракция — это принцип ООП, позволяющий скрывать детали реализации и оставлять только наиболее важные характеристики объекта.
Проще говоря, это выделение общих свойств и поведения объектов в отдельный класс, не вдаваясь в детали, которые могут различаться.

Абстракция помогает:
- Сократить количество кода
- Сделать систему более гибкой
- Упростить поддержку и развитие кода

В Python абстракция реализуется через абстрактные классы и абстрактные методы, которые задают интерфейс, а конкретная 
реализация предоставляется в дочерних классах.
"""


# 2. Примеры

# == Пример 1: Абстрактный класс и метод =="

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        """Абстрактный метод — подклассы должны его реализовать."""
        pass

class Dog(Animal):
    def make_sound(self):
        print("Гав-гав!")

class Cat(Animal):
    def make_sound(self):
        print("Мяу!")

# Попытка создать объект абстрактного класса вызовет ошибку:
try:
    a = Animal()
except TypeError as e:
    print("Ошибка:", e)

# Создание объектов потомков
# dog = Dog()
# dog.make_sound()  # Выведет: Гав-гав!
#
# cat = Cat()
# cat.make_sound()  # Выведет: Мяу!

"""
В этом примере:
- Абстрактный класс Animal задаёт интерфейс (метод make_sound).
- Подклассы Dog и Cat реализуют этот метод по-своему.
"""


# == Пример 2: Абстракция через базовый класс =="

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


rect = Rectangle(10, 5)
print(f"Площадь: {rect.area()}")
print(f"Периметр: {rect.perimeter()}")

"""
Здесь Shape — это абстрактный класс, который задаёт интерфейс для фигур.
Rectangle реализует конкретные методы area и perimeter.
"""


# == Пример 3: Интерфейс подключения (концептуальный пример) =="

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Подключение к MySQL...")

    def disconnect(self):
        print("Отключение от MySQL...")

class PostgreSQLDatabase(Database):
    def connect(self):
        print("Подключение к PostgreSQL...")

    def disconnect(self):
        print("Отключение от PostgreSQL...")

mysql_db = MySQLDatabase()
mysql_db.connect()
mysql_db.disconnect()

psql_db = PostgreSQLDatabase()
psql_db.connect()
psql_db.disconnect()

"""
Абстракция позволяет задавать общий интерфейс для работы с базой данных, а конкретные реализации могут быть разными (MySQL, PostgreSQL).
"""


# 3. Практические задания

# 1. Создайте абстрактный класс Vehicle с методом move().
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

# 2. Реализуйте два класса Car и Bike, которые наследуются от Vehicle и реализуют move().
class Car(Vehicle):
    def move(self):
        return "Машина движется по дороге"

class Bike(Vehicle):
    def move(self):
        return "Велосипед движется по тропинке"

# 3. Создайте абстрактный класс Appliance с абстрактным методом turn_on().
from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

# 4. Реализуйте подклассы: Fridge и Microwave, которые включаются по-своему.
class Fridge(Appliance):
    def turn_on(self):
        return "Холодильник сейчас охлаждает"

class Microwave(Appliance):
    def turn_on(self):
        return "Микроволновка разогревает еду"

# 5. Создайте абстрактный класс Worker с методом work().
from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

# 6. Реализуйте два подкласса: Developer и Designer.
class Developer(Worker):
    def work(self):
        return "Разработчик пишет код"

class Designer(Worker):
    def work(self):
        return "Дизайнер создает дизайны"

# 7. Создайте абстрактный класс Animal с методом speak().
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# 8. Создайте классы Cow и Sheep, которые "говорят" по-разному.
class Cow(Animal):
    def speak(self):
        return "Муу"

class Sheep(Animal):
    def speak(self):
        return "Бее"

# 9. Создайте абстрактный класс Payment с методом pay().
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# 10. Реализуйте подклассы: CreditCardPayment и CashPayment.
class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Оплачено {amount} с помощью кредитной карты"

class CashPayment(Payment):
    def pay(self, amount):
        return f"Оплачено {amount} наличными"

# 11. Создайте абстрактный класс File с методом open().
from abc import ABC, abstractmethod

class File(ABC):
    @abstractmethod
    def open(self):
        pass

# 12. Реализуйте подклассы: TextFile и ImageFile.
class TextFile(File):
    def open(self):
        return "Открытие текстового файла"

class ImageFile(File):
    def open(self):
        return "Открытие файла изображения"

# 13. Создайте абстрактный класс Person с методом introduce().
from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def introduce(self):
        pass

# 14. Реализуйте подклассы Student и Teacher.
class Student(Person):
    def introduce(self):
        return "Привет, я студент."

class Teacher(Person):
    def introduce(self):
        return "Привет, я учитель."

# 15. Создайте абстрактный класс Account с методом login().
from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def login(self):
        pass

# 16. Реализуйте подклассы: FacebookAccount и GoogleAccount.
class FacebookAccount(Account):
    def login(self):
        return "Авторизован через Facebook"

class GoogleAccount(Account):
    def login(self):
        return "Авторизован через Google"

# 17. Создайте абстрактный класс Sensor с методом read_data().
from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def read_data(self):
        pass

# 18. Реализуйте подклассы: TemperatureSensor и PressureSensor.
class TemperatureSensor(Sensor):
    def read_data(self):
        return "Temperature: 22°C"

class PressureSensor(Sensor):
    def read_data(self):
        return "Pressure: 1013 hPa"

# 19. Создайте абстрактный класс Employee с методом calculate_salary().
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

# 20. Реализуйте подклассы: HourlyEmployee и SalariedEmployee.
class HourlyEmployee(Employee):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate

class SalariedEmployee(Employee):
    def __init__(self, annual_salary):
        self.annual_salary = annual_salary

    def calculate_salary(self):
        return self.annual_salary / 12



