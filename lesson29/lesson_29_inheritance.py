
# Урок по ООП: Наследование

# 1. Введение в наследование
# Наследование — это механизм, который позволяет создавать новый класс на основе уже существующего. Новый класс (дочерний) наследует атрибуты и методы старого класса (родительского), что позволяет избежать дублирования кода и расширять функциональность.

# Зачем нужно наследование?
# - Повторное использование кода.
# - Расширение и модификация функциональности без изменений в родительском классе.
# - Упрощение структуры программы за счет создания иерархий классов.

# 2. Основы наследования
# Родительский класс (superclass) — класс, от которого наследуют другие классы.
# Дочерний класс (subclass) — класс, который наследует функциональность родительского.
# Переопределение метода — дочерний класс может изменить поведение метода, унаследованного от родительского класса.
# Использование super() — позволяет обратиться к методам и атрибутам родительского класса.

# Пример 1: Основы наследования
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return f"{self.name} makes a sound"
#
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)  # Вызов конструктора родительского класса
#         self.breed = breed
#
#     def speak(self):  # Переопределение метода родительского класса
#         return f"{self.name} barks"
#
# dog = Dog("Buddy", "Golden Retriever")
# print(dog.speak())  # Вывод: Buddy barks

# Пример 2: Использование super()
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return f"{self.name} makes a sound"
#
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)  # Вызов конструктора родительского класса
#         self.breed = breed
#
#     def speak(self):  # Переопределение метода
#         parent_speak = super().speak()  # Вызов метода родительского класса
#         return f"{parent_speak}, but {self.name} barks"
#
# dog = Dog("Buddy", "Golden Retriever")
# print(dog.speak())  # Вывод: Buddy makes a sound, but Buddy barks

# Пример 3: Множественное наследование
# class Swimmer:
#     def swim(self):
#         return "Swimming"
#
# class Animal:
#     def speak(self):
#         return "Animal sound"
#
# class Dolphin(Animal, Swimmer):
#     pass
#
# dolphin = Dolphin()
# print(dolphin.speak())  # Вывод: Animal sound
# print(dolphin.swim())   # Вывод: Swimming

# 3. Преимущества наследования
# - Повторное использование кода: Переиспользование методов и атрибутов родительских классов.
# - Легкость в модификации: Когда нужно изменить поведение, достаточно переопределить метод в дочернем классе.
# - Структурированность: Наследование помогает организовать иерархию классов.

# 4. 15 задач по теме "Наследование"
# 1. Создайте класс Person с атрибутами name и age. Реализуйте метод introduce(), который будет выводить строку "Hello, my name is {name} and I am {age} years old". Создайте класс Student, который наследует Person и добавляет атрибут student_id. Переопределите метод introduce(), чтобы выводить "Hello, I am {name}, a student with ID {student_id}".

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age} года")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"Привет, я {self.name}, студент с удостоверением личности {self.student_id}")


person = Person("Боорсок", 22)
person.introduce()

student = Student("Айсулуу", 20, "S9000MM")
student.introduce()

# 2. Создайте класс Vehicle с атрибутом speed и методом move(), который выводит сообщение "Moving at {speed} km/h". Создайте класс Car, который наследует от Vehicle и добавляет атрибут fuel_type. Переопределите метод move() для вывода сообщения "Car is moving at {speed} km/h using {fuel_type} fuel".

class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print(f"Движение со скоростью {self.speed} км/ч")

class Car(Vehicle):
    def __init__(self, speed, fuel_type):
        super().__init__(speed)
        self.fuel_type = fuel_type

    def move(self):
        print(f"Автомобиль едет со скоростью {self.speed} км/ч используя {self.fuel_type} топливо")

vehicle = Vehicle(60)
vehicle.move()

car = Car(120, "дизельное")
car.move()

# 3. Создайте базовый класс Shape с методом area() (возвращает 0). Создайте дочерние классы Circle и Rectangle, которые переопределяют метод area() для вычисления площади круга и прямоугольника соответственно.
import math

class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

shape = Shape()
print("Shape area:", shape.area())

circle = Circle(5)
print("Circle area:", circle.area())

rectangle = Rectangle(4, 6)
print("Rectangle area:", rectangle.area())

# 4. Создайте класс Animal с методом speak(), который возвращает "Animal sound". Создайте классы Dog и Cat, которые переопределяют метод speak() и выводят звуки соответствующих животных.

class Animal:
    def speak(self):
        return "Animal sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"

animal = Animal()
print("Animal:", animal.speak())

dog = Dog()
print("Dog:", dog.speak())

