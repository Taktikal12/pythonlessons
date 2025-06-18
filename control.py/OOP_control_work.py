# Задание 1
# Класс SocialMedia: name, users, is_staff, posts.
# Методы: add_user(), remove_user(), add_post(), get_feed(), get_user_count().
# Подклассы Instagram и Facebook:
# - Instagram: посты с фото (проверять формат, нельзя без фото)
# - Facebook: текстовые посты, проверка на максимальную длину текста.
# Логика: нельзя добавлять пользователей с одинаковыми username, нельзя удалить последнего админа.
class User:
    def __init__(self, username, is_admin=False):
        self.username = username
        self.is_admin = is_admin

    def __repr__(self):
        return f"{self.username} ({'admin' if self.is_admin else 'user'})"


class Post:
    def __init__(self, author, content, photo=None):
        self.author = author
        self.content = content
        self.photo = photo

    def __repr__(self):
        return f"Post by {self.author.username}: {self.content}"


class SocialMedia:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.is_staff = []
        self.posts = []

    def add_user(self, username, is_admin=False):
        if any(user.username == username for user in self.users):
            raise ValueError("Username already exists.")
        user = User(username, is_admin)
        self.users.append(user)
        if is_admin:
            self.is_staff.append(user)

    def remove_user(self, username):
        user_to_remove = next((u for u in self.users if u.username == username), None)
        if not user_to_remove:
            raise ValueError("User not found.")
        if user_to_remove in self.is_staff and len(self.is_staff) == 1:
            raise ValueError("Cannot remove the last admin.")
        self.users.remove(user_to_remove)
        if user_to_remove in self.is_staff:
            self.is_staff.remove(user_to_remove)

    def add_post(self, post):
        self.posts.append(post)

    def get_feed(self):
        return self.posts

    def get_user_count(self):
        return len(self.users)


class Instagram(SocialMedia):
    def __init__(self):
        super().__init__("Instagram")

    def add_post(self, author_username, content, photo):
        author = self._get_user(author_username)
        if not photo:
            raise ValueError("Instagram posts must contain a photo.")
        post = Post(author, content, photo=photo)
        super().add_post(post)

    def _get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        raise ValueError("User not found.")


class Facebook(SocialMedia):
    def __init__(self, max_length=280):
        super().__init__("Facebook")
        self.max_length = max_length

    def add_post(self, author_username, content):
        author = self._get_user(author_username)
        if len(content) > self.max_length:
            raise ValueError(f"Facebook posts must be under {self.max_length} characters.")
        post = Post(author, content)
        super().add_post(post)

    def _get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        raise ValueError("User not found.")


insta = Instagram()
insta.add_user("alice", is_admin=True)
insta.add_user("bob")
insta.add_post("alice", "My vacation photo!", photo="beach.jpg")

fb = Facebook(max_length=150)
fb.add_user("charlie", is_admin=True)
fb.add_post("charlie", "Just finished reading a great book!")

print(insta.get_feed())
print(fb.get_feed())



# Задание 2
# Класс SmartHomeDevice: device_name, status, energy_usage, firmware_version.
# Методы: turn_on(), turn_off(), update_firmware(version), get_status(), reset().
# Подклассы Thermostat и SecurityCamera:
# - Камера записывает только при достаточном освещении
# - Термостат требует предварительной калибровки
# Логика: нельзя обновлять прошивку, если устройство включено.
class SmartHomeDevice:
    def __init__(self, device_name, energy_usage, firmware_version):
        self.device_name = device_name
        self.status = False  # Выключено по умолчанию
        self.energy_usage = energy_usage
        self.firmware_version = firmware_version

    def turn_on(self):
        self.status = True
        print(f"{self.device_name} включено.")

    def turn_off(self):
        self.status = False
        print(f"{self.device_name} выключено.")

    def update_firmware(self, version):
        if self.status:
            print(f"Нельзя обновить прошивку, пока {self.device_name} включено.")
        else:
            self.firmware_version = version
            print(f"{self.device_name} обновлено до версии прошивки {version}.")

    def get_status(self):
        return {
            "device_name": self.device_name,
            "status": "Включено" if self.status else "Выключено",
            "energy_usage": self.energy_usage,
            "firmware_version": self.firmware_version
        }

    def reset(self):
        self.turn_off()
        self.firmware_version = "1.0"
        print(f"{self.device_name} сброшено к заводским настройкам.")


