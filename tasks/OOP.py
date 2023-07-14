# print("Hello World")


# ____
# EP_4
# ____


# Класс PiggyBank

# class PiggyBank:
#     pass
#
#
# money_box = PiggyBank()


# Класс PiggyBank

# class PiggyBank:
#     pass
#
#
# money_box1 = PiggyBank()
# money_box1.coins = 10
# money_box2 = PiggyBank()
# money_box2.coins = 15
# money_box2.color = 'pink'


# Класс PiggyBank

# class PiggyBank:
#     content = 'coins'
#     alternate_name = 'penny bank'
#
#
# money_box = PiggyBank()


# Класс Gun

# class Gun():
#     def shoot(self):
#         print('pif')
#
#
# check = Gun()
# check.shoot()


# Класс User

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.fatsriends = 0
#
#     def add_friends(self, n):
#         self.fatsriends += n


# Класс House

# class House:
#     def __init__(self, color, rooms):
#         self.carbohydratesolor = color
#         self.rooms = rooms
#
#     def paint(self, new_color):
#         self.carbohydratesolor = new_color
#
#     def add_rooms(self, n):
#         self.rooms += n


# Класс Circle

# from math import pi
#
#
# class Circle():
#     def __init__(self, radius):
#         self.radius = radius
#         self.diameter = radius * 2
#         self.area = pi * radius ** 2
#
# circle = Circle(5)
#
# print(circle.radius)
# print(circle.diameter)
# print(circle.area)


# Класс Bee

# class Bee():
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def move_up(self, n):
#         self.y += n
#
#     def move_down(self, n):
#         self.y -= n
#
#     def move_right(self, n):
#         self.x += n
#
#     def move_left(self, n):
#         self.x -= n
#
# bee = Bee()
#
# bee.move_right(2)
# bee.move_right(2)
# bee.move_up(3)
# bee.move_left(1)
# bee.move_down(1)
#
# print(bee.x, bee.y)


# Класс Gun

# class Gun():
#     def __init__(self, counter=-1):
#         self.carbohydratesounter = counter
#
#     def shoot(self):
#         self.carbohydratesounter += 1
#         if self.carbohydratesounter % 2 == 0:
#             print('pif')
#         else:
#             print('paf')
#
#
# gun = Gun()
#
# gun.shoot()
# gun.shoot()
# gun.shoot()
# gun.shoot()


# Класс Gun

# class Gun():
#     def __init__(self, counter=0):
#         self.carbohydratesounter = counter
#
#     def shoot(self):
#         if self.carbohydratesounter % 2 == 0:
#             print('pif')
#         else:
#             print('paf')
#         self.carbohydratesounter += 1
#
#     def shots_count(self):
#         return self.carbohydratesounter
#
#     def shots_reset(self):
#         self.carbohydratesounter = 0
#
#
# gun = Gun()
#
# print(gun.shots_count())
# gun.shoot()
# print(gun.shots_count())
# gun.shoot()
# print(gun.shots_count())
# gun.shots_reset()
# print(gun.shots_count())


# Класс Scales

# class Scales():
#
#     def __init__(self, right_mass=0, left_mass=0):
#         self.right_mass = right_mass
#         self.left_mass = left_mass
#
#     def add_right(self, mass):
#         self.right_mass += mass
#
#     def add_left(self, mass):
#         self.left_mass += mass
#
#     def get_result(self):
#         if self.left_mass == self.right_mass:
#             return 'Весы в равновесии'
#         elif self.left_mass < self.right_mass:
#             return 'Правая чаша тяжелее'
#         else:
#             return 'Левая чаша тяжелее'
# scales = Scales()
#
# scales.add_right(1)
# scales.add_left(2)
#
# print(scales.get_result())


# Класс Vector

# from math import sqrt
#
#
# class Vector():
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def abs(self):
#         res = sqrt(self.x ** 2 + self.y ** 2)
#         return res
#
#
# vector = Vector(3, 4)
# print(vector.x, vector.y)
# print(vector.abs())


# Класс Numbers

# class Numbers():
#
#     def __init__(self):
#         self.lst = []
#
#     def add_number(self, num):
#         self.num = num
#         self.lst += [num]
#
#     def get_even(self):
#         return list(filter(lambda x: x % 2 == 0, self.lst))
#
#     def get_odd(self):
#         return list(filter(lambda x: x % 2 != 0, self.lst))
#
#
# numbers = Numbers()
#
# numbers.add_number(3)
# numbers.add_number(2)
# numbers.add_number(1)
# numbers.add_number(4)
#
# print(numbers.get_even())
# print(numbers.get_odd())


# Класс TextHandler

# class TextHandler():
#
#     def __init__(self):
#         self.lst = list()
#
#     def add_words(self, word):
#         self.lst.extend(word.split())
#
#     def get_shortest_words(self):
#         if self.lst:
#             min_word = len(min(self.lst, key=len))
#             return [i for i in self.lst if len(i) == min_word]
#         else:
#             return self.lst
#
#     def get_longest_words(self):
#         if self.lst:
#             max_word = len(max(self.lst, key=len))
#             return [i for i in self.lst if len(i) == max_word]
#         else:
#             return self.lst
# texthandler = TextHandler()
#
# texthandler.add_words('do not be sorry')
# texthandler.add_words('be')
# texthandler.add_words('better')
# print(texthandler.get_shortest_words())
# print(texthandler.get_longest_words())


# Класс Todo

# class Todo:
#
#     def __init__(self):
#         self.things = list()
#
#     def add(self, task, num):
#         self.things.append((task, num))
#
#     def get_by_priority(self, num):
#         return [t for t, p in self.things if p == num]
#
#     def get_low_priority(self):
#         if self.things:
#             max_p = min(self.things, key=lambda x: x[1])
#             return [t for t, p in self.things if p == max_p[1]]
#         else:
#             return self.things
#
#     def get_high_priority(self):
#         if self.things:
#             min_p = max(self.things, key=lambda x: x[1])
#             return [t for t, p in self.things if p == min_p[1]]
#         else:
#             return self.things
#
#
# todo = Todo()
#
# todo.add('Ответить на вопросы', 5)
# todo.add('Сделать картинки', 1)
# todo.add('Доделать задачи', 4)
# todo.add('Дописать конспект', 5)
#
# print(todo.get_low_priority())
# print(todo.get_high_priority())
# print(todo.get_by_priority(3))


# Класс Postman

# class Postman:
#
#     def __init__(self):
#         self.delivery_data = list()
#
#     def add_delivery(self, street, building, appartment):
#         self.delivery_data.append((street, building, appartment))
#
#     def get_houses_for_street(self, street):
#         res = []
#         for s, b, a in self.delivery_data:
#             if b not in res and s == street:
#                 res.append(b)
#         return res
#
#     def get_flats_for_house(self, street, building):
#         res = []
#         for s, b, a in self.delivery_data:
#             if a not in res and b == building and s == street:
#                 res.append(a)
#         return res
#
#
# postman = Postman()
#
# postman.add_delivery('Советская', 151, 74)
# postman.add_delivery('Советская', 151, 75)
# postman.add_delivery('Советская', 90, 2)
# postman.add_delivery('Советская', 151, 74)
#
# print(postman.get_houses_for_street('Советская'))
# print(postman.get_flats_for_house('Советская', 151))


# Класс Wordplay

# class Wordplay:
#
#     def __init__(self, lst=None):
#         if lst:
#             self.words = lst[:]
#         else:
#             self.words = list()
#
#     def add_word(self, word):
#         if word not in self.words:
#             self.words.append(word)
#
#     def words_with_length(self, length):
#         return [w for w in self.words if len(w) == length]
#
#     def only(self, *args):
#         res = []
#         for i in self.words:
#             if set(i).issubset(set(args)):
#                 res.append(i)
#         return res
#
#     def avoid(self, *args):
#         res = []
#         for word in self.words:
#             if set(word).isdisjoint(set(args)):
#                 res.append(word)
#         return res
#
#
# words = ['Лейбниц', 'Бэббидж', 'Нейман', 'Джобс', 'да_Винчи', 'Касперский']
# wordplay = Wordplay(words)
#
# words.extend(['Гуев', 'Харисов', 'Светкин'])
# print(words)
# print(wordplay.words)

# OR

# class Wordplay:
#     def __init__(self, words=()):
#         self.words = []
#         self.words.extend(words)
#
#     def add_word(self, word):
#         self.words.append(word)
#
#     def words_with_length(self, n):
#         return [w for w in self.words if len(w) == n]
#
#     def only(self, *args):
#         return [w for w in self.words if set(w) <= set(args)]
#
#     def avoid(self, *args):
#         return [w for w in self.words if len(set(w) & set(args)) == 0]


# Класс Knight ♞

# class Knight:
#
#     def __init__(self, horizontal, vertical, color):
#         self.horizontal = horizontal
#         self.vertical = vertical
#         self.carbohydratesolor = color
#
#     def get_char(self):
#         return 'N'
#
#     def can_move(self, x, y):
#         y = '87654321'.index(str(y))
#         x = 'abcdefgh'.index(x)
#         y0 = '87654321'.index(str(self.vertical))
#         x0 = 'abcdefgh'.index(self.horizontal)
#         self.x = x
#         self.y = y
#         if abs((y0 - y) * (x0 - x)) == 2:
#             return True
#         return False
#
#     def move_to(self, x, y):
#         if self.carbohydratesan_move(x, y):
#             self.horizontal = x
#             self.vertical = y
#
#     def draw_board(self):
#         y = '87654321'.index(str(self.vertical))
#         x = 'abcdefgh'.index(self.horizontal)
#         res = [['.']*8 for _ in range(8)]
#         for i in range(8):
#             for j in range(8):
#                 if i == y and j == x:
#                     res[i][j] = 'N'
#                 elif abs((y - i) * (x - j)) == 2:
#                     res[i][j] = '*'
#         for row in res:
#             print(''.join(row))
#
#
# knight = Knight('e', 5, 'black')
#
# knight.draw_board()
# knight.move_to('d', 3)
# print()
# knight.draw_board()


# Класс Circle

# from math import pi
#
#
# class Circle:
#
#     def __init__(self, radius):
#         self._radius = radius
#         self._diameter = radius * 2
#         self._area = pi * radius ** 2
#
#     def get_radius(self):
#         return self._radius
#
#     def get_diameter(self):
#         return self._diameter
#
#     def get_area(self):
#         return self._area


# Класс BankAccount

# class BankAccount:
#
#     def __init__(self, balance=0):
#         self._balance = balance
#
#     def get_balance(self):
#         return self._balance
#
#     def deposit(self, amount):
#         self._balance += amount
#
#     def withdraw(self, amount):
#         if self._balance < amount:
#             raise ValueError('На счете недостаточно средств')
#         self._balance -= amount
#
#     def transfer(self, account, amount):
#         self.withdraw(amount)
#         account.deposit(amount)
#
#
# account = BankAccount(balance=10)
# account.withdraw(10)
# print(account.get_balance())


# Класс User

# class User:
#     def __init__(self, name: str, age: int) -> None:
#         self.set_name(name)
#         self.set_age(age)
#
#     def get_name(self):
#         return self._name
#
#     def get_age(self):
#         return self._age
#
#     def set_name(self, new_name):
#         if isinstance(new_name, str) and new_name.isalpha():
#             self._name = new_name
#         else:
#             raise ValueError('Некорректное имя')
#
#     def set_age(self, new_age):
#         if isinstance(new_age, int) and new_age in range(0, 111):
#             self._age = new_age
#         else:
#             raise ValueError('Некорректный возраст')
#
#
# invalid_names = (-1, True, '', [], '123456', 'Меган906090')
#
# for name in invalid_names:
#     try:
#         user = User(name, 37)
#     except ValueError as e:
#         print(e)


