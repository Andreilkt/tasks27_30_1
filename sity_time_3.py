""" Три класса определяют время в разных городах

"""

import pytz
import datetime


# Класс выводит московское время
class Moscow:
    def __init__(self):
        self.local_time = pytz.timezone('Europe/Moscow').localize(datetime.datetime.now())


# Класс выводит время Екатеринбурга
class Ekaterinburg:
    def __init__(self):
        self.local_time = pytz.timezone('Asia/Yekaterinburg').localize(datetime.datetime.now())


# Класс выводит время Владивостока
class Vladivostok:
    def __init__(self):
        self.local_time = pytz.timezone('Asia/Vladivostok').localize(datetime.datetime.now())


# Создание объектов классов
moscow = Moscow()
ekaterinburg = Ekaterinburg()
vladivostok = Vladivostok()

# Вызов методов классов
print("Москва:", moscow.local_time)
print("Екатеринбург:", ekaterinburg.local_time)
print("Владивосток:", vladivostok.local_time)
