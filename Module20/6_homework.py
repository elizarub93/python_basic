# Задача 1. Песни 2
# Мы продолжаем писать приложение для удобного прослушивания музыки, но теперь наши песни хранятся в виде словаря,
# а не вложенных списков. Каждая песня состоит из названия и продолжительности с точностью до долей минут.
# Напишите программу, которая запрашивает у пользователя количество песен из списка и затем названия этих песен,
# а на экран выводит общее время их звучания.
# Пример:
# Сколько песен выбрать? 3
# Название 1 песни: Halo
# Название 2 песни: Enjoy the Silence
# Название 3 песни: Clean
# Общее время звучания песен: 14.93 минут

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

count_songs = int(input('Сколько песен выбрать? '))
full_time = 0

for i_num in range(count_songs):
    name_song = input(f'Название {i_num + 1} песни: ')
    full_time += violator_songs.get(name_song, 0)
print('Общее время звучания песен: {0:.2f} минут'.format(full_time))

# Задача 2. География
# Антон помимо программирования также увлекается и географией, поэтому он решил связать эти две области и написать
# для своего проекта небольшую программу-навигатор.q
#
# Пользователь вводит количество стран N, а затем N раз вводит страну и города, которые в этой стране находятся, в
# одну строку. Затем пользователь вводит три названия городов. Реализуйте такую программу и для каждого из трёх
# городов укажите, в какой стране он находится. Если такого города нет, то выведите соответствующее сообщение.
#
# Пример:
#
# Кол-во стран: 2
# 1 страна: Россия Москва Петербург Новгород
# 2 страна: Германия Берлин Лейпциг Мюнхен
#
# 1 город: Москва
# Город Москва расположен в стране Россия.
#
# 2 город: Мюнхен
# Город Мюнхен расположен в стране Германия.
#
# 3 город: Рим
# По городу Рим данных нет.

count_countries = int(input('Кол-во стран: '))
countries = dict()

for i_n in range(count_countries):
    country = input(f'{i_n + 1} страна: ').split()
    countries[country[0]] = country[1:]

for i_n in range(3):
    city = input(f'{i_n + 1} город: ')
    found_city = False
    for i_c in countries:
        if city in countries[i_c]:
            print('Город {0} расположен в стране {1}.'.format(city, i_c))
            found_city = True
    if not found_city:
        print('По городу {0} данных нет.'.format(city))

# Задача 3. Криптовалюта
# При работе с API (application programming interface) сайта биржи по криптовалюте вы получили вот такие данные в
# виде словаря:



# Теперь вам предстоит немного обработать эти данные.
#
# Напишите программу, которая выполняет следующий алгоритм действий:
#
# Вывести списки ключей и значений словаря.
# В “ETH” добавить ключ “total_diff” со значением 100.
# Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”.
# Удалить total_out из словарей внутри списка tokens и присвоить сумму этих значений в total_out внутри ETH.
# Внутри "sec_token_info" изменить название ключа “price” на “total_price”.

data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

for i_key in data:
    print(i_key, ':', data[i_key])

data['ETH']['total_diff'] = 100
data['tokens'][0]['fst_token_info']['name'] = 'doge'

total_out = 0

for tokens in data['tokens']:
    total_out += tokens['total_out']
    tokens.pop('total_out')

data['ETH']['total_out'] = total_out

data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')

for i_key in data:
    print(i_key, ':', data[i_key])


# Задача 4. Товары
# В базе данных магазина вся необходимая информация по товарам делится на два словаря: первый отвечает за коды
# товаров, второй — за списки количества разнообразных товаров на складе:

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}


store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Каждая запись второго словаря отображает, сколько и по какой цене закупалось товаров (цена указана за 1 шт.).
#
# Напишите программу, которая рассчитывает, на какую сумму лежит каждого товара на складе, и выводит эту информацию
# на экран.
#
# Результат работы программы.
# Лампа - 27 шт, стоимость 1134 руб
# Стол - 54 шт, стоимость 27860 руб
# Диван - 3 шт, стоимость 3550 руб
# Стул - 105 шт, стоимость 10311 руб

for i_good in goods:
    count_goods = 0
    price_goods = 0
    for good_info in store[goods[i_good]]:
        count_goods += good_info['quantity']
        price_goods += good_info['quantity'] * good_info['price']
    print('{0} - {1} шт, стоимость {2} руб'.format(i_good, count_goods, price_goods))


# Задача 5. Гистограмма частоты 2
# Мы уже писали программу для лингвистов, которая получала на вход текст и считала, сколько раз в строке встречается
# каждый символ. Теперь задача немного поменялась: максимальную частоту выводить не нужно, однако теперь необходимо
# написать функцию, которая будет инвертировать полученный словарь. То есть в качестве ключа будет частота, а в
# качестве значения — список символов с этой частотой. Реализуйте такую программу.


text = input('Введите текст: ')
dict_char = dict()

for char in text:
    if char in dict_char:
        dict_char[char] += 1
    else:
        dict_char[char] = 1

print('Оригинальный словарь частот: ')
for i_c in sorted(dict_char.keys()):
    print(i_c, ':', dict_char[i_c])

reversed_dict = dict()

for i_c in dict_char:
    if dict_char[i_c] in reversed_dict:
        reversed_dict[dict_char[i_c]].append(i_c)
    else:
        reversed_dict[dict_char[i_c]] = []
        reversed_dict[dict_char[i_c]].append(i_c)

print('\nИнвертированный словарь частот: ')
for i_c in sorted(reversed_dict.keys()):
    print(i_c, ':', reversed_dict[i_c])