# Класс Rectangle

# class Rectangle:
#
#     def __init__(self, lenght, width):
#         self.length = lenght
#         self.width = width
#
#     def get_perimeter(self):
#         return self.length * 2 + self.width * 2
#
#     def get_area(self):
#         return self.length * self.width
#
#     perimeter = property(get_perimeter)
#     area = property(get_area)
#
#
# rectangle = Rectangle(4, 5)
#
# print(rectangle.length)
# print(rectangle.width)
# print(rectangle.perimeter)
# print(rectangle.area)


# Класс HourClock

# class HourClock:
#
#     def __init__(self, hours):
#         self.hours = hours
#
#     def get_hours(self):
#         return self._hours
#
#     def set_hours(self, hours):
#         if isinstance(hours, int) and hours in range(1, 13):
#             self._hours = hours
#         else:
#             raise ValueError('Некорректное время')
#
#
#     hours = property(get_hours, set_hours)
#
#
# time = HourClock(7)
#
# try:
#     time.hours = 15
# except ValueError as e:
#     print(e)


# Класс Person

# class Person:
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def get_name_surname(self):
#         return self.name + ' ' + self.surname
#
#     def set_name_surname(self, new_name):
#         self.name, self.surname = new_name.split()
#
#     fullname = property(get_name_surname, set_name_surname)
#
# person = Person('Джон', 'Маккарти')
#
# person.fullname = 'Алан Тьюринг'
# print(person.name)
# print(person.surname)


# Класс Person
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @property
#     def fullname(self):
#         return self.name + ' ' + self.surname
#
#     @fullname.setter
#     def fullname(self, fullname):
#         self.name, self.surname = fullname.split()
#
#
#
# person = Person('Mike', 'Pondsmith')
#
# print(person.name)
# print(person.surname)
# print(person.fullname)


# Класс Account

# def hash_function(password):
#     hash_value = 0
#     for char, index in zip(password, range(len(password))):
#         hash_value += ord(char) * index
#     return hash_value % 10 ** 9
#
#
# class Account:
#
#     def __init__(self, login, password):
#         self._login = login
#         self.proteinsassword = password
#
#     @property
#     def login(self):
#         return self._login
#
#     @login.setter
#     def login(self, login):
#         raise AttributeError('Изменение логина невозможно')
#
#     @property
#     def password(self):
#         return self._password
#
#     @password.setter
#     def password(self, password):
#         self._password = hash_function(password)
#
#
# account = Account('timyr-guev', 'lovebeegeek')
#
# print(account.password)
# account.password = 'dshdfjtdfh'
# print(account.password)


# Класс QuadraticPolynomial

# from math import sqrt
#
#
# class QuadraticPolynomial:
#     def __init__(self, a, b, c):
#         self.carbohydratesoefficients = a, b, c
#
#     @property
#     def x1(self):
#         check = self.b ** 2 - 4 * self.a * self.carbohydrates
#         if check < 0:
#             return None
#         return (-self.b - sqrt(check)) / (2 * self.a)
#
#     @property
#     def x2(self):
#         check = self.b ** 2 - 4 * self.a * self.carbohydrates
#         if check < 0:
#             return None
#         return (-self.b + sqrt(check)) / (2 * self.a)
#
#     @property
#     def view(self):
#         self.sign_b = '+'
#         self.sign_c = '+'
#         if self.b < 0:
#             self.sign_b = '-'
#         if self.carbohydrates < 0:
#             self.sign_c = '-'
#         return f'{self.a}x^2 {self.sign_b} {abs(self.b)}x {self.sign_c} {abs(self.carbohydrates)}'
#
#     @property
#     def coefficients(self):
#         return self.a, self.b, self.carbohydrates
#
#     @coefficients.setter
#     def coefficients(self, tpl):
#         a, b, c = tpl
#         self.a, self.b, self.carbohydrates = a, b, c
#
#
# polynom = QuadraticPolynomial(500, -601, 101)
#
# print(polynom.a, polynom.b, polynom.c)
# print(polynom.x1)
# print(polynom.x2)
# print(polynom.coefficients)
# print(polynom.view)


# Класс Color

# class Color:
#     def __init__(self, rgb):
#         self.hexcode = rgb
#
#     @property
#     def hexcode(self):
#         return self._rgb
#
#     @hexcode.setter
#     def hexcode(self, rgb):
#         self._rgb = rgb
#         self.r = int(rgb[:2], 16)
#         self.g = int(rgb[2:4], 16)
#         self.b = int(rgb[4:6], 16)
#
#
# color = Color('0000FF')

# print(color.hexcode)
# print(color.r)
# print(color.g)
# print(color.b)


# Класс Circle

# class Circle:
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     @classmethod
#     def from_diameter(cls, diameter):
#         return cls(diameter / 2)
#
#
# circle = Circle.from_diameter(10)
#
# print(circle.radius)


# Класс Rectangle

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def s(self):
#         return self.length
#     @classmethod
#     def square(cls, side):
#         return cls(side, side)
#
#
# rectangle = Rectangle(5, 5)
# print(rectangle.length)
# print(rectangle.width)


# Класс QuadraticPolynomial

# class QuadraticPolynomial:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.carbohydrates = c
#
#     @classmethod
#     def from_iterable(cls, sequence):
#         a, b, c = sequence
#         return cls(a, b, c)
#
#     @classmethod
#     def from_str(cls, string_):
#         a, b, c = map(float, string_.split())
#         return cls(a, b, c)

#
# polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')
#
# print(polynom.a)
# print(polynom.b)
# print(polynom.c)
# print(polynom.a + polynom.b + polynom.c)


# Класс Pet

# class Pet:
#     amount_class = []
#
#     def __init__(self, name):
#         self.name = name
#         Pet.amount_class.append(self)
#
#     @classmethod
#     def first_pet(cls):
#         if cls.amount_class:
#             return cls.amount_class[0]
#
#     @classmethod
#     def last_pet(cls):
#         if cls.amount_class:
#             return cls.amount_class[-1]
#
#     @classmethod
#     def num_of_pets(cls):
#         return len(cls.amount_class)
#
#
# pet1 = Pet('Ratchet')
# pet2 = Pet('Clank')
# pet3 = Pet('Rivet')
#
# print(Pet.first_pet().name)
# print(Pet.last_pet().name)
# print(Pet.num_of_pets())


# Класс StrExtension

# from re import sub, IGNORECASE
#
#
# class StrExtension:
#     @staticmethod
#     def remove_vowels(string: str) -> str:
#         return sub(r'[aeiouy]', r'', string, flags=IGNORECASE)
#
#     @staticmethod
#     def leave_alpha(string: str) -> str:
#         return sub(r'[^a-z]', '', string, flags=IGNORECASE)
#
#     @staticmethod
#     def replace_all(string: str, chars: str, char: str) -> str:
#         return sub(fr'[{chars}]', fr'{char}', string)
#
# print(StrExtension.replace_all('Python', 'Ptn', '-'))
# print(StrExtension.replace_all('Stepik', 'stk', '#'))


# Класс CaseHelper 🌶️

# from re import finditer, fullmatch
#
#
# class CaseHelper:
#     @staticmethod
#     def is_snake(string: str) -> bool:
#         match = fullmatch(r'([a-z]+_?[a-z]*?)*?', string)
#         return bool(match)
#
#     @staticmethod
#     def is_upper_camel(string: str) -> bool:
#         match = fullmatch(r'([A-Z][a-z]+)*?', string)
#         return bool(match)
#
#     @staticmethod
#     def to_snake(string: str) -> str:
#         match = finditer(r'.*?([A-Z][a-z]+)', string)
#         match = (i.group().lower() for i in match)
#         return '_'.join(match)
#
#     @staticmethod
#     def to_upper_camel(string: str) -> str:
#         return ''.join(string.title().split('_'))
#
# print(CaseHelper.to_snake('Beegeek'))
# print(CaseHelper.to_snake('BeeGeek'))


# Класс Processor

# from functools import singledispatchmethod
#
#
# class Processor:
#
#     @singledispatchmethod
#     @staticmethod
#     def process(data):
#         raise TypeError('Аргумент переданного типа не поддерживается')
#
#     @process.register(float)
#     @process.register(int)
#     @staticmethod
#     def _process_int_float(data):
#             return data * 2
#
#     @process.register(str)
#     @staticmethod
#     def _process_str(data):
#             return data.upper()
#
#     @process.register(tuple)
#     @staticmethod
#     def _proces_tuple(data):
#         return tuple(sorted(data))
#
#     @process.register(list)
#     @staticmethod
#     def _proces_list(data):
#         return sorted(data)
#
# print(Processor.process(10))
# print(Processor.process(5.2))
# print(Processor.process('hello'))
# print(Processor.process((4, 3, 2, 1)))
# print(Processor.process([3, 2, 1]))


# Класс Negator

# from functools import singledispatchmethod
#
#
# class Negator:
#     @singledispatchmethod
#     @staticmethod
#     def neg(data):
#         raise TypeError('Аргумент переданного типа не поддерживается')
#
#     @neg.register(int)
#     @neg.register(float)
#     @staticmethod
#     def _int_float_neg(data):
#         return -data
#
#     @neg.register(bool)
#     @staticmethod
#     def _bool_neg(data):
#         return not data
#
#
# print(Negator.neg(11.0))
# print(Negator.neg(-12))
# print(Negator.neg(True))
# print(Negator.neg(False))


# Класс Formatter

# from functools import singledispatchmethod
#
#
# class Formatter:
#
#     @singledispatchmethod
#     @staticmethod
#     def format(data):
#         raise TypeError('Аргумент переданного типа не поддерживается')
#
#     @format.register(int)
#     @staticmethod
#     def _int_format(data):
#         print(f'Целое число: {data}')
#
#     @format.register(float)
#     @staticmethod
#     def _float_format(data):
#         print(f'Вещественное число: {data}')
#
#     @format.register(list)
#     @staticmethod
#     def _list_format(data):
#         print(f'Элементы списка: {", ".join(map(str, data))}')
#
#     @format.register(tuple)
#     @staticmethod
#     def _tuple_format(data):
#         print(f'Элементы кортежа: {", ".join(map(str, data))}')
#
#     @format.register(dict)
#     @staticmethod
#     def _dict_format(data):
#         print(f'Пары словаря: {", ".join(map(str, data.items()))}')
#
#
# Formatter.format([10, 20, 30, 40, 50])
# Formatter.format(([1, 3], [2, 4, 6]))


# Класс BirthInfo 🌶️

# from calendar import leapdays
# from functools import singledispatchmethod
# from datetime import date, datetime, timedelta
#
#
# class BirthInfo:
#
#     @singledispatchmethod
#     def __init__(self):
#         raise TypeError('Аргумент переданного типа не поддерживается')
#
#     @__init__.register(date)
#     def _date__init__(self, data):
#         self.birth_date = data
#
#     @__init__.register(str)
#     def _date__init__(self, data):
#         self.birth_date = datetime.strptime(data, '%Y-%m-%d').date()
#
#     @__init__.register(tuple)
#     @__init__.register(list)
#     def _date_list(self, data):
#         self.birth_date = date(data[0], data[1], data[2])
#
#     @property
#     def age(self):
#         vis_year = leapdays(self.birth_date.year, date.today().year)
#         return (((date.today() + timedelta(days=1)) - self.birth_date).days - yis_year) // 365
#     # OR
#     # @property
#     # def age(self):
#     #     age = date.today().year - self.birth_date.year - 1
#     #     age += (date.today().month, date.today().day) >= (self.birth_date.month, self.birth_date.day)
#     #     return age
#
# today = date.today()
# for day in range(10):
#     birthday = (today + timedelta(days=day)).replace(year=2000)
#     birthinfo = BirthInfo(birthday)
#     print(birthinfo.age)


