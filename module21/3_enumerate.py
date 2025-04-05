# Задача 1. Саботаж!
#
# Какой-то нехороший человек решил подпортить жизнь frontend-разработчикам и добавил в код сайта символ ~ (тильда).
# Но программисты быстро решили эту проблему, пройдясь по всему коду маленькой программой.
#
# Пользователь вводит строку. Напишите программу, которая проходит по строке и выводит в консоль индексы символа ~.
# Для решения этой задачи (и остальных тоже) используйте функцию enumerate.

my_text = input('Строка: ')

print('\nОтвет: ', end='')
for i, char in enumerate(my_text):
    if char == '~':
        print(i, end=' ')


# Задача 2. Словари из списков
#
# Создайте два списка, в каждом из которых лежит 10 случайных букв алфавита (могут повторяться). Затем для каждого
# списка создайте словарь из пар «индекс — значение» и выведите оба словаря на экран.
#
# Подсказка: random

import random

cyrillic_lower_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
list_one = [random.choice(cyrillic_lower_letters) for _ in range(10)]
list_two = [random.choice(cyrillic_lower_letters) for _ in range(10)]
print('Первый список: ', list_one)
print('Второй список: ', list_two)

dict_one = dict()
dict_two = dict()

for i, char in enumerate(list_one):
    dict_one[i] = char

for i, char in enumerate(list_two):
    dict_two[i] = char

print('Первый словарь: ', dict_one)
print('Второй словарь: ', dict_two)

# Задача 3. Универсальная программа
#
# Один заказчик попросил нас написать небольшой скрипт для своих криптографических нужд. При этом он заранее
# предупредил, что скрипт должен уметь работать с любым итерируемым типом данных.
#
# Напишите функцию, которая возвращает список из элементов итерируемого объекта (кортежа, строки, списка, словаря),
# у которых индекс чётный.

my_object = [100, 200, 300, 'буква', 0, 2, 'а']

out_list = list()

if isinstance(my_object, set) or \
        isinstance(my_object, str) or \
        isinstance(my_object, list) or \
        isinstance(my_object, dict):
    for i, item in enumerate(my_object):
        if i % 2 == 0:
            out_list.append(item)
    print('Результат: ', out_list)
else:
    print('Объект не итерируемый')