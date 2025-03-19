# Задание 1. Тестовое задание
# Степан устраивается на работу и должен выполнить тестовое задание: проанализировать таблицу, понять, как она
# строится, и написать программу для её вывода на экран.
for row in range(6):
    for col in range(6):
        print(col * 2 + row, end = '\t')
    print()

# Задание 2. Лестница
# Что нужно сделать
# Напишите программу, которая выводит «лестницу» из чисел, когда пользователь вводит число N:

number = int(input('Введите число: '))

for row in range(number):
    for col in range(number - row - 1, number):
        print(row + 1, end=' ')
    print()

# Задание 3. Рамка
# Что нужно сделать
# Напишите программу, которая рисует прямоугольную рамку с помощью символьной графики. Для вертикальных линий
# используйте символ вертикального штриха (|), а для горизонтальных — дефис (-). Пусть ширину и высоту рамки
# определяет пользователь.
height = int(input('Введите высоту: '))
width = int(input('Введите ширину: '))

for row in range(height):
    for col in range(width):
        if (col == 0) or (col == width - 1):
            print('|', end='')
        elif (row == 0) or (row == height - 1):
            print('-', end='')
        else:
            print(' ', end='')
    print()

# Задание 4. Простые числа
# Что нужно сделать
# Напишите программу, которая считает количество простых чисел в заданной последовательности и выводит ответ на экран.
#
# Простое число делится только на себя и на единицу. Последовательность задаётся при помощи вызова ввода (input)
# на каждой итерации цикла. Одна итерация — одно число.
count_number = int(input('Введите количество чисел: '))
count_simple_number = 0

for index in range(count_number):
    number = int(input(f'Введите {index} число: '))
    simple = True
    for i in range(2, number):
        if number % i == 0:
            simple = False
            break
    if simple:
        count_simple_number += 1

print('Количество простых чисел:', count_simple_number)

# Задание 5. Наибольшая сумма цифр
# Что нужно сделать
# Пользователь вводит N чисел. Среди натуральных чисел, которые он указал, найдите наибольшее по сумме цифр.
# Выведите на экран это число и сумму его цифр.
count_number = int(input('Введите количество чисел: '))
max_sum_number = 0
max_number = 0

for index in range(count_number):
    number = int(input(f'введите {index} число: '))
    tmp_number = number
    sum_number = 0
    while number > 0:
        sum_number += number % 10
        number //= 10
    if sum_number > max_sum_number:
        max_sum_number = sum_number
        max_number = tmp_number
print(f'Число {max_number} имеет самую большую сумму чисел - {max_sum_number}')

# Задание 6. Пирамидка
# Что нужно сделать
# Напишите программу, которая выводит на экран равнобедренный треугольник (пирамидку), заполненный символами хештега
# (#). Пусть высоту пирамиды определяет пользователь.
height = int(input('Введите высоту пирамидки: '))
width = height * 2 - 1

for row in range(height):
    for col in range(width):
        if ((width // 2 - row) <= col) and ((width // 2 + row) >= col) :
            print('#', end='')
        else:
            print(' ', end='')
    print()

# Задание 7. Пирамидка-2
# Что нужно сделать
# Напишите программу, которая получает на вход количество уровней пирамиды и выводит их на экран, заполняя
# нечётными числами:
height = int(input('Введите высоту пирамидки: '))
n = 1

for row in range(height):
    space_before = height - row - 1
    print('   ' * space_before, end='')
    for col in range(row+1):
        print(n, end='    ')
        n += 2
    print()

# Задание 8. Яма
# Что нужно сделать
# Представьте, что вы разрабатываете компьютерную игру с текстовой графикой. Вам поручили создать генератор ландшафта.
# Напишите программу, которая получает на вход число N и выводит на экран числа в виде ямы:
height = int(input('Введите высоту пирамидки: '))
width = height * 2

for row in range(height):
    for col in range(width):
        if col < width // 2 and col <= row:
            print(width // 2 - col, end='')
        elif col >= width // 2 and col + row >= width - 1:
            print(col + 1 - width // 2, end='')
        else:
            print('.', end='')
    print()