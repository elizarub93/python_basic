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