class Thermostat(SmartHomeDevice):
    def __init__(self, device_name, energy_usage, firmware_version):
        super().__init__(device_name, energy_usage, firmware_version)
        self.calibrated = False

    def calibrate(self):
        self.calibrated = True
        print(f"{self.device_name} откалиброван.")

    def turn_on(self):
        if not self.calibrated:
            print(f"{self.device_name} не может быть включён без калибровки.")
        else:
            super().turn_on()


class SecurityCamera(SmartHomeDevice):
    def __init__(self, device_name, energy_usage, firmware_version):
        super().__init__(device_name, energy_usage, firmware_version)
        self.light_level = 0  # Уровень освещения от 0 до 100

    def set_light_level(self, level):
        self.light_level = level
        print(f"Уровень освещения для {self.device_name} установлен на {level}.")

    def turn_on(self):
        if self.light_level >= 50:
            super().turn_on()
        else:
            print(f"{self.device_name} не может быть включена — недостаточно освещения.")

t = Thermostat("Термостат", 100, "1.2")
t.turn_on()             # Ошибка, не откалиброван
t.calibrate()
t.turn_on()             # Теперь включается
t.update_firmware("2.0")  # Ошибка, включен
t.turn_off()
t.update_firmware("2.0")  # Прошивка обновляется

c = SecurityCamera("Камера", 50, "1.1")
c.set_light_level(30)
c.turn_on()             # Ошибка, низкий свет
c.set_light_level(80)
c.turn_on()             # Включается

# Задание 3
# Класс DeliveryService: company, vehicles, orders, completed_orders.
# Методы: add_order(), dispatch_order(), track_order(), calculate_delivery_time(), summary().
# FoodDelivery: проверка на горячие/холодные блюда (разное время доставки).
# CourierDelivery: разные классы посылок (обычные, ценные).
# Логика: нельзя отправить заказ, если водитель уже занят.
class DeliveryService:
    def __init__(self, company):
        self.company = company
        self.vehicles = {}  # vehicle_id: is_available
        self.orders = {}  # order_id: order_info
        self.completed_orders = []

    def add_vehicle(self, vehicle_id):
        self.vehicles[vehicle_id] = True  # свободен

    def add_order(self, order_id, details):
        self.orders[order_id] = {
            "details": details,
            "status": "pending",
            "vehicle": None
        }
        print(f"Заказ {order_id} добавлен.")

    def dispatch_order(self, order_id):
        if order_id not in self.orders:
            print(f"Заказ {order_id} не найден.")
            return

        available_vehicle = next((v for v, available in self.vehicles.items() if available), None)
        if not available_vehicle:
            print("Нет свободных транспортных средств для доставки.")
            return

        self.vehicles[available_vehicle] = False
        self.orders[order_id]["status"] = "in_delivery"
        self.orders[order_id]["vehicle"] = available_vehicle
        print(f"Заказ {order_id} отправлен транспортом {available_vehicle}.")

    def complete_order(self, order_id):
        if order_id in self.orders and self.orders[order_id]["status"] == "in_delivery":
            vehicle_id = self.orders[order_id]["vehicle"]
            self.vehicles[vehicle_id] = True
            self.orders[order_id]["status"] = "delivered"
            self.completed_orders.append(order_id)
            print(f"Заказ {order_id} доставлен.")
        else:
            print(f"Невозможно завершить заказ {order_id}.")

    def track_order(self, order_id):
        order = self.orders.get(order_id)
        if order:
            return order["status"]
        return "Заказ не найден."

    def calculate_delivery_time(self, order_id):
        # Заглушка — в реальности зависит от расстояния, типа доставки и т.п.
        return "30 минут"

    def summary(self):
        print(f"Компания: {self.company}")
        print(f"Доступные транспортные средства: {[v for v, a in self.vehicles.items() if a]}")
        print(f"Ожидающие заказы: {[k for k, v in self.orders.items() if v['status'] == 'pending']}")
        print(f"В пути: {[k for k, v in self.orders.items() if v['status'] == 'in_delivery']}")
        print(f"Завершённые: {self.completed_orders}")


