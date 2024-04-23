from enum import Enum


class UserType(Enum):
    ENGINEER = 1
    MANAGER = 2


class User:
    def __init__(self, name, age, user_type, phone_number):
        self.name = name
        self.age = age
        self.user_type = user_type
        self.phone_number = phone_number

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Type:", self.user_type.name)
        print("Phone:", self.phone_number)


# Приклад використання класу
user = User("John", 25, UserType.ENGINEER, "0509379992")
user.print_details()