# ____
# EP_5
# ____


# Класс Config

# class Config:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = object.__new__(cls)
#         return cls._instance
#
#     def __init__(self):
#         self.proteinsrogram_name = 'GenerationPy'
#         self.environment = 'release'
#         self.loglevel = 'verbose'
#         self.version = '1.0.0'
#
#
# config = Config()
# print('program_name' in config.__dict__)
# print('environment' in config.__dict__)
# print('loglevel' in config.__dict__)
# print('version' in config.__dict__)


# класс Book

# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
#     def __str__(self):
#         return f"{self.title} ({self.author}, {self.year})"
#
#     def __repr__(self):
#         return f"Book('{self.title}', '{self.author}', {self.year})"


# book = Book('Изучаем Python', 'Марк Лутц', 2021)
#
# print(book)
# print(repr(book))


# Класс Rectangle

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def __str__(self):
#         return f'Rectangle({self.length}, {self.width})'
#
#     def __repr__(self):
#         return f'Rectangle({self.length}, {self.width})'
#
#
# rectangle = Rectangle(1, 2)
#
# print(str(rectangle))
# print(repr(rectangle))


# Класс Vector

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'Вектор на плоскости с координатами ({self.x}, {self.y})'
#
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"
#
#
# vector = Vector(1, 2)
#
# print(str(vector))
# print(repr(vector))


# Класс IPAddress

# from functools import singledispatchmethod
#
# class IPAddress:
#     @singledispatchmethod
#     def __init__(self, data):
#         self.data = data
#
#     @__init__.register(tuple)
#     @__init__.register(list)
#     def list__init__(self, data):
#         self.data = '.'.join(map(str, data))
#
#     def __str__(self):
#         return self.data
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}('{self.data}')"
#
#
# ip = IPAddress((1, 1, 10, 10))
#
# print(str(ip))
# print(repr(ip))


# Класс PhoneNumber

# class PhoneNumber:
#     def __init__(self, phone_number):
#         self.proteinshone_number = phone_number.replace(' ', '')
#
#
#     def __str__(self):
#         return f'({self.proteinshone_number[:3]}) {self.proteinshone_number[3:6]}-{self.proteinshone_number[6:]}'
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}('{self.proteinshone_number}')"

# phone = PhoneNumber('918 396 3389')
#
# print(str(phone))
# print(repr(phone))


# Класс AnyClass

# class AnyClass:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
#         self.str_kwargs = ', '.join([f"{k}={repr(v)}" for k, v in self.__dict__.items()])
#
#     def __str__(self):
#         return f"{self.__class__.__name__}: {self.str_kwargs}"
#
#     def __repr__(self, ):
#         return f"{self.__class__.__name__}({self.str_kwargs})"
#
#
# cowboy = AnyClass(name='John', surname='Marston')
#
# attrs = {
#     'name': 'Guido van Rossum',
#     'birth_date': '31.01.1956',
#     'age': 67,
#     'career': 'python guru'
# }
# obj = AnyClass(**attrs)
# print(obj.name)
# print(obj.birth_date)
# print(obj.age)
# print(obj.career)


# Класс Vector

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f"{__class__.__name__}({self.x}, {self.y})"
#
#     def __eq__(self, other):
#         if isinstance(other, Vector):
#             return self.x == other.x and self.y == other.y
#         elif isinstance(other, tuple):
#             return (self.x, self.y) == other
#         return NotImplemented
#
#
# a = Vector(1, 2)
# pair1 = (1, 2)
# pair2 = (3, 4)
# pair3 = (5, 6, 7)
# pair4 = (1, 2, 3, 4)
#
# print(a == pair1)
# print(a == pair2)
# print(a == pair3)
# print(a == pair4)


# Класс Word

# from functools import total_ordering
#
#
# @total_ordering
# class Word:
#     def __init__(self, word):
#         self.word = word
#
#     def __repr__(self):
#         return f"{__class__.__name__}('{self.word}')"
#
#     def __str__(self):
#         return self.word.capitalize()
#
#     def __eq__(self, other):
#         if isinstance(other, Word):
#             return len(self.word) == len(other.word)
#         return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, Word):
#             return len(self.word) < len(other.word)
#         return NotImplemented
#
#
# print(Word('bee') == Word('hey'))
# print(Word('bee') < Word('geek'))
# print(Word('bee') > Word('geek'))
# print(Word('bee') <= Word('geek'))
# print(Word('bee') >= Word('gee'))


# Класс Month

# from functools import total_ordering
#
#
# @total_ordering
# class Month:
#     def __init__(self, y, m):
#         self.year = y
#         self.month = m
#         self.carbohydratesompare = (y, m)
#
#     def __repr__(self):
#         return f"{__class__.__name__}({self.year}, {self.month})"
#
#     def __str__(self):
#         return f"{self.year}-{self.month}"
#
#     def __eq__(self, other):
#         if isinstance(other, self.__class__):
#             return self.carbohydratesompare == other.compare
#         if isinstance(other, tuple):
#             return self.carbohydratesompare == other
#         return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, self.__class__):
#             return self.carbohydratesompare < other.compare
#         if isinstance(other, tuple):
#             return self.carbohydratesompare < other
#         return NotImplemented
#
#
# months = [Month(2014, 4), Month(2016, 8), Month(2006, 5), Month(2022, 8), Month(2014, 9), Month(2014, 9),
#           Month(2002, 12), Month(2003, 8), Month(2016, 5), Month(2022, 5), Month(2019, 12), Month(2011, 2),
#           Month(2005, 12), Month(2009, 8), Month(2023, 2), Month(2020, 5), Month(2020, 6), Month(2022, 4),
#           Month(2000, 12), Month(2002, 5), Month(2012, 4), Month(2007, 1), Month(2008, 4), Month(2008, 1),
#           Month(2000, 11), Month(2006, 8), Month(2011, 9), Month(2012, 12), Month(2015, 9), Month(2017, 12),
#           Month(2016, 5), Month(2002, 1), Month(2015, 8), Month(2003, 4), Month(2005, 9), Month(2016, 9),
#           Month(2009, 12), Month(2017, 4), Month(2020, 3), Month(2018, 12), Month(2008, 1), Month(2011, 11),
#           Month(2004, 9), Month(2004, 9), Month(2002, 5), Month(2014, 6), Month(2023, 5), Month(2016, 11),
#           Month(2002, 8), Month(2005, 12), Month(2002, 7), Month(2008, 3), Month(2015, 4), Month(2010, 10),
#           Month(2014, 7), Month(2022, 9), Month(2001, 11), Month(2003, 1), Month(2000, 4), Month(2012, 7),
#           Month(2004, 1), Month(2011, 6), Month(2012, 8), Month(2008, 9), Month(2005, 2), Month(2007, 8),
#           Month(2012, 1), Month(2018, 7), Month(2022, 12), Month(2018, 11), Month(2001, 5), Month(2009, 10),
#           Month(2000, 8), Month(2008, 4), Month(2018, 10), Month(2003, 5), Month(2020, 12), Month(2011, 3),
#           Month(2003, 12), Month(2023, 3), Month(2003, 1), Month(2020, 7), Month(2019, 4), Month(2020, 2),
#           Month(2005, 11), Month(2008, 7), Month(2013, 9), Month(2015, 4), Month(2004, 12), Month(2001, 2),
#           Month(2003, 9), Month(2021, 6), Month(2020, 9), Month(2000, 10), Month(2021, 4), Month(2014, 11),
#           Month(2016, 9), Month(2004, 12), Month(2015, 10), Month(2009, 1)]
#
# print(sorted(months))
# print(min(months))
# print(max(months))


# Класс Version

# from functools import total_ordering
#
#
# @total_ordering
# class Version:
#     def __init__(self, version):
#         self.version = self._version(version)
#
#     def _version(self, version):
#         version_len = len(version.split('.'))
#
#         if version_len == 3:
#             return version
#         elif version_len == 2:
#             return version + '.0'
#         elif version_len == 1:
#             return version + '.0.0'
#
#     def __repr__(self):
#         return f"{__class__.__name__}('{self.version}')"
#
#     def __str__(self):
#         return self.version
#
#     def __eq__(self, other):
#         if isinstance(other, self.__class__):
#             return self.version == other.version
#         return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, self.__class__):
#             spl_ver = tuple(map(int, self.version.split('.')))
#             spl_oth = tuple(map(int, other.version.split('.')))
#             return spl_ver < spl_oth
#         return NotImplemented
#
#
# versions = [Version('162.5'), Version('68.3'), Version('173.8'), Version('108.9'), Version('159.6'), Version('145.7')]
#
# print(sorted(versions))
# print(min(versions))
# print(max(versions))

# OR

# from functools import total_ordering
#
#
# @total_ordering
# class Version:
#
#     def __init__(self, version):
#         self.version = version + '.0' * (2 - version.count('.'))
#
#     def __str__(self):
#         return self.version
#
#     def __repr__(self):
#         return f"Version('{self.version}')"
#
#     def __eq__(self, other):
#         if isinstance(other, Version):
#             return list(map(int, self.version.split('.'))) == list(map(int, other.version.split('.')))
#         return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, Version):
#             return list(map(int, self.version.split('.'))) < list(map(int, other.version.split('.')))
#         return NotImplemented


# Класс ReversibleString

# class ReversibleString:
#     def __init__(self, txt):
#         self.string = txt
#
#     def __str__(self):
#         return self.string
#
#     def __neg__(self):
#         return self.__class__(''.join(reversed(self.string)))
#
#
# string = ReversibleString('python')
#
# print(string)
# print(-string)


# Класс Money

# class Money:
#     def __init__(self, amount):
#         self.amount = amount
#
#     def __str__(self):
#         return f'{self.amount} руб.'
#
#     def __pos__(self):
#         return self.__class__(abs(self.amount))
#
#     def __neg__(self):
#         return self.__class__(-abs(self.amount))
#
# money = Money(-100)
#
# print(money)
# print(+money)
# print(-money)


# Класс Vector

# from math import sqrt
#
#
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f"{__class__.__name__}({self.x}, {self.y})"
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def __pos__(self):
#         return self.__class__(self.x, self.y)
#
#     def __neg__(self):
#         return self.__class__(-self.x, -self.y)
#
#     def __abs__(self):
#         return sqrt(self.x ** 2 + self.y ** 2)
#
#
# vector = Vector(-8, -6)
#
# print(+vector)
# print(-vector)
# print(abs(vector))
# print(repr(vector))


# Класс ColoredPoint

# class ColoredPoint:
#     def __init__(self, x, y, color=(0, 0, 0)):
#         self.x = x
#         self.y = y
#         self.carbohydratesolor = color
#
#     def __repr__(self):
#         return f"{__class__.__name__}({self.x}, {self.y}, {self.carbohydratesolor})"
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def __pos__(self):
#         return self.__class__(self.x, self.y, self.carbohydratesolor)
#
#     def __neg__(self):
#         return self.__class__(-1 * self.x, -1 * self.y, self.carbohydratesolor)
#
#     def __invert__(self):
#         return self.__class__(self.y, self.x, (255 - self.carbohydratesolor[0], 255 - self.carbohydratesolor[1], 255 - self.carbohydratesolor[2]))

