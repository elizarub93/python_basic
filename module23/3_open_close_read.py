# Задача 1. Результаты
#
# Одному программисту дали задачу для обработки неких результатов тестирования двух групп людей. Файл первой группы
# (group_1.txt) находится в папке task, файл второй группы (group_2.txt) — в папке Additional_info.
# На экран нужно было вывести сумму очков первой группы, затем разность очков опять же первой группы и
# напоследок — произведение очков уже второй группы.
#
# Программист оказался не очень опытным, писал код наобум и даже не стал его проверять. И оказалось, этот
# код просто не работает. Вот что он написал:

# file = open('E:\task\group_1.txt', 'read')
# summa = 0
#
# for i_line in file:
#     info = i_line.split()
#     summa += info[2]
#
# file = open('E:\task\group_1.txt', 'read')
# diff = 0
#
# for i_line in file:
#     info = i_line.split()
#     diff -= info[2]
#
# file_2 = open('E:\task\group_2.txt', 'read')
# compose = 0
#
# for i_line in file:
#     info = i_line.split()
#     compose *= info[2]
#
# print(summa)
# print(diff)
# print(compose)

# Исправьте код для решения поставленной задачи. Для проверки результата создайте необходимые папки
# (task, Additional_info, Dont touch me) на своём диске в соответствии с картинкой и также добавьте файлы
# group_1.txt и group_2.txt.

import os

file = open(os.path.join('task', 'group_1.txt'), 'r', encoding='utf-8')
summa = 0
diff = 0

for i_line in file:
    info = i_line.split()
    summa += int(info[-1])
    diff -= int(info[-1])

file.close()

file_2 = open(os.path.join('task', 'Additional_info', 'group_2.txt'), 'r', encoding='utf-8')
compose = 1

for i_line in file_2:
    info = i_line.split()
    compose *= int(info[-1])

file_2.close()

print(summa)
print(diff)
print(compose)

# Задача 2. Поиск файла 2
#
# Как мы помним, скрипты — это просто куча строк текста, хоть они и понятны только программисту. Таким образом,
# с ними можно работать точно так же, как и с обычными текстовыми файлами.
#
# Используя функцию поиска файла из предыдущего урока, реализуйте программу, которая находит внутри указанного
# пути все файлы с искомым названием и выводит на экран текст одного из них (выбор можно сгенерировать случайно).
#
# Подсказка: можно использовать, например, список для сохранения найденного пути.
import random

def find_file(abs_path, file_name):
    out_paths = list()
    for i_elem in os.listdir(abs_path):
        path = os.path.join(abs_path, i_elem)
        if file_name == i_elem:
            out_paths.append(path)
        if os.path.isdir(path):
            out_paths.extend(find_file(path, file_name))
    return out_paths

abs_path = input('Ищем в: ')
file_name = input('Имя файла: ')
out_paths = find_file(abs_path, file_name)

file = open(out_paths[random.randint(0, len(out_paths) - 1)], 'r', encoding='utf-8')

for i_line in file:
    print(i_line, end='')

file.close()
