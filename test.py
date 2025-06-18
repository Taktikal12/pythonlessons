# num1 = 9
# num2 = 8.9
# num3 = 12
# print(num1 == num2)
# print(num1 >= num2)
# print(num3 != num1)
#
# num11 = -19
# print(abs(num11))
# print(max( 10, 20, 30))
# print(max(num1, num2, num3, num11))
# print(min(num1, num2, num3, num11))
# #
# #
#
# text = "  West Cost  "
# print("Uppercase:", text.upper())
# print("Lowercase:",text.lower())
# print("Title Case:", text.title())
# print("the grey:Asel", 7, 7, 1997, sep="|", end="\n")
# print("Bali")
# print(5 * 5)
# print("Result:", max(9, 7, 3, 15, -25, 23))
# print("Result:", min(9, 7, 3, 15, -25, 23))
#
#
# num1 = input(" Введите первое число: ")
# num2 = input(" Введите второе число: ")


from abc import ABC, abstractmethod

class SocialMedia(ABC):
    def __init__(self):
        self.users = {}

    def add_user(self, name, is_staff=False):
        if self.users.get(name):
            print("Username already exists. Please choose a different one.")
        else:
            self.users[name] = {
                "is_staff": is_staff,
                "posts": []
            }
            print(f"User {name} added successfully.")


    def remove_user(self, name):
        cnt = 0
        for key, value in self.users.items():
            if value["is_staff"] and name != key:
                cnt += 1

        if name in self.users and (cnt > 0 or not self.users[name]["is_staff"]):
            del self.users[name]
            print(f"User {name} removed successfully.")
        elif name not in self.users:
            print(f"User {name} not found.")
        else:
            print(f"Cannot remove user {name} because there are {cnt} staff users.")

    @abstractmethod
    def add_post(self, user, content):
        pass

    @abstractmethod
    def get_feed(self):
        pass

    def get_user_count(self):
        print(len(self.users))


class Instagram(SocialMedia):
    def add_post(self, user, content, photo=None):
        if photo:
            if not photo.endswith((".jpg", ".jpeg", ".png")):
                print("Invalid photo format. Please provide a valid image.")
            else:
                self.users[user]["posts"].append({"content": content, "photo": photo})
                print(f"Post by {user} added successfully.")
        else:
            print("Photo is required for Instagram posts.")

    def get_feed(self):
        print("Instagram feed:")
        for user, data in self.users.items():
            print(f"{user}:")
            for post in data["posts"]:
                print(f"- {post['content']}")
                if "photo" in post:
                    print(f"  Photo: {post['photo']}")


class Facebook(SocialMedia):
    def add_post(self, user, content):
        if len(content) <= 140:
            self.users[user]["posts"].append({"content": content})
            print(f"Post by {user} added successfully.")
        else:
            print("Text posts must be less than 140 characters.")

    def get_feed(self):
        print("Facebook feed:")
        for user, data in self.users.items():
            print(f"{user}:")
            for post in data["posts"]:
                print(f"- {post['content']}")

insta = Instagram()
insta.add_user("Altyn")
insta.add_user("Altyn2", is_staff=True)
insta.add_user("Altyn")
insta.add_user("Sasha")

insta.add_post("Altyn", "Hello, world!")


insta.remove_user("Altyn2")
insta.get_user_count()
insta.remove_user("Sasha")
insta.get_user_count()