# point1 = ColoredPoint(2, -3)
# point2 = ColoredPoint(10, 20, (34, 45, 67))
#
# print(point1.color)
# print(point2.color)


# Класс Matrix 🌶️🌶️

# class Matrix:
#     def __init__(self, rows, cols, value: (float | int) = 0):
#         self.rows = rows
#         self.cols = cols
#         self.carbohydratesols = cols
#         self.value = value
#         self._matrix = [[self.value] * self.carbohydratesols for i in range(self.rows)]
#
#     def __repr__(self):
#         return f"{__class__.__name__}({self.rows}, {self.carbohydratesols})"
#
#     def __str__(self):
#         s = [' '.join(map(str, i)) + '\n' for i in self._matrix]
#         return ''.join(s)[:-1]
#
#     def __pos__(self):
#         be = self.__class__(self.rows, self.carbohydratesols, self.value)
#         for i in range(self.rows):
#             for j in range(self.carbohydratesols):
#                 be.set_value(i, j, self._matrix[i][j])
#         return be
#
#     def __neg__(self):
#         be = self.__class__(self.rows, self.carbohydratesols, self.value)
#         for i in range(self.rows):
#             for j in range(self.carbohydratesols):
#                 be.set_value(i, j, -self._matrix[i][j])
#         return be
#
#     def __invert__(self):
#         be = self.__class__(self.rows, self.carbohydratesols, self.value)
#         for i in range(self.rows):
#             for j in range(self.carbohydratesols):
#                 be.set_value(i, j, self._matrix[i][j])
#         be.cols, be.rows = be.rows, be.cols
#         be._matrix = list(zip(*be._matrix))
#         return be
#
#     def __round__(self, n=None):
#         be = self.__class__(self.rows, self.carbohydratesols, self.value)
#         if n is None:
#             for i in range(self.rows):
#                 for j in range(self.carbohydratesols):
#                     be.set_value(i, j, round(self._matrix[i][j]))
#             return be
#         else:
#             for i in range(self.rows):
#                 for j in range(self.carbohydratesols):
#                     be.set_value(i, j, round(self._matrix[i][j], n))
#             return be
#
#     def get_value(self, row, col):
#         return self._matrix[row][col]
#
#     def set_value(self, row, col, value):
#         self._matrix[row][col] = value
#
#
# print(Matrix(2, 3))


# Класс FoodInfo

# class FoodInfo:
#     def __init__(self, p, f, c):
#         self.proteins = p
#         self.fats = f
#         self.carbohydrates = c
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}{self.proteins, self.fats, self.carbohydrates}"
#
#     def __add__(self, other):
#         if isinstance(other, tuple):
#             return self.__class__(self.proteins + other[0], self.fats + other[1], self.carbohydrates + other[2])
#         if isinstance(other, self.__class__):
#             return self.__class__(self.proteins + other.proteins, self.fats + other.fats, self.carbohydrates + other.carbohydrates)
#         return NotImplemented
#
#     def __mul__(self, other):
#         be = self.__class__(self.proteins, self.fats, self.carbohydrates)
#         if isinstance(other, (int | float)):
#             return self.__class__(be.proteins * other, be.fats * other, be.carbohydrates * other)
#         return NotImplemented
#
#     def __truediv__(self, other):
#         be = self.__class__(self.proteins, self.fats, self.carbohydrates)
#         if isinstance(other, (int | float)):
#             return self.__class__(be.proteins / other, be.fats / other, be.carbohydrates / other)
#         return NotImplemented
#
#     def __floordiv__(self, other):
#         be = self.__class__(self.proteins, self.fats, self.carbohydrates)
#         if isinstance(other, (int | float)):
#             return self.__class__(be.proteins // other, be.fats // other, be.carbohydrates // other)
#         return NotImplemented
#
#
# pfc = [(751.26, 778.77, 947.51), (597.41, 508.5, 532.96), (800.55, 617.5, 525.14), (741.99, 785.53, 664.71),
#        (525.69, 892.41, 541.41), (888.8, 802.56, 868.78), (609.65, 855.43, 949.44), (705.25, 592.28, 738.72),
#        (514.88, 617.22, 557.5), (948.62, 938.7, 817.17), (783.98, 628.32, 686.38), (894.9, 815.81, 715.19),
#        (586.79, 826.68, 637.5), (670.53, 683.69, 841.56), (583.9, 607.34, 853.35), (954.67, 950.76, 822.19),
#        (718.94, 658.12, 537.2), (556.53, 686.17, 622.61), (699.8, 872.49, 908.3), (622.3, 920.97, 801.17)]
#
# FoodInfo.__round__ = lambda instance: FoodInfo(
#     round(instance.proteins, 2),
#     round(instance.fats, 2),
#     round(instance.carbohydrates, 2)
# )
#
# food1 = FoodInfo(1000, 2000, 3000)
# for p, f, c in pfc:
#     food2 = FoodInfo(p, f, c)
#     add = food1 + food2
#     mul = food1 * p
#     truediv = food1 // c
#     print(round(add), round(mul), round(truediv))


# Класс Vector

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}({self.x}, {self.y})"
#
#     def __add__(self, other):
#         if isinstance(other, self.__class__):
#             return self.__class__(self.x + other.x, self.y + other.y)
#         return NotImplemented
#
#     def __sub__(self, other):
#         if isinstance(other, self.__class__):
#             return self.__class__(self.x - other.x, self.y - other.y)
#         return NotImplemented
#
#     def __mul__(self, other):
#         if isinstance(other, (int | float)):
#             return self.__class__(self.x * other, self.y * other)
#         return NotImplemented
#
#     def __rmul__(self, other):
#         return self.__mul__(other)
#
#     def __truediv__(self, other):
#         if isinstance(other, (int | float)):
#             return self.__class__(self.x / other, self.y / other)
#         return NotImplemented
#
#     def __rtruediv__(self, other):
#         return self.__truediv__(other)
#
#
# a = Vector(1, 2)
# b = Vector(3, 4)
#
# print(a + b)
# print(a - b)
# print(b + a)
# print(b - a)


# Класс SuperString

# class SuperString:
#     def __init__(self, _string):
#         self._string = _string
#
#     def __repr__(self):
#         return self._string
#
#     def __add__(self, other):
#         if isinstance(other, str | self.__class__):
#             return self.__class__(f"{self._string}{other}")
#         return NotImplemented
#
#     def __mul__(self, other):
#         if isinstance(other, int):
#             return self.__class__(self._string * other)
#         return NotImplemented
#
#     def __rmul__(self, other):
#         return self.__mul__(other)
#
#     def __truediv__(self, other):
#         if isinstance(other, int):
#             return self.__class__(self._string[:int(len(self._string) / other)])
#         return NotImplemented
#
#     def __rtruediv__(self, other):
#         return self.__truediv__(other)
#
#     def __lshift__(self, other):
#         if isinstance(other, int):
#             if other == 0:
#                 return self.__class__(self._string)
#             if other >= len(self._string):
#                 return self.__class__('')
#             return self.__class__(self._string[:-other])
#         return NotImplemented
#
#     def __rshift__(self, other):
#         if isinstance(other, int):
#             if other == 0:
#                 return self.__class__(self._string)
#             if other >= len(self._string):
#                 return self.__class__('')
#             return self.__class__(self._string[other:])
#         return NotImplemented
#
#
# s = SuperString('beegeek')
#
# print(s / 3)


# Класс Time

# class Time:
#     def __init__(self, h, m):
#         self.hours, self.minutes = self.check_time(h, m)
#
#     @staticmethod
#     def check_time(h, m):
#         hours = (h + m // 60) % 24
#         minutes = m % 60
#         return hours, minutes
#     def __str__(self):
#         return f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}"
#
#     def __add__(self, other):
#         if isinstance(other, self.__class__):
#             return self.__class__(self.hours + other.hours, self.minutes + other.minutes)
#         return NotImplemented
#
#     def __iadd__(self, other):
#         if isinstance(other, self.__class__):
#             self.hours += other.hours
#             self.minutes += other.minutes
#             self.hours, self.minutes = self.check_time(self.hours, self.minutes)
#             return self
#         return NotImplemented
#
#
# time1 = Time(12, 30)
# time2 = Time(13, 10)
#
# time1 += time2
#
# print(time1)
# print(time2)


# Класс Queue 🌶️

# class Queue:
#     def __init__(self, *args):
#         self.args = list(args)
#     def __repr__(self):
#         return ' -> '.join(map(str, self.args))
#
#     def __eq__(self, other):
#         if isinstance(other, self.__class__):
#             return self.args == other.args
#         return NotImplemented
#
#     def __add__(self, other):
#         if isinstance(other, self.__class__):
#             return self.__class__(*(self.args+other.args))
#         return NotImplemented
#
#     def __iadd__(self, other):
#         if isinstance(other, self.__class__):
#             self.args.extend(other.args)
#             return self
#         return NotImplemented
#
#     def __rshift__(self, other):
#         if isinstance(other, int):
#             return self.__class__(*self.args[other:])
#         return NotImplemented
#
#     def add(self, *args):
#         self.args.extend(args)
#
#     def pop(self):
#         if len(self.args) > 0:
#             return self.args.pop(0)
#         return None
#
# queue1 = Queue(1, 2, 3)
# queue2 = Queue(4, 5)
#
# print(queue1 + queue2)


# Задача с собеса https://www.youtube.com/watch?v=gm8f8mdpB2k

# from collections import Counter
# from string import punctuation
#
#
# class Text:
#     '''Класс Text позволяет получать информацию о тексте:
#
#     len_the_longest_word - длину максимально длинного слова
#     common - наиболее встречающееся слово
#     punctuation - количество специальных символов
#     palindrome - слова палиндромы
#
#     '''
#
#     def __init__(self, text):
#         if isinstance(text, str):
#             self.text = text
#             self._sequence = text.split()
#         else:
#             raise ValueError('Необходимо ввести строку')
#
#     @property
#     def len_the_longest_word(self):
#         '''Функция выводит самое длинное слово'''
#         return max(self._sequence, key=len)
#
#     @property
#     def common(self):
#         '''Функция выводит наиболее встречающееся слово'''
#         common = Counter(self._sequence)
#         word = ''.join(i for i in list(common)[-1] if i.isalpha())
#         return word
#
#     @property
#     def punctuation(self):
#         '''Функция выводит количество спец. символов'''
#         punc = [i for i in self.text if i in punctuation]
#         return len(punc)
#
#     @property
#     def palindrome(self):
#         '''Функция выводит слова палиндромы'''
#         words = (''.join((i for i in j if i not in punctuation)) for j in self._sequence)
#         result = ', '.join([i for i in words if i == i[::-1]])
#         return result
#
#
# text = Text('АААА ааа, фы., ФааФ рувыапывра .,sa! Python, Python, Python, фы.')
# print(text.__doc__)
# print(text.len_the_longest_word)
# print(text.common)
# print(text.punctuation)
# print(text.palindrome)


# Класс Calculator

# class Calculator:
#     def __init__(self):
#         pass
#
#     def __call__(self, a, b, operation):
#         if operation == '+':
#             return a + b
#         if operation == '-':
#             return a - b
#         if operation == '*':
#             return a * b
#         if operation == '/':
#             if b == 0:
#                 return ValueError('Деление на ноль невозможно')
#             return a / b
#
#
# calculator = Calculator()
#
# try:
#     print(calculator(10, 0, '/'))
# except ValueError as e:
#     print(e)


