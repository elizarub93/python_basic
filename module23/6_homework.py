# Задача 1. Сумма чисел — 2
# Что нужно сделать
# Во входном файле numbers.txt записано N целых чисел, которые могут быть разделены пробелами и концами строк.
# Напишите программу, которая выводит сумму чисел в выходной файл answer.txt.
from site import abs_paths
from wsgiref.util import shift_path_info

numbers = open('numbers6.txt', 'r')

numbers_list = [int(num) for i_line in numbers for num in i_line.split()]
sum_numbers = sum(numbers_list)

numbers.close()

answer = open('answer6.txt', 'w')
answer.write(str(sum_numbers))
answer.close()


# Задача 2. Дзен Пайтона
# Что нужно сделать
# В файле zen.txt хранится так называемый Дзен Пайтона — текст философии программирования на языке Python. Выглядит
# он так:
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
#
# Напишите программу, которая выводит на экран все строки этого файла в обратном порядке.
#
# Кстати, попробуйте открыть консоль Python и ввести команду import this.
#
# Результат работы программы:
#
# Namespaces are one honking great idea -- let's do more of those!
# If the implementation is easy to explain, it may be a good idea.
# If the implementation is hard to explain, it's a bad idea.
# Although never is often better than *right* now.
# …

zen = open('zen.txt', 'r')

zen_str = zen.readlines()
zen_str.reverse()
print(''.join(zen_str))
zen.close()

# Задача 3. Дзен Пайтона — 2
# Что нужно сделать
# Напишите программу, которая определяет, сколько букв (латинского алфавита), слов и строк в файле zen.txt (который
# содержит всё тот же «Дзен Пайтона»). Выведите три найденных числа на экран.
#
# Дополнительно: выведите на экран букву, которая встречается в тексте наименьшее количество раз.
#
# Формат вывода:
# Количество букв в файле:
# Количество слов в файле:
# Количество строк в файле:
# Наиболее редкая буква:

zen = open('zen.txt', 'r')

count_letter = 0
count_word = 0
count_lines = 0
letter_dict = dict()

for i_line in zen:
    count_lines += 1
    count_word += len(i_line.split())
    for i_letter in i_line:
        if i_letter.isalpha():
            count_letter += 1
            if i_letter.lower() in letter_dict:
                letter_dict[i_letter.lower()] += 1
            else:
                letter_dict[i_letter.lower()] = 1

print('Количество букв в файле:', count_letter)
print('Количество слов в файле:', count_word)
print('Количество строк в файле:', count_lines)
print('Наиболее редкая буква:', min(letter_dict, key=letter_dict.get))

zen.close()


# Задача 4. Файлы и папки
# Что нужно сделать
# Напишите программу, которая получает на вход путь до каталога (это может быть и просто корень диска) и выводит
# общее количество файлов и подкаталогов в нём. Также выведите на экран размер каталога в килобайтах
# (1 килобайт = 1024 байт).
#
# Важный момент: чтобы посчитать, сколько весит каталог, нужно найти сумму размеров всех вложенных в него файлов.
# Результат работы программы на примере python_basic\Module14:
#
# E:\PycharmProjects\python_basic\Module14
# Размер каталога (в Кб): 8.373046875
# Количество подкаталогов: 7
# Количество файлов: 15
import os

def dir_info(path):
    count_file = 0
    count_dir = 0
    size_dir = 0
    for i_elem in os.listdir(path):
        i_path = os.path.join(path, i_elem)
        if os.path.isdir(i_path):
            count_dir += 1
            c_file, c_dir, s_dir = dir_info(i_path)
            count_dir += c_dir
            count_file += c_file
            size_dir += s_dir
        elif os.path.isfile(i_path):
            count_file += 1
            size_dir += os.path.getsize(i_path)
    return count_file, count_dir, size_dir



path = input('Введите путь до каталога: ')
count_file, count_dir, size_dir = dir_info(path)
print('Размер каталога (в Кб):', size_dir)
print('Количество подкаталогов:', count_dir)
print('Количество файлов:', count_file)

# Задача 5. Сохранение
# Что нужно сделать
# Мы продолжаем работать над усовершенствованием своего текстового редактора. Конечно же, при работе с редактором
# пользователь, скорее всего, захочет сохранить то, что он написал, в отдельный файл или перезаписать тот, в
# котором он продолжил работать.
#
# Пользователь вводит строку text. Реализуйте функцию, которая запрашивает у пользователя, куда он хочет сохранить
# эту строку: вводится последовательность папок и имя файла (расширение .txt). Затем в этот файл сохраняется
# значение переменной text. Если этот файл уже существует, то нужно спросить у пользователя, действительно ли
# он хочет перезаписать его.
#
# Обеспечьте контроль ввода: указанный из папок путь должен существовать на диске.
#
# Пример 1
#
# Введите строку: programm test
# Куда хотите сохранить документ? Введите последовательность папок (через пробел):
# Users Roman PycharmProjects Skillbox Module22
# Введите имя файла: my_document
# Файл успешно сохранён!
# Содержимое файла:
# programm test
#
# Пример 2
# Введите строку: testiruyem
# Куда хотите сохранить документ? Введите последовательность папок (через пробел):
# Users Roman PycharmProjects Skillbox Module22
# Введите имя файла: my_document
# Вы действительно хотите перезаписать файл? да
# Файл успешно перезаписан!
# Содержимое файла:
# testiruyem

import os

