# Задача 1. Сумма чисел
#
# Во входном файле numbers.txt записано N целых чисел, каждое в отдельной строке. Напишите программу, которая выводит
# их сумму в выходной файл answer.txt.

numbers_file = open('numbers.txt', 'r', encoding='utf-8')

sum = 0

print('Содержимое файла numbers.txt:')
for i_line in numbers_file:
    sum += int(i_line)
    print(i_line, end='')

numbers_file.close()

answer_file = open('answer.txt', 'w', encoding='utf-8')
answer_file.write(str(sum))
answer_file.close()

answer_file = open('answer.txt', 'r')

print('Содержимое файла answer.txt')
print(answer_file.read())

answer_file.close()

# Задача 2. Всё в одном
#
# Ваш друг, который тоже проходит курс Python Basic, поехал с ноутбуком в другой город, и там у него случилась беда:
# его диск пришлось отформатировать, а доступ в интернет отсутствует. Остался только телефон с мобильным интернетом.
# Так как со связью (и с памятью) проблемы, друг попросил вас скинуть одним файлом все решения и скрипты, которые
# у вас сейчас есть.
#
# Напишите программу, которая копирует код каждого скрипта в папке проекта python_basic в файл scripts.txt,
# разделяя код строкой из 40 символов *.

import os

def get_file_path(abs_path):
    out_paths = list()
    for i_elem in os.listdir(abs_path):
        path = os.path.join(abs_path, i_elem)
        if os.path.isdir(path):
            out_paths.extend(get_file_path(path))
        elif os.path.isfile(path):
            out_paths.append(path)
    return out_paths

file_path = get_file_path(os.path.abspath(os.path.join('..', 'module22')))
print(file_path)
all_project_file = open('scripts.txt', 'w')

for i_file in file_path:
    file = open(i_file, 'r')
    print(file)
    for i_line in file:
        all_project_file.write(i_line)
    all_project_file.write('*' * 40)
    file.close()
all_project_file.close()