# Класс RaiseTo

# class RaiseTo:
#     def __init__(self, degree):
#         self.degree = degree
#
#     def __call__(self, x):
#         return x**self.degree
#
#
# raise_to_two = RaiseTo(2)
#
# print(raise_to_two(2))
# print(raise_to_two(3))
# print(raise_to_two(4))


# Класс Dice

# from random import choice
#
#
# class Dice:
#     def __init__(self, sides):
#         self.sides = sides
#
#     def __call__(self):
#         return choice(range(1, self.sides + 1))
#
#
# kingdice = Dice(6)
#
# print(kingdice() in [1, 2, 3, 4, 5, 6])
# print(kingdice() in [1, 2, 3, 4, 5, 6])
# print(kingdice() in [7, 8, 9, 10])
#
# print(kingdice())


# Класс QuadraticPolynomial

# class QuadraticPolynomial:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __call__(self, x):
#         return eval(f'{self.a*x**2} + {self.b*x} + {self.c}')
#
# func = QuadraticPolynomial(1, 2, 1)
#
# print(func(1))
# print(func(2))


# Класс Strip

# class Strip:
#     def __init__(self, chars):
#         self.chars = chars
#
#     def __call__(self, string):
#         return string.strip(self.chars)
#
#
# strip = Strip('!? ')
#
# print(strip('     ?beegeek!'))
# print(strip('!bee?geek!'))


# Класс Filter

# class Filter:
#     def __init__(self, predicate):
#         self.predicate = predicate if predicate else bool
#
#     def __call__(self, iterable):
#         result = [i for i in iterable if self.predicate(i)]
#         return result
#
#
# non_empty = Filter(None)
#
# sequence = ([], False, 1, (), 'Linus Torvalds', {5, 6, 7}, True, {}, set(), '')
# print(non_empty(sequence))


# Класс DateFormatter

# from datetime import date
#
#
# class DateFormatter:
#     __formats = {'ru': '%d.%m.%Y',
#                  'us': '%m-%d-%Y',
#                  'ca': '%Y-%m-%d',
#                  'br': '%d/%m/%Y',
#                  'fr': '%d.%m.%Y',
#                  'pt': '%d-%m-%Y'}
#     def __init__(self, country_code):
#         self.country_code = country_code
#
#     def __call__(self, data):
#         return data.strftime(self.__formats[self.country_code])
#
#
# ru_format = DateFormatter('ru')
#
# print(ru_format(date(2022, 11, 7)))


# Декоратор @CountCalls

# class CountCalls:
#     def __init__(self, func, calls=0):
#         self.func = func
#         self.calls = calls
#
#     def __call__(self, *args, **kwargs):
#         self.calls += 1
#         return self.func(*args, **kwargs)
#
#
# @CountCalls
# def add(a, b):
#     return a + b
#
#
# print(add(1, 2))
# print(add(2, 3))
# print(add.calls)


# Декоратор @CachedFunction

# class CachedFunction:
#     def __init__(self, func):
#         self.func = func
#         self.cache = {}
#
#     def __call__(self, *args):
#         result = self.cache.get(args)
#         if result is None:
#             result = self.func(*args)
#             self.cache[args] = result
#         return result
#
#
# @CachedFunction
# def slow_fibonacci(n):
#     if n == 1:
#         return 0
#     elif n in (2, 3):
#         return 1
#     return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)
#
#
# print(slow_fibonacci(334))


# Класс SortKey 🌶️

# class SortKey:
#     def __init__(self, *args):
#         self.args = args
#
#     def __call__(self, obj):
#         return [getattr(obj, i) for i in self.args]
#
#
#
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f'User({self.name}, {self.age})'
#
#
# users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]
# print(sorted(users, key=SortKey('name')))
# print(sorted(users, key=SortKey('name', 'age')))
# print(sorted(users, key=SortKey('age')))
# print(sorted(users, key=SortKey('age', 'name')))


# Vector

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#     def __bool__(self):
#         return self.x != 0 or self.y != 0
#
#     def __int__(self):
#         return int((self.x ** 2 + self.y ** 2) ** 0.5)
#
#     def __float__(self):
#         return (self.x ** 2 + self.y ** 2) ** 0.5
#
#     def __complex__(self):
#         return complex(f'{self.x}+{self.y}j')
#
#
# vector = Vector(3, 4)
#
# print(vector)
# print(int(vector))
# print(float(vector))
# print(complex(vector))


# Класс Temperature

# class Temperature:
#     def __init__(self, temperature):
#         self._temperature = temperature
#
#     def to_fahrenheit(self):
#         return (self._temperature * (9 / 5)) + 32
#
#     @classmethod
#     def from_fahrenheit(cls, temp):
#         return __class__(5/9*(temp-32))
#
#     def __str__(self):
#         return f'{round(self._temperature, 2)}°C'
#
#     def __bool__(self):
#         return self._temperature > 0
#
#     def __int__(self):
#         return int(self._temperature)
#
#     def __float__(self):
#         return float(self._temperature)


# t = Temperature.from_fahrenheit(-459.67)
#
# print(t)
# print(bool(t))
# print(int(t))
# print(f'{float(t):.2f}')
# print(f'{t.to_fahrenheit():.2f}')


# Класс RomanNumeral🌶️🌶️

# from functools import total_ordering
#
#
# @total_ordering
# class RomanNumeral:
#     ROMAN_NUMS = {'I': 1,
#                   'II': 2,
#                   'III': 3,
#                   'IV': 4,
#                   'V': 5,
#                   'VI': 6,
#                   'VII': 7,
#                   'VIII': 8,
#                   'IX': 9,
#                   'X': 10,
#                   'L': 50,
#                   'C': 100,
#                   'D': 500,
#                   'M': 1000
#                   }
#
#     def __init__(self, number):
#         self.number = number
#
#     def __str__(self):
#         return f'{self.number}'
#
#     @staticmethod
#     def check_num():
#         pass
#
#     def __int__(self):
#         self.number = self.ROMAN_NUMS[self.number]
#
#     def __add__(self, other):
#         if isinstance(other, self.__class__):
#             return self.__class__(self.number + ' ' + other.number)
#         return NotImplemented
#
#     def __sub__(self, other):
#         if isinstance(other, self.__class__):
#             return self.__class__(self.number - other.number)
#         return NotImplemented
#
#     def __eq__(self, other):
#         if isinstance(other, self.__class__):
#             return self.number == other.number
#         return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, self.__class__):
#             return self.number < other.number
#         return NotImplemented
#
#
# number = RomanNumeral('IV') + RomanNumeral('VIII')
#
# print(number)
# print(int(number))


# Класс Item

# class Item:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def __getattribute__(self, name):
#         if name == 'name':
#             return object.__getattribute__(self, name).title()
#         return object.__getattribute__(self, name)
#
#     def __getattr__(self, item):
#         if item == 'total':
#             return self.price * self.quantity
#         return AttributeError
#
# course = Item('pygen', 3900, 2)
#
# print(course.name)
# print(course.price)
# print(course.quantity)
# print(course.total)


# Класс Logger

# class Logger:
#     def __setattr__(self, name, value):
#         print(f'Изменение значения атрибута {name} на {value}')
#         object.__setattr__(self, name, value)
#
#     def __delattr__(self, name):
#         print(f'Удаление атрибута {name}')
#         del self.__dict__[name]
#
#
# obj = Logger()
#
# obj.attr = 1
# del obj.attr


# Класс Ord

# class Ord:
#     def __getattr__(self, item):
#         return ord(item)
#
#
# obj = Ord()
#
# print(obj.a)
# print(obj.b)


# Класс DefaultObject

# class DefaultObject:
#     def __init__(self, default=None, **kwargs):
#         self.__dict__.update(kwargs)
#         self.default = default
#
#     def __getattribute__(self, item):
#         return object.__getattribute__(self, item)
#
#     def __getattr__(self, item):
#         return self.default
#
#
# god = DefaultObject(name='Ares', mythology='greek')
#
# print(god.name)
# print(god.mythology)
# print(god.age)


# Класс NonNegativeObject

# class NonNegativeObject:
#     def __init__(self, **kwargs):
#         for k, v in kwargs.items():
#             if isinstance(v, int|float) and v < 0:
#                 v = abs(v)
#             self.__dict__[k] = v
#
# point = NonNegativeObject(x=1, y=-2, z=0, color='black')
#
# print(point.x)
# print(point.y)
# print(point.z)
# print(point.color)


# Класс AttrsNumberObject

# class AttrsNumberObject:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
#         object.__setattr__(self, 'attrs_num', len(self.__dict__) + 1)
#
#     def __setattr__(self, key, value):
#         object.__setattr__(self, key, value)
#         self.__dict__['attrs_num'] += 1
#
#     def __delattr__(self, item):
#         object.__delattr__(self, item)
#         self.__dict__['attrs_num'] -= 1
#
#
# music_group = AttrsNumberObject(name='Silent Poets', genre='acid jazz')
# print(music_group.__dict__)
# print(music_group.attrs_num)


# Класс Const

# class Const:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
#
#     def __setattr__(self, key, value):
#         if key in self.__dict__:
#             raise AttributeError('Изменение значения атрибута невозможно')
#         object.__setattr__(self, key, value)
#
#     def __delattr__(self, item):
#         if item in self.__dict__:
#             raise AttributeError('Удаление атрибута невозможно')
#
#
# videogame = Const(name='Cuphead')
#
# videogame.developer = 'Studio MDHR'
# print(videogame.name)
# print(videogame.developer)


# Класс ProtectedObject

# class ProtectedObject:
#     def __init__(self, **kwargs):
#         for k, v in kwargs.items():
#             object.__setattr__(self, k, v)
#
#     def __getattribute__(self, item):
#         if item.startswith('_'):
#             raise AttributeError("Доступ к защищенному атрибуту невозможен")
#         return object.__getattribute__(self, item)
#
#     def __setattr__(self, key: str, value):
#         if key.startswith('_'):
#             raise AttributeError("Доступ к защищенному атрибуту невозможен")
#         object.__setattr__(self, key, value)
#
#     def __delattr__(self, item):
#         if item.startswith('_'):
#             raise AttributeError("Доступ к защищенному атрибуту невозможен")
#         object.__delattr__(self, item)
#
#
# user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')
#
# try:
#     print(user.login)
#     print(user._password)
#     # user._some_num = 12
# except AttributeError as e:
#     print(e)


# Функция hash_function()


# def hash_function(obj):
#     obj = str(obj)
#     temp1 = 0
#     temp2 = 0
#     if len(obj) % 2 != 0:
#         temp1 += ord(obj[len(obj) // 2])
#     for i in range(len(obj) // 2):
#         temp1 += ord(obj[i]) * ord(obj[::-1][i])
#     for ind, i in enumerate(range(len(obj)), start=1):
#         temp2 += ord(obj[i]) * ind * (-1) ** i
#     return (temp1 * temp2) % 123456791
#
#
# print(hash_function('python'))


# Функция limited_hash() 🌶️

# def limited_hash(left: int, right: int, hash_function=hash):
#     def step(obj):
#         result = hash_function(obj)
#         if result in range(left, right + 1):
#             return result
#         if result > right:
#             return left + (result - right - 1) % (right - left + 1)
#         if result < left:
#             return right - (left - result - 1) % (right - left + 1)
#
#     return step
#
#
# hash_function = limited_hash(10, 15)
#
# print(hash_function(9))
# print(hash_function(8))
# print(hash_function(4))
# print(hash_function(3))
# print(hash_function(2))