cat = Cat()
print("Cat:", cat.speak())

# 5. Создайте класс Employee с атрибутами name и salary. Создайте класс Manager, который наследует от Employee и добавляет атрибут department. Переопределите метод __str__() в классе Manager, чтобы выводить строку "Manager {name}, Department: {department}, Salary: {salary}".

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def __str__(self):
        return f"Manager {self.name}, Department: {self.department}, Salary: {self.salary}"

employee = Employee("Айганыш", 50000)
manager = Manager("Азим", 75000, "Sales")

print(manager)

# 6. Создайте класс BankAccount с атрибутом balance и методами deposit() и withdraw(). Создайте класс SavingsAccount, который наследует от BankAccount и добавляет метод add_interest().

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}, New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}, New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")


class SavingsAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0.02):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}, New balance: {self.balance}")

account = BankAccount(100)
account.deposit(50)
account.withdraw(30)

savings = SavingsAccount(200, 0.05)
savings.add_interest()

# 7. Создайте класс Person с атрибутом name и методом greet(). Создайте класс Employee, который наследует от Person и добавляет атрибут job_title. Переопределите метод greet() в классе Employee, чтобы выводить "Hello, I am {name}, and I work as a {job_title}".
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

class Employee(Person):
    def __init__(self, name, job_title):
        super().__init__(name)
        self.job_title = job_title

    def greet(self):
        print(f"Hello, I am {self.name}, and I work as a {self.job_title}")

p = Person("Alice")
p.greet()

e = Employee("Bob", "Software Engineer")
e.greet()

# 8. Создайте класс Book с атрибутами title и author. Создайте дочерний класс EBook, который добавляет атрибут file_size и переопределяет метод __str__(), чтобы включить размер файла в строковое представление.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{self.title} by {self.author}, File size: {self.file_size}MB"

book = Book("1984", "George Orwell")
ebook = EBook("Brave New World", "Aldous Huxley", 2.5)

print(ebook)

# 9. Создайте класс Product с атрибутами name и price. Создайте дочерний класс DiscountedProduct, который добавляет атрибут discount и метод get_discounted_price() для расчета цены со скидкой.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def get_discounted_price(self):
        return self.price * (1 - self.discount / 100)

product = Product("Laptop", 1000)
discounted = DiscountedProduct("Laptop", 1000, 15)

print(discounted.get_discounted_price())

# 10. Создайте класс Shape с методом draw(). Создайте дочерние классы Circle и Square, которые переопределяют метод draw() для рисования соответствующих фигур.
class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

s = Shape()
c = Circle()
sq = Square()

s.draw()
c.draw()
sq.draw()

# 11. Создайте класс Person с методом speak(). Создайте дочерний класс Teacher, который добавляет метод teach() и переопределяет метод speak(), чтобы выводить информацию о том, что этот человек учит.
class Person:
    def speak(self):
        print("I am a person.")

class Teacher(Person):
    def speak(self):
        print("I am a teacher and I am speaking.")

    def teach(self):
        print("I am teaching.")

p = Person()
t = Teacher()

p.speak()
t.speak()
t.teach()

# 12. Создайте класс Vehicle с атрибутом capacity. Создайте класс Bus, который наследует от Vehicle и добавляет метод pick_up(), который выводит сообщение о том, что автобус забирает пассажиров.
class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

class Bus(Vehicle):
    def pick_up(self):
        print(f"The bus with capacity {self.capacity} is picking up passengers.")

bus = Bus(50)
bus.pick_up()

# 13. Создайте класс Shape с атрибутами width и height. Создайте класс Rectangle, который наследует от Shape и добавляет метод calculate_area(), который вычисляет площадь прямоугольника.
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height

rect = Rectangle(5, 10)
print(rect.calculate_area())

# 14. Создайте класс Person с методом work(). Создайте дочерний класс Engineer, который наследует от Person и переопределяет метод work(), чтобы выводить информацию о проекте, над котором работает инженер.
class Person:
    def work(self):
        print("Working...")

class Engineer(Person):
    def work(self):
        print("I am working on a software development project.")

eng = Engineer()
eng.work()

# 15. Создайте класс Student с атрибутом name и методом study(). Создайте дочерний класс GraduateStudent, который добавляет метод research() и переопределяет метод study() для вывода информации о научной работе.
class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f"{self.name} is studying.")

class GraduateStudent(Student):
    def study(self):
        print(f"{self.name} is studying for research.")

    def research(self):
        print(f"{self.name} is doing research on machine learning.")

gs = GraduateStudent("Ivan")
gs.study()
gs.research()
