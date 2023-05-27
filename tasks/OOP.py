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
#         self.friends = 0
#
#     def add_friends(self, n):
#         self.friends += n


# Класс House

# class House:
#     def __init__(self, color, rooms):
#         self.color = color
#         self.rooms = rooms
#
#     def paint(self, new_color):
#         self.color = new_color
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
#         self.counter = counter
#
#     def shoot(self):
#         self.counter += 1
#         if self.counter % 2 == 0:
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
#         self.counter = counter
#
#     def shoot(self):
#         if self.counter % 2 == 0:
#             print('pif')
#         else:
#             print('paf')
#         self.counter += 1
#
#     def shots_count(self):
#         return self.counter
#
#     def shots_reset(self):
#         self.counter = 0
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
#         self.color = color
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
#         if self.can_move(x, y):
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
#         self.password = password
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
#         self.coefficients = a, b, c
#
#     @property
#     def x1(self):
#         check = self.b ** 2 - 4 * self.a * self.c
#         if check < 0:
#             return None
#         return (-self.b - sqrt(check)) / (2 * self.a)
#
#     @property
#     def x2(self):
#         check = self.b ** 2 - 4 * self.a * self.c
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
#         if self.c < 0:
#             self.sign_c = '-'
#         return f'{self.a}x^2 {self.sign_b} {abs(self.b)}x {self.sign_c} {abs(self.c)}'
#
#     @property
#     def coefficients(self):
#         return self.a, self.b, self.c
#
#     @coefficients.setter
#     def coefficients(self, tpl):
#         a, b, c = tpl
#         self.a, self.b, self.c = a, b, c
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
#         self.c = c
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
