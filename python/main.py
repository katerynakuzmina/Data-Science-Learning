# from other import my_name, print_sum



# print_sum(5, 2)

# my_list = {}

# first_key = input("Введите имя первой подруги: ")
# first_num = input("Введите возраст первой подруги:")
# second_key = input("Введите имя второй подруги: ")
# second_num = input("Введите возраст второй подруги:")
# third_key = input("Введите имя третьей подруги: ")
# third_num = input("Введите возраст третьей подруги:")

# my_list[first_key] = int(first_num)
# my_list[second_key] = int(second_num)
# my_list[third_key] = int(third_num)

# print(my_list)

# del my_list[first_key]
# my_list['Katia'] = 20

# my_nams = (2, 12, 10, 2, 2)

# index_one = my_nams.index(2)
# print(index_one)
# index_two = my_nams.index(2, index_one + 1)
# print(index_two)
# index_three = my_nams.index(2, index_two + 1)
# print(index_three)

# my_list = list(my_nams)

# print(my_list)
# my_list.append(7)
# print(my_list)
# my_nams = tuple(my_list)

# print(my_nams)

# my_touple = tuple({'first': 1, 'second': True})
# print(my_touple)

# my_tuple = ('abc', 'cbc', 'a')
# my_tuple_ad = (12, 6, 0)
# my_tuples = my_tuple + my_tuple_ad
# print(my_tuples)

# my_set = {'abc', 'd', 'f', 'y'}
# other_set = my_set.copy()

# my_set.add('l')
# other_set.add('g')

# print(my_set)
# print(other_set)

# print(my_set & other_set)


# my_set = {19, 10, 7, 21}
# my_set.add(5)
# other_set = {19, 6, 7, 11}
# new_set = my_set & other_set
# print(new_set)
# my_list = list (new_set)
# print(my_list)

# my_range = range (5)
# # print(my_range)
# # print(type(my_range))
# # print(my_range[-1])
# # for n in my_range:
# #     print(n)

# print(set(range(12, 25, 5)))

# my_range = range(5, 30, 5)
# my_list = []
# for n in my_range:
#     my_list.append(n)
# print(my_list)

# my_str = "My string"
# print(my_str[2])

# fruits = ['apple', 'banana', 'lime', 'orange']

# quantities = [10, 70, 50, 20]

# availability = [True, False, False, True]

# fruit_qtys_zip = zip(fruits, quantities, availability)

# print(fruit_qtys_zip)

# fruit_qtys_list = list(fruit_qtys_zip)

# print(fruit_qtys_list)

# goods = ['milk', 'bread', 'tea']
# prices = [10, 24, 17]
# goods_qtys_zip = zip(goods, prices)
# print(goods_qtys_zip)
# # goods_qtys_list = list(goods_qtys_zip)
# goods_qtys_dict = dict(goods_qtys_zip)
# # print(goods_qtys_list)
# print(goods_qtys_dict)

# my_list = [1, 2, 3]
# other_list = my_list

# print(id(my_list))
# print(id(other_list))

# # other_list.append(5)
# # print(my_list)
# # print(other_list)

# from copy import deepcopy

# info = {
#     'name': 'Katia',
#     'is_instructor': True,
#     'reviews': []
# }

# info_deepcopy = deepcopy(info)

# info_deepcopy['reviews'].append('Great course?')

# print(info)

# print(info_deepcopy)


# def my_fn (a):
#     print(id(a))
#     a = a + 1
#     return a

# num_one = 10

# res = my_fn(num_one)
# print(res)
# print(num_one)
# print(id(num_one))

# def increase_age(persone):
#     print(id(persone))
#     persone['age'] += 1
#     return persone

# persone_one = {
#     'name': 'Bob',
#     'age': 21
# }

# print(id(persone_one))

# increase_age(persone_one)

# print(persone_one['age'])

# def merge_lists_to_dict (a, b):
#     return dict(zip (a, b))

# print(merge_lists_to_dict(b=[1, 2, 3], a=['a', 'b', 'c']))
# print(merge_lists_to_dict(['ab', 'd', 'ef'], b=[2, 7, 1]))


# def sum_nums (*args):
#     print(args)
#     print(type(args))

#     print(args[0])
#     return sum (args)

# print(sum_nums(2, 3, 7))


# def get_posts_info (**person):
#     print(person)
#     print(type(person))
#     info = (
#         f"{person['name']} wrote "
#         f"{person['posts_qty']} posts"
#     )
#     return info