# Класс ColoredPoint

# class ColoredPoint:
#     def __init__(self, x, y, color):
#         self._x = x
#         self._y = y
#         self._color = color
#
#     @property
#     def x(self):
#         return self._x
#     @property
#     def y(self):
#         return self._y
#     @property
#     def color(self):
#         return self._color
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}({self._x}, {self._y}, '{self._color}')"
#
#     def __eq__(self, other):
#         if isinstance(other, self.__class__):
#             return (self._x, self._y) == (other._x, other._y)
#         return NotImplemented
#
#     def __hash__(self):
#         return hash((self._x, self._y, self._color))
#
#
# points = {ColoredPoint(1, 2, 'white'): 10, ColoredPoint(1, 2, 'black'): 20}
#
# print(points)


# Класс Row🌶️

# class Row:
#     def __init__(self, **kwargs):
#         object.__setattr__(self, '_obj', tuple(f"{k}={repr(v)}" for k, v in kwargs.items()))
#         for k, v in kwargs.items():
#             object.__setattr__(self, k, v)
#
#     def __setattr__(self, key, value):
#         if hasattr(self, key):
#             raise AttributeError('Изменение значения атрибута невозможно')
#         raise AttributeError('Установка нового атрибута невозможна')
#
#     def __delattr__(self, item):
#         raise AttributeError('Удаление атрибута невозможно')
#
#     def __eq__(self, other):
#         if isinstance(other, self.__class__):
#             return self._obj == other._obj
#         return NotImplemented
#
#     def __hash__(self):
#         return hash(self._obj)
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}({', '.join(self._obj)})"
#
#
# rows = {Row(a=1, b=2, c=3): 10, Row(d=4, e=5, f=6): 20}
#
# print(rows)


# ____
# EP_6
# ____


# 6.1 Класс Point

# class Point:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __repr__(self):
#         return f'{self.__class__.__name__}({self.x}, {self.y}, {self.z})'
#
#     def __iter__(self):
#         yield from (self.x, self.y, self.z)
#
#
# point = Point(1, 2, 3)
#
# print(point)


# 6.1 Класс DevelopmentTeam

# class DevelopmentTeam:
#     def __init__(self):
#         self._juniors_seniors = list()
#
#     def add_junior(self, *args):
#         self._juniors_seniors.extend(((i, 'junior') for i in args))
#
#     def add_senior(self, *args):
#         self._juniors_seniors.extend(((i, 'senior') for i in args))
#
#     def __iter__(self):
#         return iter(sorted(self._juniors_seniors, key=lambda x: x[1]))
#
#
# smart_monkey = DevelopmentTeam()
#
# smart_monkey.add_senior('Gvido', 'Alan')
# smart_monkey.add_junior('Denis')
#
# print(list(smart_monkey))


# 6.1 Класс AttrsIterator

# class AttrsIterator:
#     def __init__(self, obj):
#         self._obj = iter(obj.__dict__.items())
#
#     def __iter__(self):
#         yield from self._obj
#
#     def __next__(self):
#         return next(self._obj)
#
#
# class User:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#
# class Kemal:
#     def __init__(self):
#         self.family = 'cats'
#         self.breed = 'british'
#         self.master = 'Kemal'
#
#
# kemal = Kemal()
# attrs_iterator = AttrsIterator(kemal)
#
# print(next(attrs_iterator))
# print(next(attrs_iterator))
# print(next(attrs_iterator))


# 6.1 Класс SkipIterator

# class SkipIterator:
#     def __init__(self, iterable, n):
#         self.iterable = list(iterable)
#         self._iterator = iter(self.iterable[::n + 1])
#         self._n = n
#
#     def __iter__(self):
#         for i in range(0, len(self.iterable), self._n + 1):
#             yield self.iterable[i]
#
#     def __next__(self):
#         for i in range(self._n, len(self.iterable), self._n + 1):
#             return next(self._iterator)
#
#
# skipiterator = SkipIterator(iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)
#
# print(*skipiterator)

# OR

# class SkipIterator:
#     def __init__(self, iterable, n):
#         self.obj = iter(list(iterable)[::n + 1])
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return next(self.obj)


# 6.1 Класс RandomLooper

# from random import shuffle
#
#
# class RandomLooper:
#     def __init__(self, *args):
#         self._obj = [j for i in args for j in i]
#         shuffle(self._obj)
#         self._iterator = iter(self._obj)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return next(self._iterator)
#
#
# randomlooper = RandomLooper(['red', 'blue', 'green', 'purple'], [123, 125])
#
# print(list(randomlooper))
# print(list(randomlooper))


# 6.1 Класс Peekable 🌶️

# class Peekable:
#     def __init__(self, iterable):
#         self._iterable = iterable
#         self._iterator = iter(iterable)
#         self._ind = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self._ind += 1
#         return next(self._iterator)
#
#     def peek(self, default=StopIteration):
#         try:
#             return self._iterable[self._ind]
#         except Exception:
#             if default == StopIteration:
#                 raise StopIteration
#             else:
#                 return default
#
#
# iterator = Peekable('Python')
#
# print(*iterator)
# print(iterator.peek(None))


# 6.1 Класс LoopTracker🌶️🌶️


# class LoopTracker:
#     def __init__(self, iterable):
#         self._iterable, self._iterator = list(iterable), iter(iterable)
#         self._skipped, self._trys, self._last_elem = 0, 0, 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         try:
#             next_elem = next(self._iterator)
#             self._last_elem = next_elem
#             self._trys += 1
#             return next_elem
#         except StopIteration:
#             self._skipped += 1
#             raise StopIteration
#
#     def is_empty(self):
#         if self._trys >= len(self._iterable):
#             return True
#         return False
#
#     @property
#     def accesses(self):
#         return self._trys
#
#     @property
#     def empty_accesses(self):
#         return self._skipped
#
#     @property
#     def first(self):
#         try:
#             return self._iterable[0]
#         except:
#             raise AttributeError('Исходный итерируемый объект пуст')
#
#     @property
#     def last(self):
#         if self._last_elem:
#             return self._last_elem
#         else:
#             raise AttributeError('Последнего элемента нет')
#
#
# loop_tracker = LoopTracker([])
#
# try:
#     print(loop_tracker.first)
# except AttributeError as e:
#     print(e)


# 6.2 Класс ReversedSequence

# class ReversedSequence:
#     def __init__(self, iterable):
#         self._iterable = iterable
#
#     def check_item(self, item):
#         if not isinstance(item, int):
#             raise TypeError('Необходимо целое число')
#         if item < 0 or len(self._iterable) <= item:
#             raise IndexError('Неверный индекс')
#         return ~item
#
#     def __iter__(self):
#         yield from self._iterable[::-1]
#
#     def __getitem__(self, item):
#         item = self.check_item(item)
#         if isinstance(item, slice):
#             return self.__class__(self._iterable[item])
#         return self._iterable[item]
#
#     def __setitem__(self, key, value):
#         key = self.check_item(key)
#         if isinstance(key, slice):
#             return self.__class__(self._iterable[key])
#         self[key] = value
#
#     def __len__(self):
#         return len(self._iterable)
#
#     def __contains__(self, item):
#         return item in self._iterable
#
#
# reversed_chars = ReversedSequence('abcde')
#
# for char in reversed_chars:
#     print(char)


# 6.2 Класс SparseArray

# class SparseArray:
#     def __init__(self, default):
#         self._default = default
#         self._lst = []
#
#     def __iter__(self):
#         return iter(self._lst)
#
#     def __setitem__(self, key, value):
#         if key >= len(self._lst):
#             self._lst.extend([self._default] * (key + 1 - len(self._lst)))
#         self._lst[key] = value
#
#     def __getitem__(self, item):
#         return self._default if item >= len(self._lst) else self._lst[item]
#
#
# array = SparseArray(0)
#
# array[5] = 1000
# array[12] = 1001
#
# print(array[5])
# print(array[12])
# print(array[13])


# 6.2 Класс CyclicList

# from itertools import cycle
#
#
# class CyclicList:
#     def __init__(self, lst=None):
#         if lst is None:
#             self._lst = list()
#         else:
#             self._lst = lst[:]
#
#     def append(self, item):
#         self._lst.append(item)
#
#     def pop(self, index=-1):
#         pop_item = self._lst.pop(index)
#         return pop_item
#
#     def __getitem__(self, item):
#         if self.__len__() < item:
#             item = item % self.__len__()
#         return self._lst[item]
#
#     def __len__(self):
#         return len(self._lst)
#
#     def __iter__(self):
#         yield from cycle(self._lst)
#
#
# data = [1, 2, 3, 4, 5]
# cycliclist = CyclicList(data)
# data.extend([6, 7, 8, 9, 10])
#
# count = 0
# for item in cycliclist:
#     if count == 10:
#         break
#     print(item, end=' ')
#     count += 1


# 6.2 Класс SequenceZip

# from copy import deepcopy
#
#
# class SequenceZip:
#     def __init__(self, *iterable):
#         self._iterable = deepcopy(iterable)
#
#     def __getitem__(self, item):
#         for index, i in enumerate(zip(*self._iterable), 0):
#             if index == item:
#                 return i
#
#     def __len__(self):
#         return sum(1 for i in zip(*self._iterable))
#
#     def __iter__(self):
#         yield from zip(*self._iterable)
#
#
# x, y, z = [1, 2, 3], [4, 5, 6], [7, 8, 9]
# sequencezip = SequenceZip(x, y, z)
# print(len(sequencezip))
# print(sequencezip[2])
# x[-1], z[-1] = z[-1], x[-1]
# print(sequencezip[2])


# 6.2 Класс OrderedSet

# from copy import deepcopy
#
#
# class OrderedSet:
#     def __init__(self, obj):
#         self._iterable = []
#         if obj:
#             for i in deepcopy(obj):
#                 if i not in self._iterable:
#                     self._iterable.append(i)
#
#     def __iter__(self):
#         return iter(self._iterable)
#
#     def __len__(self):
#         return len(self._iterable)
#
#     def __eq__(self, other):
#         if isinstance(other, self.__class__):
#             return self._iterable == other._iterable
#         if isinstance(other, set):
#             return set(self._iterable) == other
#         return NotImplemented
#
#     def add(self, item):
#         if item not in self._iterable:
#             self._iterable.append(item)
#
#     def discard(self, item):
#         if item in self._iterable:
#             self._iterable.remove(item)
#
#     def __contains__(self, item):
#         return item in self._iterable
#
#
# print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['green', 'red', 'blue']))
# print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['red', 'blue', 'green']))
# print(OrderedSet(['green', 'red', 'blue']) == {'blue', 'red', 'green'})
# print(OrderedSet(['green', 'red', 'blue']) == ['green', 'red', 'blue'])
# print(OrderedSet(['green', 'red', 'blue']) == 100)


# 6.2 Класс AttrDict

# class AttrDict:
#     def __init__(self, data=()):
#         self._data = dict(data) or dict()
#
#     def __getattr__(self, item):
#         return self._data[item]
#
#     def __getitem__(self, item):
#         return self._data[item]
#
#     def __setitem__(self, key, value):
#         self._data[key] = value
#
#     def __len__(self):
#         return len(self._data)
#
#     def __iter__(self):
#         yield from self._data.keys()


# 6.2 Класс PermaDict