class FoodDelivery(DeliveryService):
    def calculate_delivery_time(self, order_id):
        order = self.orders.get(order_id)
        if not order:
            return "Заказ не найден."

        dish_type = order["details"].get("dish_type", "hot")
        if dish_type == "hot":
            return "30 минут"
        elif dish_type == "cold":
            return "45 минут"
        else:
            return "60 минут"


class CourierDelivery(DeliveryService):
    def calculate_delivery_time(self, order_id):
        order = self.orders.get(order_id)
        if not order:
            return "Заказ не найден."

        package_type = order["details"].get("package_type", "regular")
        if package_type == "valuable":
            return "120 минут"
        else:
            return "60 минут"

# Пример: еда
food = FoodDelivery("FastFoodExpress")
food.add_vehicle("V1")
food.add_vehicle("V2")
food.add_order("F001", {"dish_type": "hot"})
food.dispatch_order("F001")
print(food.calculate_delivery_time("F001"))
food.complete_order("F001")

# Пример: курьерская доставка
courier = CourierDelivery("QuickShip")
courier.add_vehicle("C1")
courier.add_order("C001", {"package_type": "valuable"})
courier.dispatch_order("C001")
print(courier.calculate_delivery_time("C001"))
courier.complete_order("C001")

courier.summary()

# Задание 4
# Класс FitnessApp: name, users, workouts, challenges.
# Методы: add_workout(), remove_workout(), track_progress(), get_user_stats(), leaderboard().
# YogaApp: фиксирует выполнение асан.
# RunningApp: учитывает пройденное расстояние и калории.
# Логика: прогресс сохраняется только для зарегистрированных пользователей.

# Задание 5
# Класс ECommerceSite: name, products, users, carts.
# Методы: add_product(), search_product(), add_to_cart(user), checkout(user), get_sales_report().
# FashionStore: одежда проверяет размер и наличие.
# ElectronicsStore: проверка гарантии, запрет продажи бракованного товара.
# Логика: скидки считаются только при сумме корзины > 1000.

# Задание 6
# Класс Bank: name, accounts, total_balance, overdraft_limit.
# Методы: create_account(), deposit(), withdraw(), transfer(), get_summary().
# SavingsBank: запрет перевода, если баланс < 0.
# InvestmentBank: учёт комиссии при переводе.
# Логика: нельзя открыть второй аккаунт с тем же ID.

# Задание 7
# Класс StreamingService: name, content, subscribers, ratings.
# Методы: add_content(), remove_content(), play(), rate_content(), get_recommendations().
# Netflix: сериал нельзя начать с середины, если не смотрел первые серии.
# Spotify: рейтинг трека меняется от прослушивания.
# Логика: подписчик с низким рейтингом контента — контент скрывается.

# Задание 8
# Класс School: name, students, teachers, schedule.
# Методы: add_student(), add_teacher(), schedule_lesson(), get_statistics(), expel_student().
# PrimarySchool: не более 5 уроков в день.
# HighSchool: проверка наличия лабораторных занятий.
# Логика: ученик не может быть удалён, если у него есть незавершённые проекты.

# Задание 9
# Класс Transportation: type, capacity, routes, current_passengers.
# Методы: add_route(), remove_route(), board_passenger(), start_service(), stop_service().
# Bus: проверка билетов перед посадкой.
# Train: разные классы вагонов (1-й и 2-й).
# Логика: нельзя посадить пассажира без билета или если превышен capacity.