# info = get_posts_info(name='Katia', posts_qty='20')
# print(info)

# def update_car_info (**car):
#     car['is_avaliable']= True
#     return car

# print(update_car_info(brand='Renault', price=125))

# from datetime import date


# def get_weekday():
#     return date.today().strftime('%A')


# def create_new_post (post, weekday=get_weekday()):
#     post_copy = post.copy()
#     post_copy['created_on_weekday'] = weekday
#     return post_copy


# initial_post = {
#     'id': 243,
#     'author': 'Katia',
# }

# post_with_weekday = create_new_post(initial_post)
# print(post_with_weekday)

# def print_number_info (num):
#     if (num % 2) == 0:
#         print ("Entered number is even")
#     else:
#         print("Entered number is odd")

# def process_number (num, callback_fn):
#     callback_fn (num)

# entered_num = int (input("Enter any number: "))

# process_number(entered_num, print_number_info)

# def mult_by_factor (value, mult=1):
#     """Multiplies number by multiplicator"""
#     return value * mult

# # mult_by_factor(5)

# def print_number_info (num):
#     """
#     Prints num information

#     Args:
#         num (int): Integer Number

#     Returns:
#         int: Same Number
#     """
#     if (num % 2) == 0:
#         print("Num is even")
# #     else:
# #         print("Num is odd")

# #     return num

# # print_number_info()


# def my_fn (a, b):
#     print(a)
#     print(b)

# my_fn('abc', 'xyz')

# print(a)

# my_sict = (12, 10, 5)

# my_dict = (12, 10, 5)
# print(my_dict == my_sict)
# print(my_sict is my_dict)


# first_set = {'abc', 'df', 'zz'}
# second_set = {'abc', 'df', 'zz'}

# print(first_set == second_set)
# print(first_set is second_set)
# print('abc' in first_set)


# print(bool(['abc', 12]))
# # print(bool({}))
# # print(bool(""))
# # print(bool(set()))
# # print(bool(range(0)))
# # print(bool(0))
# # print(bool(0.0))
# # print(bool(0j))
# # print(bool(None))

# print(not not (['abc', 12]))
# print(not not ([]))
# print(not not ({}))
# print(not not (""))
# print(not not (set()))
# print(not not (range(0)))
# print(not not (0))
# print(not not (0.0))
# print(not not (0j))
# print(not not (None))


# dict_one = {
#     'a': 2,
#     'b': 5
# }

# dict_two = {
#     'a': 2,
#     'b': 5
# }

# dict_one == dict_two and print("Dictionaries are equal")

# button = {
#     'width': 125,
#     'text': 'Buy',
# }

# button_two = {
#     'color': 'red'
# # }

# button_three = button_two | button

# print(button)
# print(button_two)
# print(button_three)
# red_button = button.copy()
# red_button['color'] = 'red'
# # red_button = {
# #     **button,
# #     'color': 'red'
# # }

# print(button)
# print(red_button)

# name = 'katia'
# hobby = 'running'
# time = 8

# # info = name + ' likes ' + hobby + ' at ' + str(time) + 'o\'clock'
# info = f"{name} likes {hobby} at {time} o\'clock"

# print(info.upper())

# mult = lambda a, b: a * b

# print(mult(10, 5))

# def greeting (greet):
#     return lambda name: f"{greet}, {name}"

# morning_greeting = greeting("Good morning")
# print(morning_greeting('Katia'))
# evening_greeting = greeting("Good evening")
# print(evening_greeting('Katia'))


# def image_info (a):
#     if ('image_id' not in a)or ('image_title' not in a):
#         raise TypeError ('Some of two arguments doesn\'t exist')
#     print (f"Image {a['image_title']} has id {a['image_id']}")

# try:
#     image_info({
#         'image_title': 'Foto',
#         'image_idss': '01'
#     })
# except TypeError as e:
#     print(e)

# print('Continue...')

# my_list = [1, 2, 3]

# first, second, third = my_list

# print(first)
# print(second)
# print(third)

# user_profile = ['Katia', 23]

# def user_info (name, comments_qty = 0):
#     if not comments_qty:
#         return f"{name} has no comments" 

#     return F"{name} has {comments_qty} comments"

# print(user_info(*user_profile))


# my_list = [
#     {
#         'brand': 'Toyota',
#         'price': 100,
#     },
#     {
#         'brand': 'Mercedes',
#         'price': 200,
#     },
#     {
#         'brand': 'Citroen',
#         'price': 250
#     }
# ]