# Задача 6. Словарь синонимов
# Одна библиотека поручила вам написать программу для оцифровки словарей слов-синонимов. На вход в программу
# подаётся N пар слов. Каждое слово является синонимом к парному ему слову.
#
# Реализуйте код, который составляет словарь слов-синонимов (все слова в словаре различны), затем запрашивает у
# пользователя слово и выводит на экран его синоним. Обеспечьте контроль ввода: если такого слова нет, то выведите
# ошибку и запросите слово ещё раз. При этом проверка не должна зависеть от регистра символов.

count_sinonims = int(input('Введите количество пар слов:  '))
dict_sinonims = dict()

for i_c in range(count_sinonims):
    pair = input(f'{i_c + 1} пара: ').lower().split(' - ')
    dict_sinonims[pair[0]] = pair[1]


while True:
    word = input('Введите слово: ').lower()
    if word in dict_sinonims.keys():
        print('Синоним: {}'.format(dict_sinonims[word]))
        break
    elif word in dict_sinonims.values():
        print('Синоним: {}'.format(list(dict_sinonims.keys())[list(dict_sinonims.values()).index(word)]))
        break
    else:
        print('Такого слова в словаре нет.')

# Задача 7. Пицца
# В базе данных интернет-магазина PizzaTime хранятся данные о том, кто, что и сколько заказывал у них в определённый
# период. Вам нужно структурировать эту информацию, а также понять, сколько всего пицц купил каждый заказчик.
#
# На вход в программу подаётся N заказов. Каждый заказ представляет собой строку вида «Покупатель — название
# пиццы — количество заказанных пицц». Реализуйте код, который выводит список покупателей и их заказов по алфавиту.
# Учитывайте, что один человек может заказать одно и то же несколько раз.

count_order = int(input('Введите кол-во заказов: '))
dict_order = dict()

for i_o in range(count_order):
    order_info = input(f'{i_o + 1} заказ: ').split()
    if order_info[0] in dict_order:
        if order_info[1] in dict_order[order_info[0]]:
            dict_order[order_info[0]][order_info[1]] += int(order_info[2])
        else:
            dict_order[order_info[0]][order_info[1]] = int(order_info[2])
    else:
        dict_order[order_info[0]] = dict()
        dict_order[order_info[0]][order_info[1]] = int(order_info[2])

for i_p in dict_order:
    print(i_p, ':')
    for i_o in dict_order[i_p]:
        print('\t', i_o, ':', dict_order[i_p][i_o])
    print()

# Задача 8. Угадай число
# Артём и Борис играют в игру. Артём загадал натуральное число от 1 до N. Борис пытается угадать это число, для этого
# он называет несколько чисел подряд. Артём говорит Борису «да», если среди названных Борисом чисел есть задуманное.
# В противном случае Артём говорит «нет». После нескольких заданных вопросов Борис сдался и попросил вас помочь ему
# определить, какие числа мог задумать Артём.
#
# Напишите программу, которая имитирует диалог Артёма и Бориса. В начале на вход подаётся число N — это максимальное
# число, которое мог загадать Артём. Затем Борис предполагает, что среди некоторых чисел есть то, которое загадал
# Артём (несколько чисел через пробел), а Артём отвечает. Так продолжается до тех пор, пока Борис не попросит
# помощи (пока не введётся строка «Помогите!») или Борис не угадает число. В конце программы необходимо вывести,
# какие числа мог загадать Артём.

max_number = int(input('Введите максимальное число: '))
all_number = set(list(range(1, max_number + 1)))
print(all_number)

find_number = input('Нужное число есть среди вот этих чисел: ')

while find_number != 'Помогите!':
    find_number = set([int(x) for x in find_number.split()])
    answer = input('Ответ Артёма: ')
    if answer == 'Да':
        all_number = all_number.intersection(find_number)
    elif answer == 'Нет':
        all_number = all_number.difference(find_number)
    find_number = input('Нужное число есть среди вот этих чисел: ')

print(f'Артём мог загадать следующие числа: {''.join(list(all_number))}')

# Задача 9. Родословная
# В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель. Каждому элементу
# дерева сопоставляется целое неотрицательное число, называемое высотой. У родоначальника высота равна 0, у
# любого другого элемента высота на 1 больше, чем у его родителя. Вам нужно написать программу, которая по
# заданному генеалогическому древу определяет высоту всех его элементов.
#
# Программа получает на вход N количество человек в генеалогическом древе. Далее следует N−1 строк, в каждой из
# которых задаётся родитель для каждого элемента дерева, кроме родоначальника. Каждая строка имеет вид
# имя_потомка имя_родителя.
#
# Программа должна вывести список всех элементов древа в лексикографическом порядке (по алфавиту). После вывода
# имени каждого элемента необходимо вывести его высоту.

count_people = int(input('Введите количество человек: '))
dict_tree = dict()

for i_num in range(count_people - 1):
    pair = input(f'{i_num + 1} пара: ').split()
    if pair[1] in dict_tree:
        dict_tree[pair[0]] = dict_tree[pair[1]] + 1
    else:
        dict_tree[pair[1]] = 0
        dict_tree[pair[0]] = dict_tree[pair[1]] + 1

print('“Высота” каждого члена семьи: ')
for i_p in sorted(dict_tree.keys()):
    print(i_p, dict_tree[i_p])

# Задача 10 (по желанию). Снова палиндром
# Пользователь вводит строку. Необходимо написать программу, которая определяет, существует ли у этой строки такая
# перестановка, при которой она станет палиндромом. Выведите соответствующее сообщение.

def is_poly(my_string):
    dict_char = dict()
    for char in my_string:
        dict_char[char] = dict_char.get(char, 0) + 1
    count_odd = 0
    for i_value in dict_char.values():
        if i_value % 2 == 1:
            count_odd += 1
    return count_odd <= 1

my_string = input('Введите строку: ')

if is_poly(my_string):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')