# class PermaDict:
#     def __init__(self, data=()):
#         self._data = dict(data) or dict()
#
#     def __getitem__(self, item):
#         return self._data[item]
#
#     def __setitem__(self, key, value):
#         if key not in self._data:
#             self._data[key] = value
#         else:
#             raise KeyError('Изменение значения по ключу невозможно')
#
#     def __delitem__(self, key):
#         if key in self._data:
#             del self._data[key]
#
#     def __len__(self):
#         return len(self._data)
#
#     def __iter__(self):
#         yield from self._data
#
#     def keys(self):
#         yield from self._data.keys()
#
#     def values(self):
#         yield from self._data.values()
#
#     def items(self):
#         yield from self._data.items()
#
#
# permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})
#
# try:
#     permadict['name'] = 'Arthur'
# except KeyError as e:
#     print(e)


# 6.2 Класс HistoryDict 🌶️

# class HistoryDict:
#     def __init__(self, data=()):
#         self._data = dict(data) or {}
#         self._data_history = {k: [v] for k, v in self._data.items()}
#
#     def __iter__(self):
#         yield from self._data
#
#     def __setitem__(self, key, value):
#         self._data[key] = value
#         self._data_history.setdefault(key, []).append(value)
#
#     def __getitem__(self, item):
#         return self._data[item]
#
#     def __delitem__(self, key):
#         del self._data_history[key]
#
#     def __len__(self):
#         return len(self._data_history)
#
#     def keys(self):
#         return self._data.keys()
#
#     def values(self):
#         return self._data.values()
#
#     def items(self):
#         return self._data.items()
#
#     def history(self, key):
#         return self._data_history.get(key, [])
#
#     def all_history(self):
#         return self._data_history
#
#
# historydict = HistoryDict()
# print('Keys:', *historydict.keys())
# print('Values:', *historydict.values())
# print('Items:', *historydict.items())
# print('History(key=1):', historydict.history(1))
# print('History(key=1):', historydict.history(1))
# print('All history:', historydict.all_history())


# Класс MutableString 🌶️

# class MutableString:
#     def __init__(self, string=''):
#         self._string = string
#
#     def lower(self):
#         self._string = self._string.lower()
#
#     def upper(self):
#         self._string = self._string.upper()
#
#     def __str__(self):
#         return self._string
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}({repr(self._string)})"
#
#     def __len__(self):
#         return len(self._string)
#
#     def __iter__(self):
#         yield from self._string
#
#     def __getitem__(self, item):
#         if isinstance(item, slice):
#             return self.__class__(self._string[item])
#         return self._string[item]
#
#     def __setitem__(self, key, value):
#         txt = list(self._string)
#         txt[key] = value
#         self._string = ''.join(txt)
#
#     def __delitem__(self, key):
#         txt = list(self._string)
#         del txt[key]
#         self._string = ''.join(txt)
#
#     def __add__(self, other):
#         if isinstance(other, self.__class__):
#             return self.__class__(self._string + other._string)
#         return NotImplemented
#
#
# mutablestring = MutableString('beegeek')
#
# print(mutablestring)
# mutablestring[0] = 'B'
# mutablestring[-4] = 'G'
# print(mutablestring)


# Класс Grouper🌶️🌶️

# class Grouper:
#     def __init__(self, iterable, key=None):
#         self._key, self._iterable, self._data = key, iterable, dict()
#         for i in iterable:
#             self.add(i)
#
#     def add(self, item):
#         self._data.setdefault(self._key(item), []).append(item)
#
#     def group_for(self, item):
#         return self._key(item)
#
#     def __getitem__(self, item):
#         return self._data[item]
#
#     def __contains__(self, item):
#         return item in self._data
#
#     def __iter__(self):
#         yield from self._data.items()
#
#     def __len__(self):
#         return len(self._data)
#
#
# grouper = Grouper(['hi'], key=lambda s: s[0])
#
# print(grouper.group_for('hello'))
# print(grouper.group_for('bee'))
# print(grouper['h'])
# print('b' in grouper)


# 6.3 Функция print_file_content()

# def print_file_content(filename):
#     try:
#         with open(filename, encoding='utf-8') as file:
#             print(file.read())
#     except Exception as error:
#         print(f'Файл не найден')


# 6.3 Функция non_closed_files()

# def non_closed_files(files):
#     return [file for file in files if not file.closed]
#
#
# with (
#     open('file1.txt', 'w', encoding='utf-8') as file1,
#     open('file2.txt', 'w', encoding='utf-8') as file2,
#     open('file3.txt', 'w', encoding='utf-8') as file3
# ):
#     file1.write('i am the first file')
#     file2.write('i am the second file')
#     file3.write('i am the third file')
#
# file1 = open('file1.txt', encoding='utf-8')
# file3 = open('file3.txt', encoding='utf-8')
#
# for file in non_closed_files([file1, file2, file3]):
#     print(file.read())


# Функция log_for()

# def log_for(log_file, date_str):
#     with (
#         open(f'log_for_{date_str}.txt', 'w', encoding='utf-8') as file,
#         open(log_file, 'r', encoding='utf-8') as input_file
#     ):
#         [
#             print(line.split(' ', 1)[1].strip("\n"), file=file)
#             for line in input_file.readlines()
#             if line.split(' ', 1)[0] == date_str
#         ]
#
#
# with open('log.txt', 'w', encoding='utf-8') as file:
#     print('2022-01-01 INFO: User logged in', file=file)
#     print('2022-01-01 ERROR: Invalid input data', file=file)
#     print('2022-01-02 INFO: User logged out', file=file)
#     print('2022-01-03 INFO: User registered', file=file)
#
# log_for('log.txt', '2022-01-01')
#
# with open('log_for_2022-01-01.txt', encoding='utf-8') as file:
#     print(file.read())


# 6.4 Функция is_context_manager()

# def is_context_manager(obj):
#     return '__enter__' in dir(obj) and '__exit__' in dir(obj)
#
# class ContextManager:
#     def __enter__(self):
#         return 'beegeek'
#
# print(is_context_manager(ContextManager()))
# print(dir(ContextManager))


# 6.5 Класс SuppressAll

# class SuppressAll:
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         return True


# 6.5 Класс Greeter

# class Greeter():
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print(f'Приветствую, {self.name}!')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(f'До встречи, {self.name}!')
#
#
# with Greeter('Кейв'):
#     print('...')


# 6.5 Класс Closer

# class Closer():
#     def __init__(self, obj):
#         self.obj = obj
#
#     def __enter__(self):
#         return self.obj
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if hasattr(self.obj, '__enter__') and hasattr(self.obj, '__exit__'):
#             self.obj.close()
#         else:
#             print('Незакрываемый объект')
#         return True
#
#
# output = open('output.txt', 'w', encoding='utf-8')
#
# with Closer(output) as file:
#     print(file.closed)
#
# print(file.closed)


# 6.5 Класс ReadableTextFile

# class ReadableTextFile:
#     def __init__(self, filename):
#         self.filename = filename
#
#     def __enter__(self):
#         with open(self.filename, 'r', encoding='utf-8') as file:
#             return [i.strip('\n') for i in file.readlines()]
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         return True
#
#
# with open('glados_quotes.txt', 'w', encoding='utf-8') as file:
#     print('Только посмотрите!', file=file)
#     print('Как величаво она парит в воздухе', file=file)
#     print('Как орел', file=file)
#     print('На воздушном шаре', file=file)
#
# with ReadableTextFile('glados_quotes.txt') as file:
#     for line in file:
#         print(line)


# 6.5 Класс Reloopable

# class Reloopable:
#     def __init__(self, file):
#         self.file = file
#
#     def __enter__(self):
#         return self.file.readlines()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#         return True
#
#
# with open('file.txt', 'w') as file:
#     file.write('Evil is evil\n')
#     file.write('Lesser, greater, middling\n')
#     file.write('Makes no difference\n')
#
# with Reloopable(open('file.txt')) as reloopable:
#     for line in reloopable:
#         print(line.strip())
#     for line in reloopable:
#         print(line.strip())


# 6.5 Класс UpperPrint

# import sys
#
#
# class UpperPrint:
#     def __init__(self):
#         self.new_output = 'new_output.txt'
#
#     def __enter__(self):
#         self.standart_output = sys.stdout
#         sys.stdout = open(self.new_output, 'w', encoding='utf-8')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         sys.stdout = self.standart_output
#         with open(self.new_output, 'r', encoding='utf-8') as out:
#             for i in out.readlines():
#                 print(i.upper().strip('\n'))
#
# print('Если жизнь одаривает вас лимонами — не делайте лимонад')
# print('Заставьте жизнь забрать их обратно!')
#
# with UpperPrint():
#     print('Мне не нужны твои проклятые лимоны!')
#     print('Что мне с ними делать?')
#
# print('Требуйте встречи с менеджером, отвечающим за жизнь!')


# 6.5 Класс Suppress

# class Suppress:
#     def __init__(self, *args):
#         self.errors = args
#         self.exception = None
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type in self.errors:
#             self.exception = exc_val
#             return True
#
#
# with Suppress(TypeError, ValueError) as context:
#     number = int('я число')
#
# print(context.exception)
# print(type(context.exception))


# 6.5 Класс WriteSpy🌶️

# class WriteSpy:
#     def __init__(self, file1, file2, to_close=False):
#         self.file1 = file1
#         self.file2 = file2
#         self.to_close = to_close
#
#     def write(self, txt):
#         if (not self.file1.closed and self.file1.writable()) and (not self.file2.closed and self.file2.writable()):
#             self.file1.write(txt)
#             self.file2.write(txt)
#         else:
#             raise ValueError('Файл закрыт или недоступен для записи')
#
#     def close(self):
#         self.file1.close()
#         self.file2.close()
#
#     def writable(self):
#         if not self.file1.closed and not self.file2.closed:
#             return self.file1.writable() and self.file2.writable()
#         return False
#
#     def closed(self):
#         return self.file1.closed and self.file2.closed
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.to_close:
#             self.file1.close()
#             self.file2.close()
#
#
# f1 = open('file1.txt', mode='w')
# f2 = open('file2.txt', mode='w')
#
# with WriteSpy(f1, f2) as combined:
#     pass
#
# print(combined.closed())


# 6.5 Класс Atomic 🌶️

# from copy import deepcopy, copy
#
#
# class Atomic:
#     def __init__(self, data, deep=False):
#         self.data = data
#         self.deep = deep
#
#     def __enter__(self):
#         if self.deep:
#             self._temp = deepcopy(self.data)
#         else:
#             self._temp = copy(self.data)
#         return self._temp
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is None:
#             if isinstance(self.data, list):
#                 self.data[:] = self._temp
#             if isinstance(self.data, set | dict):
#                 self.data |= self._temp
#         return True
#
#
# numbers = {1, 2, 3, 4, 5}
#
# with Atomic(numbers) as atomic:
#     atomic.add(6)
#     atomic.append(7)  # добавление элемента с помощью несуществующего метода
#
# print(sorted(numbers))
#
# with Atomic(numbers) as atomic:
#     atomic.add(6)
#
# print(sorted(numbers))


# 6.5 Класс AdvancedTimer

# from time import perf_counter
#
#
# class AdvancedTimer:
#     def __init__(self):
#         self.last_run = None
#         self.min, self.max = None, None
#         self.runs = []
#
#     def __enter__(self):
#         self.start = perf_counter()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.last_run = perf_counter() - self.start
#         self.runs.append(self.last_run)
#         self.min = min(self.runs)
#         self.max = max(self.runs)
#         return False
#
#
# from time import sleep
#
# timer = AdvancedTimer()
#
# with timer:
#     sleep(1.5)
#
# with timer:
#     sleep(0.7)
#
# with timer:
#     sleep(1)
#
# print([round(runtime, 1) for runtime in timer.runs])
# print(round(timer.min, 1))
# print(round(timer.max, 1))