# toyota, mercedes, citroen = my_list

# def auto_info (brand, price):
#     return f"{brand} costs {price}"

# print(auto_info(**toyota))
# print(auto_info(**mercedes))
# print(auto_info(**citroen))

# print(toyota)


# if 10 > 2:
#     print(True)

# num_one = 10
# num_two = 5.7

# if (num_one > 0 and
#     num_two > 0 and
#     isinstance(num_one, int) and
#     isinstance(num_two, int)):
#     print("Both numbers are ints and positives")

# my_phone = {
#     'price': 200,
#     'brand': 'Motorola'
# }

# if my_phone.get('brand'):
#     print("Phone's brand is", my_phone['brand'])
# else:
#     print("There is no phone brand")

# def route_info (data):
#     if data.get('distance'):
#         return(f"Distance to your destination is {data['distance']}")

#     if (data.get('speed') and data.get('time')):
#         your_dest = data['speed'] * data['time']
#         return(f"Distance to your destination is {your_dest}")
#     return f"No distance info is available"

# print(route_info({'distance': 200}))
# print(route_info({'speed': 100, 'time': 20}))
# print(route_info({'speed': 100}))


# my_img = ('1920', '1080')

# print(f"{my_img[0]}x{my_img[1]}" 
#     if (len(my_img) == 2 and type(my_img[0]) == str and type(my_img[1]) == str)
#     else "incorrect format")
# if (len(my_img) == 2 and type(my_img[0]) == str and type(my_img[1]) == str):
#     print(f"{my_img[0]}x{my_img[1]}")
# else:
#     print("incorrect format")


# my_str = "Zycie jest piekne"

# print("Long string" if len(my_str) >= 39 else "Short string")
# # my_dict = {'id': 1}

# # for key in my_dict:
# #     print(type(key))
# #     print(key)
# #     print(my_dict[key])


# my_dict = {
#     'key_one': 10,
#     'key_two': [],
#     'key-three': 100
# }

# def dict_to_list (some_dist):
#     some_list = []
#     for key, value in some_dist.items():
#         if type(value) == int:
#             value *=2
#         some_list.append((key, value))
#     return some_list

# print(dict_to_list(my_dict))


# def filter_list (list_to_filter, value_type):
#     new_list = []
#     for value in list_to_filter:
#         if type(value) == value_type:
#             new_list.append(value)
#     return new_list

# print(filter_list([2.3, 12, 'abc', True, 90, 4.6, 5], int))

# def filter_list (list_to_filter, value_type):
#     # def chech_elem_type(elem):
#     #     return type(elem) is value_type
#     return list(filter(lambda elem: type(elem) is value_type, list_to_filter))

# res = filter_list([2.3, 12, 'abc', True, 90, 4.6, 5], int)
# print(res)

# import random

# random_num = random.randint(1, 5)
# while True:
#     num = int(input("Guess the number from 1 to 5: "))
#     if num != random_num:
#         print("Try again...")
#         continue
#     print("Congratulations!", random_num)
#     break
# 
# while True:
#     try:
#         num_one = int (input("Put your first number: "))
#         num_two = int (input("Put your second number: "))
#     except ValueError as e:
#         print(e)
#         print("You must enter numbers")
#         continue
#     if num_two == 0:
#         print("The second number can not be 0")
#     else:
#         print(int(num_one / num_two))
#     final_answer = input("Are you goin to continue? yes/no: ")
#     if final_answer == 'yes':
#         continue
#     break

# my_dict = {
#     'a': 'mouse',
#     'b': 'cat'
# }

# new_dict = {k: v.upper() for k, v in my_dict.items()}
# print(new_dict)

# my_list = ['abc', 'df', 'ancd', 'blabla']
# new_list = [num for num in my_list if len(num) > 3]
# print(new_list)


# from sys import getsizeof 

# squares_gen = (num * num for num in range(10_000_000))

# print(getsizeof(squares_gen))

# print(type(squares_gen))

# squares_list = [num * num for num in range(10_000_000)]

# print(getsizeof(squares_list))

# print(type(squares_list))


# class Car:
#     def move(self):
#         print("Car is moving")
    
#     def stop(self):
#         print("Car stopped")

# my_car = Car()

# print(my_car)
# print(type(my_car))
# print(isinstance(my_car, Car))
# print(isinstance(my_car, object))


# my_car.move()
# my_car.stop()

# class Comment:
#     def __init__(self, text):
#         self.text = text
#         self.votes_qty = 0

#     def upvote(self, qty):
#         self.votes_qty += qty

