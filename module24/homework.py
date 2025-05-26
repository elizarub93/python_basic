# Задача 1. Имена — 2
# Что нужно сделать
# Есть файл people.txt, в котором построчно хранится N имён пользователей.
#
# Напишите программу, которая берёт количество символов в каждой строке файла и в качестве ответа выводит общую сумму.
# Если в какой-либо строке меньше трёх символов (не считая литерала \n), то вызывается ошибка и сообщение, в какой
# именно строке возникла ошибка. Программа при этом не завершается и обрабатывает все имена файла.
#
# Также при желании можно вывести все ошибки в отдельный файл errors.log.
#
# Пример работы программы
#
# Содержимое файла people.txt:
#
# Василий
# Николай
# Надежда
# Никита
# Ян
# Ольга
# Евгения
# Кристина
#
# Ответ в консоли:
#
# Ошибка: менее трёх символов в строке 5.
# Общее количество символов: 49.

line_count = 0
sum_sim = 0

with open('people.txt', 'r', encoding='utf-8') as people_file:
    for people in people_file:
        line_count += 1
        try:
            people = people.rstrip()
            count_char = len(people)
            if count_char < 3:
                raise ValueError
            else:
                sum_sim += count_char
        except ValueError:
            print('Ошибка: менее трёх символов в строке {}'.format(line_count))

print('Общее количество символов:', sum_sim)

# Задача 2. Координаты
# Что нужно сделать
# Есть файл coordinates.txt, в котором хранится N пар из чисел X и Y. Оба числа передаются в первую функцию, где
# к каждой координате прибавляется случайное число (от 0 до 5 и от 0 до 10) и возвращается результат деления X на Y.
# Затем эти же координаты передаются во вторую функцию, где уже отнимается случайное число и возвращается Y/X.
#
# После этого формируется случайное число от 0 до 100, затем в файл result.txt в каждую строку записывается
# отсортированный список, состоящий из этого случайного числа и двух полученных результатов.
#
# Один программист уже написал за нас программу для этой задачи, но «почему-то» его вариант решения отклонили.
# Вот его код:

# import random
#
# def f(x, y):
#     x += random.randint(0, 10)
#     y += random.randint(0, 5)
#     return x / y
#
# def f2(x, y):
#     x -= random.randint(0, 10)
#     y -= random.randint(0, 5)
#     return y / x
#
# try:
#     file = open('coordinates.txt', 'r')
#     for line in file:
#         nums_list = line.split()
#         res1 = f(int(nums_list[0]), int(nums_list[1]))
#         try:
#             res2 = f2(int(nums_list[0]), int(nums_list[1]))
#             try:
#                 number = random.randint(0, 100)
#                 file_2 = open('result.txt', 'w')
#                 my_list = sorted([res1, res2, number])
#                 file_2.write(' '.join(my_list))
#             except Exception:
#                 print("Что-то пошло не так : ")
#         except Exception:
#             print("Что-то пошло не так со второй функцией")
#         finally:
#             file.close()
#             file_2.close()
# except Exception:
#     print("Что-то пошло не так с первой функцией")


import random

def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y

def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x

file = open('coordinates.txt', 'r')
file_2 = open('result.txt', 'w')
for line in file:
    nums_list = line.split()
    try:
        res1 = f(int(nums_list[0]), int(nums_list[1]))
        try:
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            number = random.randint(0, 100)
            my_list = sorted([res1, res2, number])
            text = ' '.join(map(str, my_list)) + '\n'
            file_2.writelines(text)
        except ZeroDivisionError:
            print('Что-то пошло не так со второй функцией')
    except ZeroDivisionError:
        print('Что-то пошло не так с первой функцией')

file.close()
file_2.close()


# Задача 3. Счастливое число
# Что нужно сделать
# Напишите программу, которая запрашивает у пользователя число до тех пор, пока сумма этих чисел не станет больше
# либо равна 777. Каждое введённое число при этом дозаписывается в файл out_file.txt. Сделайте так, чтобы перед
# дозаписью программа с вероятностью 1 к 13 выбрасывала пользователю случайное исключение и завершалась.

