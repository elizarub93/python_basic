# Задача 1. Ревью кода
# Ваня работает middle-разработчиком на Python в IT-компании. Один кандидат на junior-разработчика прислал ему код
# тестового задания. Задание состояло в следующем: есть словарь из трёх студентов. Необходимо:
#
# Вывести на экран список пар «ID студента — возраст».
# Написать функцию, которая принимает в качестве аргумента словарь и возвращает два значения: полный список интересов
# всех студентов и общую длину всех фамилий студентов.
# Далее в основном коде эта функция вызывается, и значения присваиваются отдельным переменным, которые после выводятся
# на экран. (Т.е. нужно распаковать все возвращаемые значения в отдельные переменные.)

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def f(dict):
    lst = []
    cnt = 0
    for _, i_info in dict.items():
        lst.extend(i_info['interests'])
        cnt += len(i_info['surname'])
    return lst, cnt

pairs = []
for i, i_info in students.items():
    print(i, i_info['age'])

my_lst, l = f(students)
print(my_lst, l)

# Задача 2. Универсальная программа 2
# Спустя некоторое время заказчик попросил нас немного изменить скрипт для своей криптографии: теперь индексы
# элементов должны быть простыми числами.
#
# Напишите функцию, которая возвращает список из элементов итерируемого объекта (кортежа, строки, списка, словаря),
# у которых индекс — это простое число. Для проверки на простое число напишите отдельную функцию is_prime.
#
# Дополнительно: сделайте так, чтобы основная функция состояла только из оператора return и при этом также
# возвращала список.

def is_prime(num):
    if num <= 1:
        return False
    for i_n in range(2, num):
        if num % i_n == 0:
            return False
    return True


def change_object(my_object):
    return [item for i, item in enumerate(my_object) if is_prime(i)]


my_object = [100, 200, 300, 'буква', 0, 2, 'а']

if isinstance(my_object, set) or \
        isinstance(my_object, str) or \
        isinstance(my_object, list) or \
        isinstance(my_object, dict):
    out_list = change_object(my_object)
    print('Результат: ', out_list)
else:
    print('Объект не итерируемый')

# Задача 3. Функция
# Напишите функцию, которая принимает на вход кортеж и какой-то случайный элемент (его можно вводить с клавиатуры).
# Функция должна возвращать новый кортеж, начинающийся с первого появления элемента в нём и заканчивающийся вторым
# его появлением включительно.
#
# Если элемента нет вовсе — вернуть пустой кортеж. Если элемент встречается только один раз, то вернуть кортеж,
# который начинается с него и идёт до конца исходного.
import random

def change_tuple(my_tuple, my_number):
    if my_number in my_tuple:
        print(my_tuple.count(my_number))
        if my_tuple.count(my_number) == 1:
            return my_tuple[my_tuple.index(my_number):]
        else:
            start = my_tuple.index(my_number)
            stop = my_tuple[start + 1:].index(my_number) + start + 2
            return my_tuple[start: stop]
    else:
        return tuple()


my_tuple = tuple([random.randint(0, 10) for _ in range(15)])
my_number = random.randint(0, 10)

print('Кортеж: ', my_tuple)
print('Число: ', my_number)
print('Измененный кортеж: ', change_tuple(my_tuple, my_number))

# Задача 4. Игроки
# У вас есть словарь игроков, которые участвовали в трёх видах спорта. В словаре хранятся пары «Ф. И. — очки»:

players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

# Один программист попросил нас для своей базы отправить ему немного другой вариант хранения этой информации.
#
# Напишите программу, которая объединяет ключ словаря со значением в один кортеж, и выведите результат на экран.
# Постарайтесь использовать как можно более эффективное решение.
#
# Результат работы программы:
#
# [('Ivan', 'Volkin', 10, 5, 13), ('Bob', 'Robbin', 7, 5, 14), ('Rob', 'Bobbin', 12, 8, 2)]

new_list = list()

for player, score in players.items():
    list_player = list(player)
    list_player.extend(list(score))
    new_list.append(tuple(list_player))

print(new_list)

# Задача 5. Одна семья
# В одной базе данных хранится информация о членах нескольких разных семей. Хранение реализовано с помощью словаря
# с парами «Ф. И. — возраст».
#
# Напишите программу, которая запрашивает у пользователя фамилию и выводит на экран возраст всех членов одной семьи.
# Учтите, что, например, у двух людей разного пола фамилии различаются окончаниями. Поиск не должен быть регистрозависимым.
#
# Пример:
#
# Введите фамилию: Сидоров
#
#
# Сидоров Никита 35
#
# Сидорова Алина 34
#
# Сидоров Павел 10

data = {
    ('Сидоров', 'Никита') : 35,
    ('Сидорова', 'Алина') : 34,
    ('Сидоров', 'Павел') : 10,
    ('Петров', 'Василий'): 31,
    ('Петрова', 'Алена') : 25
}

surname = input('Введите фамилию: ').lower()

if list(surname)[-1] == 'а':
    surname = surname[:-1]

for i_name, i_age in data.items():
    if surname in i_name[0].lower():
        print(' '.join(list(i_name)), i_age)


# Задача 6. По парам
# Есть список из 10 случайных чисел. Напишите программу, которая делит эти числа на пары кортежей внутри списка,
# и выведите результат на экран.
#
# Дополнительно: решите задачу несколькими способами.
#
# Пример:
#
# Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Оригинальный список: ', my_list)

new_list = [(num, my_list[i+1]) for i, num in enumerate(my_list) if i % 2 == 0]
print('Новый список: ', new_list)


# Задача 7. Функция сортировки
# Напишите функцию, которая сортирует кортеж, состоящий из целых чисел, по возрастанию и возвращает его. Если хотя
# бы один элемент не является целым числом, то функция возвращает исходный кортеж.

def sort_tuple(my_tuple):
    my_list = list(my_tuple)
    for i, i_num in enumerate(my_list):
        if i_num.is_integer():
           for j in range(len(my_list) - i - 1):
               if my_list[j] > my_list[j+1]:
                   my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
        else:
            return my_tuple
    return tuple(my_list)

my_tuple = tuple([random.randint(0, 10) for _ in range(10)])
# my_tuple = (4, 0.1, 0, 2.4)
print('исходный кортеж: {}'.format(my_tuple))
print('отсортированный кортеж: {}'.format(sort_tuple(my_tuple)))