# my_comment = Comment("My comment")

# print(my_comment.text)
# print(my_comment.votes_qty)

# my_comment.upvote(5)

# print(my_comment.votes_qty)

# class Image:
#     def __init__(self, title):
#         self.title = title
#         self.resolution = '1920x1080'
#         self.extension = 'JPG'

#     @staticmethod
#     def merge_img (first, second):
#         return f"{first} {second}"

#     def resize(self, value):
#         self.resolution = value

#     def __str__(self):
#         return f"{self.title}.{self.extension}"

    



# img_one = Image("First image")
# print(img_one.resolution)

# merged_images = img_one.merge_img('Pic 1', 'Pic 2')
# print(merged_images)

# img_one.resize('1480x960')
# print(img_one.resolution)

# print(img_one)
# print(isinstance(img_one, Image))

# img_two = Image("Second Image")
# print(img_two.title)
# print(img_two.resolution)
# print(img_two.extension)
# img_two.resize('960x234')
# print(img_two.resolution)
# # print(img_one.resolution)

# class Comment:
#     def __init__(self, text):
#         self.text = text
#         self.votes_qty = 0

#     def upvote(self):
#         self.votes_qty += 1

#     def __add__(self, other):
#         return (f"{self.text} {other.text}", 
#                 self.votes_qty + other.votes_qty)
    
#     def __eq__(self, other):
#         return (self.text == other.text) and (
#                 self.votes_qty == other.votes_qty)
    
# comment_one = Comment ("First comment")
# comment_one.upvote()
# comment_two = Comment ("First comment")
# comment_two.upvote()
# print(comment_one + comment_two)
# print(comment_one == comment_two)

# class ExtendedList(list):
#     def print_list_info(self):
#         print(f"List has {len(self)} elements")

# custom_list = ExtendedList([3, 5, 2])

# print(ExtendedList.__dict__)

# def decorator_function(original_fn):
#     #такие параметры делают функцию wrapper универсальной
#     def wrapper_function(*args, **kwargs): 
#         #Some actions before execution of the original_fn
#         print("Executed before function")
#         result = original_fn(*args, **kwargs)

#          #Some actions after execution of the original_fn
#         print("Executed after function")

#         return result

#     return wrapper_function

# @decorator_function
# def my_function(a, b):
#     print("This is my function!")
#     return (a, b)

# result = my_function(100, 50)
# print(result)


# def log_function_call(fn):
#     def wrapper(*args, **kwargs):
#         print(f"Function name: {fn.__name__}")
#         print(f"Function arguments: {args}, {kwargs}")
#         result = fn(*args, **kwargs)
#         print(f"Function result: {result}")
#         return result

#     return wrapper

# @log_function_call
# def mult(a, b):
#     return a * b

# print(mult(a=5, b=2))

# print('')

# @log_function_call
# def sum(a, b):
#     return a + b

# print(sum(40.3, 20.7))


# def validate_args(fn):
#     def wrapper(*args, **kwargs):
#         for arg in [*args, *kwargs.values()]:
#             if not isinstance(arg, int) and not isinstance(arg, float):
#                 raise ValueError(f"Value type of {arg} is {type(arg)}",
#                                  "All arguments must be int or float!")
#         result = fn(*args, **kwargs)
#         return result

#     return wrapper
# @validate_args
# def sum_nums(a, b):
#     return a + b

# try:
#     print(sum_nums(7, 2))
#     print(sum_nums(10.5, 2.3))
#     print(sum_nums(a='10.5', b=2.3))
# except ValueError as e:
#     print(e)

# def is_user_authenticated():
#     return True

# def check_user_ayth(fn):
#     def wrapper(*args, **kwargs):
#         if is_user_authenticated():
#             print("User is authenticated")
#             return fn(*args, **kwargs)
#         else:            
#             raise Exception("User is NOT authenticated")

#     return wrapper

# @check_user_ayth
# def do_sensative_job():
#     print("Result of some sensative tasks")
# try:
#     do_sensative_job()
# except Exception as e:
#     print(e)

# import json

# json_str = '{"id":235, "brand": "Nike", "qty": 84, "status": {"isForSale":true}}'

# sneakers = json.loads(json_str)

# print(type(sneakers))

# print(sneakers['brand'])
# print(sneakers['qty'])
# print(sneakers['status']['isForSale'])
# print(sneakers)

# json_from_dict = json.dumps(sneakers, indent=2)
# print(json_from_dict)

# import json