# Пример 1
#
# Введите число: 10
# Введите число: 500
# Введите число: 200
# Введите число: 67
# Вы успешно выполнили условие для выхода из порочного цикла!
#
# Содержимое файла out_file.txt:
#
# 10
# 500
# 200
# 67
#
# Пример 2
#
# Введите число: 10
# Введите число: 500
# Вас постигла неудача!
#
# Содержимое файла out_file.txt:
#
# 10

import random

try:
    with open('out_file.txt', 'w') as out_file:
        full_sum = 0
        while full_sum < 777:
            number = int(input('Введите число: '))
            if random.randint(1, 13) != 13:
                out_file.write(str(number) + '\n')
                full_sum += number
            else:
                raise BaseException
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
except BaseException:
    print('Вас постигла неудача!')

print('Содержимое файла out_file.txt:')
with open('out_file.txt', 'r') as out_file:
    for i_line in out_file:
        print(i_line, end='')


# Задача 4. Регистрация
# Что нужно сделать
# У вас есть файл с протоколом регистраций пользователей на сайте — registrations.txt. Каждая строка содержит имя,
# имейл и возраст, разделённые пробелами. Например: Василий test@test.ru 27.
#
# Напишите программу, которая проверяет данные из файла для каждой строки:
#
# Присутствуют все три поля.
# Поле «Имя» содержит только буквы.
# Поле «Имейл» содержит @ и . (точку).
# Поле «Возраст» является числом от 10 до 99.
# В результате проверки сформируйте два файла:
#
# log — для правильных данных, записывать строки в том виде, как есть;
# log — для ошибочных, записывать строку и вид ошибки.
# Для валидации строки данных напишите функцию, которая может выдавать исключения:
#
# НЕ присутствуют все три поля: IndexError.
# Поле «Имя» содержит НЕ только буквы: NameError.
# Поле «Имейл» НЕ содержит @ и . (точку): SyntaxError.
# Поле «Возраст» НЕ является числом от 10 до 99: ValueError.

def check_data(name, email, age):
    if not name and not email and not age:
        raise IndexError
    if not name.isalpha():
        raise NameError
    if not ('%' in email or '.' in email):
        raise SyntaxError
    if int(age) < 10 or int(age) > 99:
        raise ValueError

with open('registrations.txt', 'r', encoding='utf-8') as registration:
    reg_bad = open('registrations_bad.log', 'w', encoding='utf-8')
    reg_good = open('registrations_good.log', 'w', encoding='utf-8')
    for i_line in registration:
        try:
            name, email, age = i_line.split()
            check_data(name, email, age)
            reg_good.write(i_line)
        except IndexError:
            reg_bad.write(i_line.rstrip() + ' НЕ присутствуют все три поля \n')
        except NameError:
            reg_bad.write(i_line.rstrip() + ' Поле «Имя» содержит НЕ только буквы \n')
        except SyntaxError:
            reg_bad.write(i_line.rstrip() + ' Поле «Имейл» НЕ содержит @ и . (точку) \n')
        except ValueError:
            reg_bad.write(i_line.rstrip() + ' Поле «Возраст» НЕ является числом от 10 до 99 \n')
    reg_bad.close()
    reg_good.close()