def write_text(path, text):
    file_path = open(path, 'w')
    file_path.write(text)
    file_path.close()

def file_info(path):
    print('Содержимое файла:')
    file_path = open(path, 'r')
    print(file_path.read())
    file_path.close()

def save_text(path, file, text):
    file_path = os.path.join(path, file + '.txt')
    if os.path.exists(file_path):
        answer = input('Вы действительно хотите перезаписать файл? ')
        if answer.lower() == 'да':
            write_text(file_path, text)
            print('Файл успешно перезаписан!')
    else:
        write_text(file_path, text)
    file_info(file_path)

text = input('Введите строку: ')
path_info = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел):')
file = input('Введите имя файла:')

abs_path = os.path.join(os.path.sep, *path_info.split())
save_text(abs_path, file, text)


# Задача 6. Паранойя
# Что нужно сделать
# Артуру постоянно кажется, что за ним следят и все хотят своровать «крайне важную информацию» с его компьютера,
# включая переписку с людьми. Поэтому он эти переписки шифрует. И делает это с помощью шифра Цезаря
# (чем веселит агента службы безопасности).
#
# Напишите программу, которая шифрует содержимое текстового файла text.txt шифром Цезаря, при этом символы первой
# строки файла должны циклически сдвигаться на один, второй строки — на два, третьей строки — на три и так далее.
# Результат выведите в файл cipher_text.txt.
#
# Пример
#
# Содержимое файла text.txt:
#
# Hello
# Hello
# Hello
# Hello
#
# Содержимое файла cipher_text.txt:
#
# Ifmmp
# Jgnnq
# Khoor
# Lipps


def ceasar(text, shift):
    chiper_text = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    for i_char in text:
        if i_char.isalpha():
            if i_char.islower():
                chiper_text += shifted_alphabet[alphabet.index(i_char)]
            else:
                chiper_text += shifted_alphabet[alphabet.index(i_char.lower())].upper()
    return chiper_text

text = open('text.txt', 'r')
cipher_text = open('cipher_text.txt', 'w')


shift = 1
for i_line in text:
    print(i_line)
    ciper = ceasar(i_line, shift)
    shift += 1
    cipher_text.write(str(ciper) + '\n')

text.close()
cipher_text.close()


# Задача 7. Турнир
# Что нужно сделать
# В файле first_tour.txt записано число K и данные об участниках турнира по настольной игре «Орлеан»: фамилии,
# имена и количество баллов, набранных в первом туре. Во второй тур проходят участники, которые набрали более
# K баллов в первом туре.
#
# Напишите программу, которая выводит в файл second_tour.txt данные всех участников, прошедших во второй тур,
# с нумерацией.
#
# В первой строке нужно вывести в файл second_tour.txt количество участников второго тура. Затем программа
# должна вывести фамилии, инициалы и количество баллов всех участников, прошедших во второй тур, с нумерацией.
# Имя нужно сократить до одной буквы. Список должен быть отсортирован по убыванию набранных баллов.
#
# Пример
#
# Содержимое файла first_tour.txt:
#
# 80
# Ivanov Serg 80
# Sergeev Petr 92
# Petrov Vasiliy 98
# Vasiliev Maxim 78
#
# Содержимое файла second_tour.txt:
#
# 2
# 1) V. Petrov 98
# 2) P. Sergeev 92


first_tour = open('first_tour.txt', 'r')

min_point = int(first_tour.readline().split()[0])

second_player_dict = dict()

for i_line in first_tour:
    player_info = i_line.split()
    if int(player_info[2]) > min_point:
        second_player_dict[(player_info[0], player_info[1])] = int(player_info[2])
first_tour.close()

count_second = 1

second_tour = open('second_tour.txt', 'w')
for i_s in sorted(second_player_dict, key=second_player_dict.get, reverse=True):
    new_second_player = f'{count_second}){i_s[1][:1]}.{i_s[0]} {second_player_dict[i_s]} \n'
    second_tour.write(new_second_player)
    count_second += 1
second_tour.close()

# Задача 8. Частотный анализ
# Что нужно сделать
# Есть файл text.txt, который содержит текст. Напишите программу, которая выполняет частотный анализ, определяя долю
# каждой буквы английского алфавита в общем количестве английских букв в тексте, и выводит результат в файл
# analysis.txt. Символы, не являющиеся буквами английского алфавита, учитывать не нужно.
#
# В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, с тремя знаками в дробной части.
# Буквы должны быть отсортированы по убыванию их доли. Буквы с равной долей должны следовать в алфавитном порядке.
#
# Пример
#
# Содержимое файла text.txt:
# Mama myla ramu.
# Содержимое файла analysis.txt:
# a 0.333
# m 0.333
# l 0.083
# r 0.083
# u 0.083
# y 0.083

text = open('text.txt', 'r')
char_dict = dict()
count_alpha_char = 0

for i_line in text:
    for i_char in i_line:
        if i_char.isalpha():
            count_alpha_char += 1
            i_char = i_char.lower()
            if i_char in char_dict:
                char_dict[i_char] += 1
            else:
                char_dict[i_char] = 1

text.close()

for i_char, i_cnt in char_dict.items():
    char_dict[i_char] = round(i_cnt / count_alpha_char, 3)

analysis = open('analysis.txt', 'w')

for i_char in sorted(char_dict, key=char_dict.get, reverse=True):
    new_line = f'{i_char} {char_dict[i_char]}\n'
    analysis.write(new_line)

analysis.close()