# Задание 10
# Класс Hotel: name, rooms, guests, bookings.
# Методы: book_room(), check_in(), check_out(), get_available_rooms(), generate_invoice().
# BoutiqueHotel: подарки для гостей при заселении.
# ResortHotel: туристический сбор.
# Логика: нельзя отменить бронирование за день до заселения без штрафа.

# Задание 11
# Класс Marketplace: name, sellers, buyers, active_products.
# Методы: register_seller(), register_buyer(), list_product(), buy_product(), get_market_stats().
# FarmerMarket: товар — только еда и растения.
# ArtMarket: проверка подлинности (уникальность продукта).
# Логика: один продавец не может продавать больше 100 товаров.

# Задание 12
# Класс NewsWebsite: name, articles, authors, categories.
# Методы: add_article(), remove_article(), search_articles(), get_top_authors(), get_analytics().
# TechNews: проверка достоверности фактов.
# SportsNews: сортировка статей по актуальности матчей.
# Логика: нельзя публиковать статью без проверки редактором.

# Задание 13
# Класс FlightBookingSystem: name, flights, passengers, taxes.
# Методы: add_flight(), book_ticket(), cancel_ticket(), check_status(), calculate_revenue().
# DomesticFlight: внутренние рейсы — местные налоги.
# InternationalFlight: загран — визовые сборы.
# Логика: нельзя забронировать место, если нет визы (для международного рейса).

# Задание 14
# Класс OnlineCourse: name, students, lessons, assignments.
# Методы: add_lesson(), remove_lesson(), enroll_student(), complete_lesson(), get_progress().
# ProgrammingCourse: обязательная сдача заданий.
# LanguageCourse: тесты после каждого урока.
# Логика: нельзя пройти итоговый тест без прохождения всех уроков.

# Задание 15
# Класс GamingPlatform: name, players, games, leaderboards.
# Методы: add_game(), remove_game(), play_game(), update_leaderboard(), get_total_playtime().
# PCGaming: бонус за длительные сессии.
# MobileGaming: лимит времени игры (анти-зависимость).
# Логика: в leaderboard попадают только активные игроки за последние 7 дней.

# Задание 16
# Класс Cinema: name, movies, viewers, tickets_sold.
# Методы: add_movie(), remove_movie(), sell_ticket(), get_movie_stats(), daily_report().
# IndieCinema: дополнительная скидка при повторном просмотре.
# MultiplexCinema: разные цены на сеанс в зависимости от времени.
# Логика: нельзя продать билет, если у фильма рейтинг < 3.

# Задание 17
# Класс Restaurant: name, menu, orders, reviews.
# Методы: add_dish(), remove_dish(), place_order(), calculate_bill(), get_popular_dishes().
# FastFood: скидки на большие заказы.
# GourmetRestaurant: сервисный сбор.
# Логика: нельзя заказать блюдо, если оно закончилось (остаток).

# Задание 18
# Класс Library: name, books, members, late_returns.
# Методы: add_book(), lend_book(), return_book(), search_book(), get_stats().
# PublicLibrary: бесплатная выдача.
# UniversityLibrary: плата за просрочку.
# Логика: член с долгами не может взять книгу.

# Задание 19
# Класс Pet: name, species, owner, health.
# Методы: feed(), play(), sleep(), get_info(), visit_vet().
# DogPet: игра восстанавливает здоровье.
# CatPet: больше спит — больше довольство.
# Логика: здоровье ухудшается без игр и еды, визит к ветеринару восстанавливает здоровье.

# Задание 20
# Класс Portfolio: owner, investments, total_value, risk_profile.
# Методы: add_investment(), remove_investment(), calculate_value(), rebalance(), summary().
# StockPortfolio: медленный рост, низкий риск.
# CryptoPortfolio: быстрые колебания, высокий риск.
# Логика: нельзя добавить инвестицию, если она превышает лимит по риску (risk_profile).

