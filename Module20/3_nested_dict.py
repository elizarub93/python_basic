# Задача 1. Член семьи
#
# Дана структура, которая содержит описание одного из членов семьи (имя, фамилия, хобби, сколько лет и дети):
#
# family_member = {
#     "name": "Jane",
#     "surname": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "name": "Alice",
#             "age": 6
#         },
#         {
#             "name": "Bob",
#             "age": 8
#         }
#     ]
# }
#
#
#
# Напишите программу, которая реализует такую структуру: имя, фамилия, хобби, количество лет и дети. Затем с помощью
# метода get и установки значения по умолчанию проверьте, есть ли ребёнок с именем Bob. Затем так же проверьте ребёнка
# с именем Rob. Если такого ребёнка нет, то получите значение Noname.

family_member = dict()
family_member['name'] = 'Jane'
family_member['surname'] = 'Doe'
family_member['hobbies'] = ['running', 'sky diving', 'singing']
family_member['age'] = 35
family_member['children'] = [
    {
        'name': 'Alice',
        'age': 6
    },
    {
        'name': 'Bob',
        'age': 8
    }
]
print(family_member)
for child in family_member['children']:
    if child.get('name') == 'Bob':
        print('Ребенок с именем Bob есть')


# Задача 2. Игроки
#
# Есть готовый словарь игроков, у каждого игрока есть имя, команда, в которой он играет, а также его текущий статус,
# в котором указано, отдыхает он, тренируется или путешествует:

# players_dict = {
#     1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
#     2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
#     3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
#     4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
#     5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
#     6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
#     7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
#     8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
# }
#
# Напишите программу, которая выводит на экран вот такие данные в разных строчках:
# Все члены команды из команды А, которые отдыхают.
# Все члены команды из группы B, которые тренируются.
# Все члены команды из команды C, которые путешествуют.

players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

for player in players_dict:
    print(player, ':', players_dict[player])

print('Все члены команды из команды А, которые отдыхают: {}'.format(
    ', '.join([player['name'] for player in players_dict.values()
               if player['team'] == 'A' and  player['status'] == 'Rest']
)))

print('Все члены команды из группы B, которые тренируются: {}'.format(
    ', '.join([player['name'] for player in players_dict.values()
               if player['team'] == 'B' and  player['status'] == 'Training']
)))

print('Все члены команды из команды C, которые путешествуют: {}'.format(
    ', '.join([player['name'] for player in players_dict.values()
               if player['team'] == 'C' and  player['status'] == 'Travel']
)))