# Задача 5. Текстовый калькулятор
# Что нужно сделать
# Иван стоит на пороге величайшего открытия (не будем его расстраивать), которое перевернёт представление обо всей
# математике и программировании. Имя этому открытию — текстовый калькулятор. Правда, код для своего открытия ему
# сложно написать самому, и поэтому он попросил вас помочь ему. Так что уже можно бежать в патентное бюро.
#
# Есть файл calc.txt, в котором хранятся записи вида:
#
# 100 + 34,
# 23 / 4,
# то есть ОПЕРАНД_1 ОПЕРАЦИЯ ОПЕРАНД_2, разделённые пробелами.
#
# Операнды — целые числа. Операции — арифметические (включая деление нацело и нахождение остатка).
#
# Напишите программу, которая вычисляет все эти операции и находит сумму их результатов. Пропишите обработку возможных
# ошибок. Программа не должна завершаться при первой же ошибке, она учитывает все верные строки и выводит найденный
# ответ.
#
# После успешного выполнения задания, попробуйте модифицировать задачу. Теперь пользователю на экран должно
# выводиться сообщение с ошибочной строкой и предложением её исправить.
#
# Пример 1
#
# Содержимое файла calc.txt:
#
# 100 + 34
# 10 +* 3
# 23 / 4
#
# Содержимое консоли:
#
# Обнаружена ошибка в строке: 10 +* 3   Хотите исправить? Да
#
# Введите исправленную строку: 10 + 3
#
# Сумма результатов: 152.75
#
# Пример 2
#
# Содержимое файла calc.txt:
#
# 100 + 34
# 10 +* 3
# 20 -* 2
# 23 / 4
#
# Содержимое консоли:
#
# Обнаружена ошибка в строке: 10 +* 3   Хотите исправить? Нет
# Обнаружена ошибка в строке: 20 -* 2   Хотите исправить? Да
# Введите исправленную строку: 20 - 2
# Сумма результатов: 157.75

def oper_num(num1, num2, oper):
    if oper == '+':
        res = int(num1) + int(num2)
    elif oper == '-':
        res = int(num1) - int(num2)
    elif oper == '*':
        res = int(num1) * int(num2)
    elif oper == '/':
        res = int(num1) * int(num2)
    elif oper == '%':
        res = int(num1) % int(num2)
    elif oper == '//':
        res = int(num1) // int(num2)
    elif oper == '**':
        res = int(num1) ** int(num2)
    else:
        raise ValueError
    return res

sum_res = 0

with open('calc.txt') as calc:
    for i_line in calc:
        try:
            num1, oper, num2 = i_line.split()
            sum_res += oper_num(num1, num2, oper)
        except ValueError:
            answer = input(f'Обнаружена ошибка в строке: {i_line.rstrip()} Хотите исправить? ')
            if answer.lower() == 'да':
                new_line = input('Введите исправленную строку:').split()
                sum_res += oper_num(new_line[0], new_line[2], new_line[1])


print('Сумма результатов:', sum_res)


# Задача 6. Чат
# Что нужно сделать
# Реализуйте программу — чат, в котором могут участвовать сразу несколько человек, то есть программа может работать
# одновременно для нескольких пользователей. При запуске запрашивается имя пользователя. После этого он
# выбирает одно из действий:
#
# Посмотреть текущий текст чата.
# Отправить сообщение (затем вводит сообщение).
# Действия запрашиваются бесконечно.
#
# Примечание: для решения задачи вам будет достаточно текущих знаний, нужно лишь проявить немного фантазии и хитрости.
# Не нужно лезть в дебри работы с сетями, создания GUI-приложений и прочих штук. (Но если очень хочется,
# то останавливать вас никто не будет!)

def show_chat(file_name):
    try:
        with open(file_name, 'r') as chat:
            message = chat.readline()
            print(' '.join(message))
    except FileNotFoundError:
        print('Чат не найден')

def add_message(file_name, user_name, message):
    with open(file_name, 'a') as chat:
        chat.write('{name}: {message}\n'.format(name=user_name, message=message))

file_name = 'chat.txt'
user_name = input('Введите имя: ')

while True:
    action = int(input('Выберите действие: 1 - просмотр истории чата, 2 - отправить сообщение: '))
    if action == 1:
        show_chat(file_name)
    elif action == 2:
        message = input('Введите сообщение: ')
        add_message(file_name, user_name, message)
    else:
        print('Выбрано некорректное действие')

