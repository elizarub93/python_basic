# Задача 1. Пятый элемент
#
# В курсе по программированию студенту дали простую задачу: умножить константу (число 42) на пятый элемент строки,
# введённой пользователем. Вот код студента:
#
# BRUCE_WILLIS = 42
#
# input_data = input('Введите строку: ')
# leeloo = int(input_data[4])
# result = BRUCE_WILLIS * leeloo
# print(f'- Leeloo Dallas! Multi-pass № {result}!')
#
# Модифицируйте этот код, обработав исключения для произвольных входных параметров:
#
# ValueError — невозможно преобразовать к числу,
# IndexError — выход за границы списка,
# остальные исключения.
# Для каждого типа исключений выведите на консоль соответствующее сообщение.

BRUCE_WILLIS = 42
input_data = input('Введите строку: ')
try:
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except ValueError:
    print('Невозможно преобразовать к числу пятый элемент')
except IndexError:
    print('Введенная строка имеет меньше пяти элементов')
except BaseException:
    print('Невозможно рассчитать пятый элемент')

# Задача 2. Возраст
#
# Дан файл ages.txt, в котором построчно хранятся десять возрастов для каждого человека.
#
# Напишите программу, которая считывает файл, даёт имя для каждого возраста (можно просто использовать буквы алфавита)
# и выводит результат в новый файл result.txt в формате «имя — возраст». Программа должна обрабатывать следующие ошибки
# и выводить сообщение на экран:
#
# Попытка создания файла, который уже существует.
# На чтение ожидался файл, но это оказалась директория.
# Неверный тип данных и некорректное значение (две ошибки обрабатываются одинаково).
# При желании воспользуйтесь подсказкой, чтобы найти подходящие имена ошибок.
import random
import string

try:
    ages = open('ages.txt', 'r')
    result = open('result.txt', 'x')
    for i_line in ages:
        age = int(i_line)
        new_line = f'{random.choice(string.ascii_uppercase)} - {age} \n'
        result.write(new_line)
    ages.close()
    result.close()
except FileExistsError:
    print('Файл result.txt уже существует')
except IsADirectoryError:
    print('Для чтения необходимо ввести файл')
except (ValueError, TypeError):
    print('В файле неверный тип данных или некорректное значение')