# 6.5 Класс HtmlTag 🌶️

# class HtmlTag:
#     space = -1
#
#     def __init__(self, tag, inline=False):
#         self.tag = tag
#         self.inline = inline
#
#     def __enter__(self):
#         self.__class__.space += 1
#         if self.inline is False:
#             print('  ' * self.space + f'<{self.tag}>')
#         else:
#             print('  ' * self.space + f'<{self.tag}>', end='')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.inline is False:
#             print('  ' * self.space + f'</{self.tag}>')
#         self.__class__.space -= 1
#
#     def print(self, text):
#         if self.inline is False:
#             print('    ' * self.space + text)
#         else:
#             print(f"{text}</{self.tag}>")
#
#
# with HtmlTag('body') as _:
#     with HtmlTag('h1') as header:
#         header.print('Поколение Python')
#     with HtmlTag('p') as section:
#         section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')


# 6.5 Класс TreeBuilder 🌶️🌶️

# class TreeBuilder:
#     def __init__(self):
#
#     def __enter__(self):
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#
#     def add(self, item):
#
#     def structure(self):
#
#
# tree = TreeBuilder()
# print(tree.structure())
#
# tree.add('1st')
# print(tree.structure())
#
# with tree:
#     tree.add('2nd')
#     with tree:
#         tree.add('3rd')
#     tree.add('4th')
#     with tree:
#         pass
#
# print(tree.structure())


# 6.6 Контекстный менеджер make_tag

# from contextlib import contextmanager
#
#
# @contextmanager
# def make_tag(tag):
#     print(tag)
#     yield
#     print(tag)
#
#
# with make_tag('---'):
#     print('Поколение Python')


# 6.6 Контекстный менеджер reversed_print

# import sys
# from contextlib import contextmanager
#
#
# @contextmanager
# def reversed_print():
#     standart_stdout = sys.stdout.write
#     sys.stdout.write = lambda x: standart_stdout(x[::-1])
#     yield sys.stdout.write
#     sys.stdout.write = standart_stdout
#
#
# print('Вывод вне блока with')
#
# with reversed_print():
#     print('Вывод внутри блока with')
#
# print('Вывод вне блока with')


# 6.6 Контекстный менеджер safe_write

# from contextlib import contextmanager
#
#
# @contextmanager
# def safe_write(path):
#     try:
#         backup = open('backup.txt', mode='w')
#         yield backup
#         backup.close()
#     except Exception as err:
#         print(f'Во время записи в файл было возбуждено исключение {type(err).__name__}')
#     else:
#         txt = open('backup.txt', mode='r')
#         path_file = open(path, 'w')
#         path_file.write(txt.read())
#         path_file.close(), txt.close()
#
#
# with safe_write('undertale.txt') as file:
#     file.write('Тень от руин нависает над вами, наполняя вас решительностью\n')
#
# with safe_write('undertale.txt') as file:
#     print('Под весёлый шорох листвы вы наполняетесь решительностью', file=file)
#     raise ValueError
#
# with open('undertale.txt') as file:
#     print(file.read())


# 6.6 Контекстный менеджер safe_open

# from contextlib import contextmanager
#
#
# @contextmanager
# def safe_open(filename, mode='r'):
#     try:
#         temp = open(filename, mode=mode)
#         yield (temp, None)
#         temp.close()
#     except Exception as error:
#         yield (None, error)
#
#
# with safe_open('Ellies_jokes_2.txt') as file:
#     file, error = file
#     print(file)
#     print(error)


# 6.8 Класс NonKeyword

# from keyword import kwlist
#
#
# class NonKeyword():
#     def __init__(self, name):
#         self._attr = name
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         if self._attr in instance.__dict__:
#             return instance.__dict__[self._attr]
#         else:
#             raise AttributeError('Атрибут не найден')
#
#     def __set__(self, instance, value):
#         if value not in kwlist:
#             instance.__dict__[self._attr] = value
#         else:
#             raise ValueError('Некорректное значение')
#
#
# class NonKeywordData:
#     obj = NonKeyword('obj')
#
#
# data = [1, 2.3, [4, 5, 6], (7, 8, 9), {10: 11, 12: 13, 14: 15}, True, False, 'Mantrida']
# nonkeyworddata = NonKeywordData()
#
# for item in data:
#     nonkeyworddata.obj = item
#     print(nonkeyworddata.obj)


# 6.8 Класс NonNegativeInteger

# class NonNegativeInteger():
#     def __init__(self, name, default=None):
#         self._attr = name
#         self._default = default
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         if self._attr in instance.__dict__:
#             return instance.__dict__[self._attr]
#         if self._default is None:
#             raise AttributeError('Атрибут не найден')
#         return self._default
#
#     def __set__(self, instance, value):
#         if isinstance(value, int) and value >= 0:
#             instance.__dict__[self._attr] = value
#         else:
#             raise ValueError('Некорректное значение')
#
#
# class Student:
#     score = NonNegativeInteger('score')
#
# student = Student()
# student.score = 90
#
# print(student.score)


# 6.8 Класс LimitedTakes

# class MaxCallsException(Exception):
#     pass
#
#
# class LimitedTakes:
#     def __set_name__(self, owner, name):
#         self._attr = name
#
#     def __init__(self, times):
#         self._times = times
#         self._counter = 0
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         if self._times == self._counter:
#             raise MaxCallsException('Превышено количество доступных обращений')
#         if self._attr in instance.__dict__:
#             self._counter += 1
#             return instance.__dict__[self._attr]
#         else:
#             raise AttributeError('Атрибут не найден')
#
#     def __set__(self, instance, value):
#         instance.__dict__[self._attr] = value
#
#
# class Programmer:
#     name = LimitedTakes(1)
#
#
# programmer = Programmer()
#
# try:
#     print(programmer.name)
# except AttributeError as e:
#     print(e)


# 6.8 Класс TypeChecked

# class TypeChecked:
#     def __set_name__(self, owner, name):
#         self._attr = name
#
#     def __init__(self, *args):
#         self._types = args
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return None
#         if self._attr in instance.__dict__:
#             return instance.__dict__[self._attr]
#         raise AttributeError('Атрибут не найден')
#
#     def __set__(self, instance, value):
#         if type(value) in self._types:
#             instance.__dict__[self._attr] = value
#
#         else:
#             raise TypeError('Некорректное значение')


# class Student:
#     age = TypeChecked(int, float)
#
# student = Student()
#
# student.age = 18
# print(student.age)
#
# student.age = 18.5
# print(student.age)


# 6.8 Класс RandomNumber

# from random import randint
#
#
# class RandomNumber:
#     def __set_name__(self, owner, name):
#         self._attr = name
#
#     def __init__(self, start, end, cache=False):
#         self.start = start
#         self.end = end
#         self.cache = cache
#         self.fst = None
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return None
#         if self.fst:
#             return self.fst
#         if self.cache is False:
#             return randint(self.start, self.end)
#         else:
#             self.fst = randint(self.start, self.end)
#             return self.fst
#
#     def __set__(self, instance, value):
#         raise AttributeError('Изменение невозможно')
#
#
# class MagicPoint:
#     x = RandomNumber(0, 5)
#     y = RandomNumber(0, 5)
#     z = RandomNumber(0, 5)
#
#
# magicpoint = MagicPoint()
#
# try:
#     magicpoint.x = 10
# except AttributeError as e:
#     print(e)


# 6.8 Класс Versioned🌶️

# class Versioned():
#     def __set_name__(self, owner, name):
#         self._attr = name
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         if self._attr in instance.__dict__:
#             return instance.__dict__[self._attr][-1]
#         raise AttributeError('Атрибут не найден')
#
#     def __set__(self, instance, value):
#         instance.__dict__.setdefault(self._attr, []).append(value)
#
#     def get_version(self, instance, ver):
#         return instance.__dict__[self._attr][ver - 1]
#
#     def set_version(self, instance, ver):
#         instance.__dict__[self._attr].append(instance.__dict__[self._attr].pop(ver-1))
#
# class Student:
#     age = Versioned()
#
#
# student = Student()
#
# student.age = 18
# student.age = 19
# student.age = 20
#
# print(student.age)
# Student.age.set_version(student, 1)
# print(student.age)


# ____
# EP_4
# ____


# 7.1 Иерархия классов 🛸

# class Vehicle:
#     pass
#
#
# class WaterVehicle(Vehicle):
#     pass
#
#
# class LandVehicle(Vehicle):
#     pass
#
#
# class Car(LandVehicle):
#     pass
#
#
# class Motocycle(LandVehicle):
#     pass
#
#
# class Bicycle(LandVehicle):
#     pass
#
#
# class AirVehicle(Vehicle):
#     pass
#
#
# class Propeller(AirVehicle):
#     pass
#
#
# class Jet(AirVehicle):
#     pass


# 7.1 Иерархия классов 🔶

# class Shape():
#     pass
#
#
# class Circle(Shape):
#     pass
#
#
# class Polygon(Shape):
#     pass
#
#
# class Triangle(Polygon):
#     pass
#
#
# class IsoscelesTriangle(Triangle):
#     pass
#
#
# class EquilateralTriangle(Triangle):
#     pass
#
#
# class Quadrilateral(Polygon):
#     pass
#
#
# class Parallelogram(Quadrilateral):
#     pass
#
#
# class Rectangle(Parallelogram):
#     pass
#
#
# class Square(Rectangle):
#     pass


# 7.1 Иерархия классов 🐍

# class Animal:
#     def sleep(self):
#         pass
#
#     def eat(self):
#         pass
#
#
# class Fish(Animal):
#     def swim(self):
#         pass
#
#
# class Bird(Animal):
#     def lay_eggs(self):
#         pass
#
#
# class FlyingBird(Bird):
#     def fly(self):
#         pass


# 7.1 Классы User и PremiumUser


# class User:
#     def __init__(self, name):
#         self.name = name
#
#     def skip_ads(self):
#         return False
#
#
# class PremiumUser(User):
#     def skip_ads(self):
#         return True


# 7.1 Классы Validator и NumberValidator

# class Validator:
#     def __init__(self, obj):
#         self.obj = obj
#
#     def is_valid(self):
#         return None
#
#
# class NumberValidator(Validator):
#     def is_valid(self):
#         return isinstance(self.obj, int | float)


# 7.1 Класс Counter и подклассы


# class Counter:
#     def __init__(self, start=0):
#         self.start = start
#         self.value = start
#
#     def inc(self, num=1):
#         self.value += num
#
#     def dec(self, num=1):
#         self.value -= num
#         if self.value < 0:
#             self.value = 0
#
#
# class NonDecCounter(Counter):
#     def dec(self, num=1):
#         pass
#
#
# class LimitedCounter(Counter):
#     def __init__(self, start=0, limit=10):
#         Counter.__init__(self, start)
#         self.limit = limit
#
#     def inc(self, num=1):
#         if self.value + num <= self.limit:
#             self.value += num
#         else:
#             self.value = self.limit
#
#
# counter = LimitedCounter(start=5, limit=30)
#
# print(counter.value)
# counter.inc()
# counter.inc(4)
# print(counter.value)
# counter.dec()
# counter.dec(2)
# print(counter.value)
# counter.inc(24)
# print(counter.value)