# my_disct = {
#     'brand': [1, 2, 3],
#     'price': (1, 2, 3),
#     'status': True,
#     'num': 10.2
# }

# json_data = json.dumps(my_disct)
# print(json_data)
# print(type(json_data))

# from pathlib import Path

# cwd = Path('C:/').joinpath('users').joinpath('tako').joinpath('Desktop')
# print(cwd)


# with open('test.txt', 'w') as test_file:
#     test_file.write("First String\n")
#     test_file.write("Second String\n")
#     test_file.write("Third String\n")

# with open('test.txt') as test_file:
#     while True:
#         line = test_file.readline()
#         print(line)
#         if not line:
#             break

# from pathlib import Path

# file = open('test.txt', 'w')
# file.close()

# my_file = Path('test.txt')

# if my_file.exists():
#     my_file.unlink() 


# from pathlib import Path

# cwd = Path('files')

# cwd.mkdir(exist_ok=True)

# first_file = Path(cwd / 'first.txt')
# second_file = Path(cwd / 'second.txt')

# with open (first_file, 'w') as f:
#     f.write("first line \n")
#     f.write("second line \n")

# with open (second_file, 'w') as f:
#     lines = [
#        "First line in the second file", 
#        "Second line in the second file", 
#        "Last line in the second file", 
#     ]
#     for line in lines:
#         f.write(line + '\n')

# with open (first_file) as f:
#     print(f.read())

# with open (second_file) as f:
#     for line in f.readlines():
#         print(line)

# first_file.unlink()
# second_file.unlink()
# cwd.rmdir()

# from zipfile import ZipFile
# from pathlib import Path

# with ZipFile('my-files.zip') as my_zip_file:
#     my_zip_file.extractall('my-files-unzipped')
# with ZipFile('my-files.zip', mode='w') as my_zip_file:
#     # print(my_zip_file)
#     for file in Path('my-files').iterdir():
#         print(file)
#         my_zip_file.write(file)

# import csv
# with open ('test.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(['user_is', 'user_name', 'comments'])
#     writer.writerow([5242, 'katya', 643])
#     writer.writerow([467, 'zenya', 71])
#     writer.writerow([524, 'roma', 987])
# with open('test.csv') as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(line)
#         print(reader.line_num)

# from datetime import datetime, timedelta

# my_time = datetime(2100, 4, 12, 18, 10, 45)

# print(timedelta)
# print(my_time + timedelta(days=100, minutes=20))

# print(my_time)

# print(my_time.strftime('%d/%m/%Y'))

# date_str = '12/04/2100'
# converted_date = datetime.strptime(date_str, '%d/%m/%Y')
# print(converted_date)

# import time

# print(time.time())
# print(time.ctime(25876568726))


import random

# print(random.random())
# print(random.randint(1, 10))
# print(random.choice('abcd'))
# print(random.choices([1, 4, 7, 2, 0], k=2))


# my_list = [1, 4, 7, 2, 0]
# print(random.shuffle(my_list))
# print(my_list)
# print(random.shuffle(my_list))
# print(my_list)
# print(random.shuffle(my_list))
# print(my_list)

# print(''.join(random.choices('0123456789', k=8)))

# import secrets
# import string

# all_chars = string.ascii_letters + string.digits +string.punctuation
# print(''.join(secrets.choice(all_chars) for i in range(8)))


# import math

# print(math.pi)
# print(math.e)
# print(math.sqrt(25))
# print(math.log(100))
# print(math.factorial(10))


# def calc_factorial(num):
#     if type(num) is not int:
#         raise TypeError("Number must be integer")
#     if num <= 0:
#         raise ValueError("Number must be positive")
#     if num == 1:
#         return 1
#     return calc_factorial(num - 1) * num
# # calc_factorial('abc')
# calc_factorial(10)


# import re

# def check_email(email):
#     email_regexp = r"[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
#     email_check_pattern = re.compile(email_regexp)
#     validation_result = 'valid' if email_check_pattern.fullmatch(email) else 'not valid'
#     return (email, validation_result)

# print(check_email("bs@gmail.com"))
# print(check_email("bs@gmailcom"))
# print(check_email("bsgmail.com"))
# print(check_email("bs@"))

# import re

# def check_password(password):
# #проверка что в строке минимум 8 символов, 
# #при этом пробелы, переносы и Tab не считается
#     length_pattern  = re.compile(r"\S{8,}" )

# #проверка букв в нижнем регистре
#     lowercase_pattern = re.compile(r"^.*[a-z]+.*$")

# #проверка букв в верхнем регистре
#     uppercase_pattern = re.compile(r"^.*[A-Z]+.*$")

# #проверка наличия хотя бы одной цифры
#     number_pattern = re.compile(r"^.*[0-9]+.*$")
    
# #проверка наличия хотя бы одного специального символа
#     special_symbol_pattern = re.compile(r"^.*[@%#!&*^]+.*$")

# #проверка на наличие прробеловб переносов строки
#     no_whitespaces_pattern = re.compile(r"^\S*$")

#     if not re.fullmatch(no_whitespaces_pattern, password):
#         return (False, "No whitespaces allowed in the password")

#     if not re.fullmatch(length_pattern, password):
#         return(False, "Password must have at least 8 symbols")

#     if not re.fullmatch(lowercase_pattern, password):
#         return (False, "Password must have at least one lowercase symbol")
    
#     if not re.fullmatch(uppercase_pattern, password):
#         return (False, "Password must have at least one uppercase symbol")
    
#     if not re.fullmatch(number_pattern, password):
#         return (False, "Password must have at least one number")
    
#     if not re.fullmatch(special_symbol_pattern, password):
#         return (False, "Password must have at least one special symbol")

#     return (True, "Password is valid!")

# while True:
#     password = input("PLEASE ENTER PASSWORD: ")
#     password_check_res = check_password(password)
#     if password_check_res[0]:
#         print(password_check_res[1])
#         break
#     print(password_check_res[1])
    

# print(check_password("123bnbn UIUH !@!"))
# print(check_password("123"))
# print(check_password("12345678"))
# print(check_password("1234567a"))
# print(check_password("123456aA"))
# print(check_password("Katyaaaa"))
# print(check_password("90Katty17"))
# print(check_password("90Kat@ty17"))


# from email.message import EmailMessage
# import smtplib
# from string import Template
# from pathlib import Path


# my_email = EmailMessage()

# html_template = Template(Path("templates/index.html").read_text())
# html_content = html_template.substitute({'name': 'Katya', 'date': 'tomorrow'})

# my_email['from'] = 'Katya <kk@gmail.com>'
# my_email['to'] = 'friend@gmail.com'
# my_email['subject'] = "Email with image"
# my_email.set_content(html_content, 'html')

# with open('images/email.jpg', 'rb') as img:
#     image_data = img.read()
#     my_email.add_attachment(image_data, maintype='image', subtype='jpg')

# with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
#     smtp_server.ehlo()
#     # smtp_server.starttls()
#     # smtp_server.login('username', 'password')
#     smtp_server.send_message(my_email)
#     print("Email was send!")


# import sqlite3
 
# DB_NAME = "sglite3_db.db"

# with sqlite3.connect(DB_NAME) as sqlite3_conn:
#     sql_request = "SELECT * FROM courses WHERE reviews_qty>=50"
#     sql_cursor = sqlite3_conn.execute(sql_request)
#     # for record in sql_cursor:
#     #     print(record)
#     records = sql_cursor.fetchall()
#     print(records)

#Add records to the table courses

# courses = [
#     (331, "Java Script", 400, 130),
#     (461, "C++ course", 100, 35),
#     (722, "JAVA course", 160, 19)    
# ]

# with sqlite3.connect(DB_NAME) as sqlite3_conn:
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     for course in courses:
#         sqlite3_conn.execute(sql_request, course)    
#     sqlite3_conn.commit()


# with sqlite3.connect(DB_NAME) as sqlite3_conn:
#     print(sqlite3_conn)
#     print(sqlite3.version)

#Create new table
# with sqlite3.connect(DB_NAME) as sqlite3_conn:
#     sql_request = """CREATE TABLE IF NOT EXISTS courses (
#     id integer PRIMARY KEY,
#     title text NOT NULL,
#     students_qty integer,
#     reviews_qty 
#     );"""
#     sqlite3_conn.execute(sql_request)


# from array import array

# my_int_array = array('i', [5, 10, 2, 90, 12, 5])

# with open ('my_array.bin', 'wb') as my_file:
#     my_int_array.tofile(my_file)

# imported_array = array('i')
# with open ('my_array.bin', 'rb') as my_file:
#     imported_array.fromfile(my_file, 3)
    
# print(imported_array)

# imported_array.reverse()
# print(imported_array)

# import sys

# print(sys.argv)

import requests

my_request = requests.get('https://www.python.org')

print(my_request)
print(my_request.text)
print(my_request.status_code)